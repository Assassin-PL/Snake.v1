import pygame
from utlis import Config
import random

#Klasa obslugujaca nasz plik konfiguracyjny
config = Config()
ustawienia : str = "SETTINGS"
sciezki : str = "PATHS"
SZEROKOSC_EKRANU = int(config.get(ustawienia,"SZEROKOSC_EKRANU"))
WYSOKOSC_EKRANU = int(config.get(ustawienia, "WYSOKOSC_EKRANU"))

vec = pygame.math.Vector2
class Kulka(pygame.sprite.Sprite):
    def __init__(self):
        super(Kulka, self).__init__()
        self.config = Config()
        self.ustawienia : str = "SETTINGS"
        self.sciezki : str = "PATHS"
        self.obraz = pygame.image.load(self.config.get(self.sciezki, "pilka")) 
        self.zresetujpozycje()
        self.u = 16
        self.przegrana = False
        
    def zresetujpozycje(self):
        self.wspolrzedne = vec(SZEROKOSC_EKRANU / 2, WYSOKOSC_EKRANU - 140)
        self.pozycja = self.obraz.get_rect(center=self.wspolrzedne)
        self.wektor = vec(0, -10)
        self.kat_nachylenia = random.randrange(-30, 30)
        self.wektor.rotate_ip(self.kat_nachylenia)
    
    def aktualizuj(self):
        self.wspolrzedne += self.wektor
        self.pozycja.center = self.wspolrzedne
    
