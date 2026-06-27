from pathlib import Path
import pygame as pg
import random

BASE_DIR = Path(__file__).resolve().parent
SND_DIR  = BASE_DIR / "sounds"

class SoundManager():
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        pg.mixer.music.load(SND_DIR / "bgm.wav")
        self._over  = pg.mixer.Sound(SND_DIR / "over.wav")
        self._clear = pg.mixer.Sound(SND_DIR / "clear.wav")
        self._clap1 = pg.mixer.Sound(SND_DIR / "clap1.wav")
        self._clap2 = pg.mixer.Sound(SND_DIR / "clap2.wav")
        self._clap3 = pg.mixer.Sound(SND_DIR / "clap3.wav")
        self._blast = pg.mixer.Sound(SND_DIR / "blast.wav")
        self._bomb  = pg.mixer.Sound(SND_DIR / "bomb.wav")

    def bgmstart(self):
        pg.mixer.music.play(-1)

    def bgmstop(self):
        pg.mixer.music.stop()

    def playover(self):
        self._over.play()

    def playclear(self):
        self._clear.play()

    def playattack(self):
        random.choice([self._clap1, self._clap2, self._clap3]).play()

    def playblast(self):
        self._blast.play()

    def playbomb(self):
        self._bomb.play()
