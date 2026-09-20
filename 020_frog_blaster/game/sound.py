from pathlib import Path
import pygame as pg
import random

BASE_DIR = Path(__file__).resolve().parent
SND_DIR  = BASE_DIR / "sounds"

class SoundManager():
    instance = None

    def get_instance():
        if SoundManager.instance is None:
            SoundManager.instance = SoundManager()
        return SoundManager.instance

    def __init__(self):
        pg.mixer.music.load(SND_DIR / "bgm.wav")
        self.over  = pg.mixer.Sound(SND_DIR / "over.wav")
        self.clear = pg.mixer.Sound(SND_DIR / "clear.wav")
        self.clap1 = pg.mixer.Sound(SND_DIR / "clap1.wav")
        self.clap2 = pg.mixer.Sound(SND_DIR / "clap2.wav")
        self.clap3 = pg.mixer.Sound(SND_DIR / "clap3.wav")
        self.blast = pg.mixer.Sound(SND_DIR / "blast.wav")
        self.bomb  = pg.mixer.Sound(SND_DIR / "bomb.wav")

    def bgmstart(self):
        pg.mixer.music.play(-1)

    def bgmstop(self):
        pg.mixer.music.stop()

    def playover(self):
        self.over.play()

    def playclear(self):
        self.clear.play()

    def playattack(self):
        random.choice([self.clap1, self.clap2, self.clap3]).play()

    def playblast(self):
        self.blast.play()

    def playbomb(self):
        self.bomb.play()
