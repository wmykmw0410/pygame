import pygame as pg
import random
import player, enemy, bullet, status, sound

class Subject:
    def __init__(self) -> None:
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self, ntype):
        for observer in self.observers:
            observer.update(ntype)


class GameManager(Subject):
    def __init__(self) -> None:
        super().__init__()
        self.player  = player.Player()
        self.enemies = []
        self.effects = []
        self.bullets = []
        self.factory = enemy.EnemyFactory()
        self.status  = status.Status()
        self.attach(self.status)
        self.reset()

    def reset(self):
        self.is_playing  = True
        self.is_cleared  = False
        self.player.reset()
        self.enemies.clear()
        self.bullets.clear()
        self.spawn_count  = 0
        self.bullet_count = 0
        self.status.reset()
        sound.SoundManager.get_instance().bgmstart()

    def update(self):
        self.notify("distance")

        # 弾の発射
        self.bullet_count += 1
        if self.bullet_count > 10:
            key = pg.key.get_pressed()
            if key[pg.K_a]:
                self.bullets.append(bullet.Bullet(self.player.rect))
                self.bullet_count = 0

        for eff in self.effects:
            eff.update()
        for b in self.bullets:
            b.update()
        self.player.update()

        # 敵の生成
        self.spawn_count += 1
        if self.spawn_count > 15:
            self.spawn_count = 0
            self.enemies.append(self.factory.random_create())

        dead_enemies = set()
        dead_bullets = set()

        for e in self.enemies:
            e.update()

            # 弾との衝突
            for b in self.bullets:
                if b in dead_bullets:
                    continue
                if e.rect.colliderect(b.rect):
                    sound.SoundManager.get_instance().playattack()
                    dead_bullets.add(b)
                    e.hp -= 50
                    if e.hp <= 0:
                        self.notify("score")
                        effect = enemy.BombEffect(e.rect, self.effects)
                        sound.SoundManager.get_instance().playblast()
                        self.effects.append(effect)
                        dead_enemies.add(e)
                        if self.status.score == 30:
                            self.is_playing = False
                            self.is_cleared = True
                            sound.SoundManager.get_instance().bgmstop()
                            sound.SoundManager.get_instance().playclear()
                    break

            # 画面外に出た敵
            if not e.is_alive:
                dead_enemies.add(e)
                continue

            # 主人公との衝突
            if e not in dead_enemies and e.rect.colliderect(self.player.rect):
                dead_enemies.add(e)
                self.player.damage()
                self.player.hp -= 50
                sound.SoundManager.get_instance().playbomb()
                if self.player.hp <= 0:
                    self.is_playing = False
                    sound.SoundManager.get_instance().bgmstop()
                    sound.SoundManager.get_instance().playover()

        alive_enemies = []
        for e in self.enemies:
            if e not in dead_enemies:
                alive_enemies.append(e)
        self.enemies = alive_enemies

        alive_bullets = []
        for b in self.bullets:
            if b not in dead_bullets and b.is_alive:
                alive_bullets.append(b)
        self.bullets = alive_bullets

    def draw(self, screen):
        for b in self.bullets:
            b.draw(screen)
        for eff in self.effects:
            eff.draw(screen)
        self.player.draw(screen)
        for e in self.enemies:
            e.draw(screen)
        self.status.draw(screen)
