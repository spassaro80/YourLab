from django.db import models
from django.utils import timezone
import datetime 

# Create your models here.
class Match(models.Model):
    chanpionship = models.CharField(max_length=200, verbose_name = 'Campionato')
    place = models.CharField(max_length=200, verbose_name = 'Luogo')
    date = models.DateField(default=timezone.now, blank=True, verbose_name="Data")
    time = models.TimeField(default=timezone.now, blank=True, verbose_name = 'Hora')
    weather = models.CharField(max_length=200, verbose_name = 'Tempo')
    temperature = models.CharField(max_length=200, verbose_name = 'Temperatura')
    team_a = models.CharField(max_length=200, verbose_name = 'Squadra di Casa')
    team_b = models.CharField(max_length=200, verbose_name = 'Squadra Ospite')

    def __str__(self):
        return (self.team_a + " vs " + self.team_b + " in data " + str(self.date))

    class Meta:
        verbose_name_plural = "Partite"

class Stats(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='stats')
    first_half = models.TimeField(max_length=200, blank=True, null=True, default="00:00:00", verbose_name = 'Primo Tempo')
    second_half = models.TimeField(max_length=200, blank=True, null=True, default="00:00:00", verbose_name = 'Secondo Tempo')
    possession1A= models.TimeField(max_length=200, blank=True, null=True, default="00:00:00", verbose_name = 'Possesso Palla Squadra A Primo Tempo')
    possession1B = models.TimeField(max_length=200, blank=True, null=True, default="00:00:00", verbose_name = 'Possesso Palla Squadra B Primo Tempo')
    possession2A= models.TimeField(max_length=200, blank=True, null=True, default="00:00:00", verbose_name = 'Possesso Palla Squadra A Secondo Tempo')
    possession2B = models.TimeField(max_length=200, blank=True, null=True, default="00:00:00", verbose_name = 'Possesso Palla Squadra B Secondo Tempo')
    possessionA= models.TimeField(max_length=200, blank=True, null=True, default="00:00:00", verbose_name = 'Possesso Palla Squadra A ')
    possessionB = models.TimeField(max_length=200, blank=True, null=True, default="00:00:00", verbose_name = 'Possesso Palla Squadra B')
    tiri_in_porta1A_sx = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Tiri in porta a sinistra Primo Tempo Squadra A")
    tiri_in_porta1A_dx = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Tiri in porta a destra Primo Tempo Squadra A")
    tiri_in_porta1A_cc = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Tiri in porta al centro Primo Tempo Squadra A")
    tiri_in_porta1A = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Tiri in porta Primo Tempo Squadra A")
    tiri_in_fuori1A_sx = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Tiri in fuori a sinistra Primo Tempo Squadra A")
    tiri_in_fuori1A_dx = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Tiri in fuori a destra Primo Tempo Squadra A")
    tiri_in_fuori1A_cc = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Tiri in fuori al centro Primo Tempo Squadra A")
    tiri_in_fuori1A = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Tiri in fuori Primo Tempo Squadra A")
    punizioni_difensive1A_sx = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Punizioni difensive a sinistra Primo Tempo Squadra A")
    punizioni_difensive1A_dx = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Punizioni difensive a destra Primo Tempo Squadra A")
    punizioni_difensive1A_cc = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Punizioni difensive al centro Primo Tempo Squadra A")
    punizioni_difensive1A = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Punizioni difensive  Primo Tempo Squadra A")
    punizioni_offensive1A_sx = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Punzioni offensive a sinistra Primo Tempo Squadra A")
    punizioni_offensive1A_dx = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Punzioni offensive a destra Primo Tempo Squadra A")
    punizioni_offensive1A_cc = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Punzioni offensive al centro Primo Tempo Squadra A")
    punizioni_offensive1A = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Punzioni offensive Primo Tempo Squadra A")
    cross_dx1A = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Cross a destra Primo Tempo Squadra A")
    cross_cc1A = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Cross al centro Primo Tempo Squadra A")
    cross_sx1A = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Cross a sinistra Primo Tempo Squadra A")
    cross1A = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Cross  Primo Tempo Squadra A")
    corners1A = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Calci d'angolo Primo Tempo Squadra A")
    parate1A = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Parate Primo Tempo Squadra A")
    fuorigioco1A = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Fuorigioco Primo Tempo Squadra A")
    tiri_in_porta1B_sx = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Tiri in porta a sinistra Primo Tempo Squadra B")
    tiri_in_porta1B_dx = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Tiri in porta a destra Primo Tempo Squadra B")
    tiri_in_porta1B_cc = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Tiri in porta al centro Primo Tempo Squadra B")
    tiri_in_fuori1B_sx = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Tiri in fuori a sinistra Primo Tempo Squadra B")
    tiri_in_fuori1B_dx = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Tiri in fuori a destra Primo Tempo Squadra B")
    tiri_in_fuori1B_cc = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Tiri in fuori al centro Primo Tempo Squadra B")
    punizioni_difensive1B_sx = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Punizioni difensive a sinistra Primo Tempo Squadra B")
    punizioni_difensive1B_dx = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Punizioni difensive a destra Primo Tempo Squadra B")
    punizioni_difensive1B_cc = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Punizioni difensive al centro Primo Tempo Squadra B")
    punizioni_offensive1B_sx = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Punzioni offensive a sinistra Primo Tempo Squadra B")
    punizioni_offensive1B_dx = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Punzioni offensive a destra Primo Tempo Squadra B")
    punizioni_offensive1B_cc = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Punzioni offensive al centro Primo Tempo Squadra B")
    punizioni_offensive1B_sx = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Punzioni offensive a sinistra Primo Tempo Squadra B")
    cross_dx1B = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Cross a destra Primo Tempo Squadra B")
    cross_cc1B = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Cross al centro Primo Tempo Squadra B")
    cross_sx1B = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Cross a sinistra Primo Tempo Squadra B")
    corners1B = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Calci d'angolo Primo Tempo Squadra B")
    parate1B = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Parate Primo Tempo Squadra B")
    fuorigioco1B = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Fuorigioco Primo Tempo Squadra B")
    tiri_in_porta2A_sx = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Tiri in porta a sinistra Secondo Tempo Squadra A")
    tiri_in_porta2A_dx = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Tiri in porta a destra Secondo Tempo Squadra A")
    tiri_in_porta2A_cc = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Tiri in porta al centro SecondoTempo Squadra A")
    tiri_in_fuori2A_sx = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Tiri in fuori a sinistra Secondo Tempo Squadra A")
    tiri_in_fuori2A_dx = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Tiri in fuori a destra Secondo Tempo Squadra A")
    tiri_in_fuori2A_cc = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Tiri in fuori al centro SecondoTempo Squadra A")
    punizioni_difensive2A_sx = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Punizioni difensive a sinistra Secondo Tempo Squadra A")
    punizioni_difensive2A_dx = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Punizioni difensive a destra Secondo Tempo Squadra A")
    punizioni_difensive2A_cc = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Punizioni difensive al centro SecondoTempo Squadra A")
    punizioni_offensive2A_sx = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Punzioni offensive a sinistra Secondo Tempo Squadra A")
    punizioni_offensive2A_dx = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Punzioni offensive a destra Secondo Tempo Squadra A")
    punizioni_offensive2A_cc = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Punzioni offensive al centro SecondoTempo Squadra A")
    punizioni_offensive2A_sx = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Punzioni offensive a sinistra Secondo Tempo Squadra A")
    cross_dx2A = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Cross a destra Secondo Tempo Squadra A")
    cross_cc2A = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Cross al centro SecondoTempo Squadra A")
    cross_sx2A = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Cross a sinistra Secondo Tempo Squadra A")
    corners2A = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Calci d'angolo Secondo Tempo Squadra A")
    parate2A = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Parate Secondo Tempo Squadra A")
    fuorigioco2A = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Fuorigioco Secondo Tempo Squadra A")
    tiri_in_porta2B_sx = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Tiri in porta a sinistra Secondo Tempo Squadra B")
    tiri_in_porta2B_dx = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Tiri in porta a destra Secondo Tempo Squadra B")
    tiri_in_porta2B_cc = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Tiri in porta al centro SecondoTempo Squadra B")
    tiri_in_fuori2B_sx = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Tiri in fuori a sinistra Secondo Tempo Squadra B")
    tiri_in_fuori2B_dx = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Tiri in fuori a destra Secondo Tempo Squadra B")
    tiri_in_fuori2B_cc = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Tiri in fuori al centro SecondoTempo Squadra B")
    punizioni_difensive2B_sx = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Punizioni difensive a sinistra Secondo Tempo Squadra B")
    punizioni_difensive2B_dx = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Punizioni difensive a destra Secondo Tempo Squadra B")
    punizioni_difensive2B_cc = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Punizioni difensive al centro SecondoTempo Squadra B")
    punizioni_offensive2B_sx = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Punzioni offensive a sinistra Secondo Tempo Squadra B")
    punizioni_offensive2B_dx = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Punzioni offensive a destra Secondo Tempo Squadra B")
    punizioni_offensive2B_cc = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Punzioni offensive al centro SecondoTempo Squadra B")
    punizioni_offensive2B_sx = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Punzioni offensive a sinistra Secondo Tempo Squadra B")
    cross_dx2B = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Cross a destra Secondo Tempo Squadra B")
    cross_cc2B = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Cross al centro SecondoTempo Squadra B")
    cross_sx2B = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Cross a sinistra Secondo Tempo Squadra B")
    corners2B = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Calci d'angolo Secondo Tempo Squadra B")
    parate2B = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Parate Secondo Tempo Squadra B")
    fuorigioco2B = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Fuorigioco Secondo Tempo Squadra B")
    tiri_in_porta1B = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Tiri in porta Primo Tempo Squadra B")
    tiri_in_fuori1B = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Tiri in fuori Primo Tempo Squadra B")
    punizioni_difensive1B = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Punizioni difensive  Primo Tempo Squadra B")
    punizioni_offensive1B = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Punzioni offensive Primo Tempo Squadra B")
    cross1B = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Cross  Primo Tempo Squadra B")
    tiri_in_porta2A = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Tiri in porta Secondo Tempo Squadra A")
    tiri_in_fuori2A = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Tiri in fuori Secondo Tempo Squadra A")
    punizioni_difensive2A = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Punizioni difensive  Secondo Tempo Squadra A")
    punizioni_offensive2A = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Punzioni offensive Secondo Tempo Squadra A")
    cross2A = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Cross  Secondo Tempo Squadra A")
    tiri_in_porta2B = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Tiri in porta Secondo Tempo Squadra B")
    tiri_in_fuori2B = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Tiri in fuori Secondo Tempo Squadra B")
    punizioni_difensive2B = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Punizioni difensive  Secondo Tempo Squadra B")
    punizioni_offensive2B = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Punzioni offensive Secondo Tempo Squadra B")
    cross2B = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Cross  Secondo Tempo Squadra B")
    tiri_in_porta1 = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Totale Tiri in porta Primo Tempo")
    tiri_in_porta2 = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Totale Tiri in porta Secondo Tempo")
    tiri_in_porta = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Total Tiri in porta ")
    tiri_in_fuori1 = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Totale Tiri in fuori Primo Tempo")
    tiri_in_fuori2 = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Totale Tiri in fuori Secondo Tempo")
    tiri_in_fuori = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Total Tiri in fuori ")
    punizioni_offensive1 = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Totale Punizioni Offensive Primo Tempo")
    punizioni_offensive2 = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Totale Punizioni Offensive Secondo Tempo")
    punizioni_offensive = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Total Punizioni Offensive ")
    punizioni_difensive1 = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Totale Punizioni difensive Primo Tempo")
    punizioni_difensive2 = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Totale Punizioni difensive Secondo Tempo")
    punizioni_difensive = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Total Punizioni difensive ")
    cross1 = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Totale cross Primo Tempo")
    cross2 = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Totale cross Secondo Tempo")
    cross = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Total cross ")
    corners1 = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Totale corners Primo Tempo")
    corners2 = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Totale corners Secondo Tempo")
    corners = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Total corners ")
    parate1 = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Totale parate Primo Tempo")
    parate2 = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Totale parate Secondo Tempo")
    parate = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Total parate ")
    fuorigioco1 = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Totale fuorigioco Primo Tempo")
    fuorigioco2 = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Totale fuorigioco Secondo Tempo")
    fuorigioco = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Total fuorigioco ")
    tiri_in_portaA = models.IntegerField(null=True, blank=True, default=0, verbose_name = "Totale tiri in porta Equipo A")
    tiri_in_fuoriA =models.IntegerField(null=True, blank=True, default=0, verbose_name = "Totale tiri in fuori Equipo A")
    punizioni_offensiveA =models.IntegerField(null=True, blank=True, default=0, verbose_name = "Totale punizioni offensive Equipo A")
    punizioni_difensiveA =models.IntegerField(null=True, blank=True, default=0, verbose_name = "Totale punizioni difensive Equipo A")
    crossA =models.IntegerField(null=True, blank=True, default=0, verbose_name = "Totale cross Equipo A")
    cornersA =models.IntegerField(null=True, blank=True, default=0, verbose_name = "Totale corners Equipo A")
    parateA =models.IntegerField(null=True, blank=True, default=0, verbose_name = "Totale parate Equipo A")
    fuorigiocoA =models.IntegerField(null=True, blank=True, default=0, verbose_name = "Totale fuorigioco Equipo A")
    tiri_in_portaB =models.IntegerField(null=True, blank=True, default=0, verbose_name = "Totale tiri in porta Equipo B")
    tiri_in_fuoriB =models.IntegerField(null=True, blank=True, default=0, verbose_name = "Totale tiri in fuori Equipo B")
    punizioni_offensiveB =models.IntegerField(null=True, blank=True, default=0, verbose_name = "Totale punizioni offensive Equipo B")
    punizioni_difensiveB =models.IntegerField(null=True, blank=True, default=0, verbose_name = "Totale punizioni difensive Equipo B")
    crossB =models.IntegerField(null=True, blank=True, default=0, verbose_name = "Totale cross Equipo B")
    cornersB =models.IntegerField(null=True, blank=True, default=0, verbose_name = "Totale cornerns Equipo B")
    parateB =models.IntegerField(null=True, blank=True, default=0, verbose_name = "Totale parate Equipo B")
    fuorigiocoB =models.IntegerField(null=True, blank=True, default=0, verbose_name = "Totale fuorigioco Equipo B")
    
    
    def __str__(self):
        return ("Statistiche della partita " + str(self.match.team_a) + " vs " + str(self.match.team_b) + " del " + str(self.match.date))
    
    def save(self, *args, **kwargs):
        self.tiri_in_porta1A=self.tiri_in_porta1A_sx + self.tiri_in_porta1A_dx + self.tiri_in_porta1A_cc
        self.tiri_in_fuori1A=self.tiri_in_fuori1A_sx + self.tiri_in_fuori1A_dx + self.tiri_in_fuori1A_cc
        self.punizioni_offensive1A=self.punizioni_offensive1A_sx + self.punizioni_offensive1A_dx + self.punizioni_offensive1A_cc
        self.punizioni_difensive1A=self.punizioni_difensive1A_sx + self.punizioni_difensive1A_dx + self.punizioni_difensive1A_cc
        self.cross1A=self.cross_sx1A + self.cross_dx1A + self.cross_cc1A
        self.tiri_in_porta1B=self.tiri_in_porta1B_sx + self.tiri_in_porta1B_dx + self.tiri_in_porta1B_cc
        self.tiri_in_fuori1B=self.tiri_in_fuori1B_sx + self.tiri_in_fuori1B_dx + self.tiri_in_fuori1B_cc
        self.punizioni_offensive1B=self.punizioni_offensive1B_sx + self.punizioni_offensive1B_dx + self.punizioni_offensive1B_cc
        self.punizioni_difensive1B=self.punizioni_difensive1B_sx + self.punizioni_difensive1B_dx + self.punizioni_difensive1B_cc
        self.cross1B=self.cross_sx1B + self.cross_dx1B + self.cross_cc1B
        self.tiri_in_porta2A=self.tiri_in_porta2A_sx + self.tiri_in_porta2A_dx + self.tiri_in_porta2A_cc
        self.tiri_in_fuori2A=self.tiri_in_fuori2A_sx + self.tiri_in_fuori2A_dx + self.tiri_in_fuori2A_cc
        self.punizioni_offensive2A=self.punizioni_offensive2A_sx + self.punizioni_offensive2A_dx + self.punizioni_offensive2A_cc
        self.punizioni_difensive2A=self.punizioni_difensive2A_sx + self.punizioni_difensive2A_dx + self.punizioni_difensive2A_cc
        self.cross2A=self.cross_sx2A + self.cross_dx2A + self.cross_cc2A
        self.tiri_in_porta2B=self.tiri_in_porta2B_sx + self.tiri_in_porta2B_dx + self.tiri_in_porta2B_cc
        self.tiri_in_fuori2B=self.tiri_in_fuori2B_sx + self.tiri_in_fuori2B_dx + self.tiri_in_fuori2B_cc
        self.punizioni_offensive2B=self.punizioni_offensive2B_sx + self.punizioni_offensive2B_dx + self.punizioni_offensive2B_cc
        self.punizioni_difensive2B=self.punizioni_difensive2B_sx + self.punizioni_difensive2B_dx + self.punizioni_difensive2B_cc
        self.cross2B=self.cross_sx2B + self.cross_dx2B + self.cross_cc2B
        self.tiri_in_porta1 =  self.tiri_in_porta1A + self.tiri_in_porta1B
        self.tiri_in_porta2 =  self.tiri_in_porta2A + self.tiri_in_porta2B
        self.tiri_in_porta = self.tiri_in_porta1 + self.tiri_in_porta2
        self.tiri_in_fuori1 =  self.tiri_in_fuori1A + self.tiri_in_fuori1B
        self.tiri_in_fuori2 =  self.tiri_in_fuori2A + self.tiri_in_fuori2B
        self.tiri_in_fuori = self.tiri_in_fuori1 + self.tiri_in_fuori2
        self.punizioni_offensive1 = self.punizioni_offensive1A + self.punizioni_offensive1B
        self.punizioni_offensive2 = self.punizioni_offensive2A + self.punizioni_offensive2B
        self.punizioni_offensive =  self.punizioni_offensive1 + self.punizioni_offensive2
        self.punizioni_difensive1 = self.punizioni_difensive1A + self.punizioni_difensive1B
        self.punizioni_difensive2 = self.punizioni_difensive2A + self.punizioni_difensive2B
        self.punizioni_difensive =  self.punizioni_difensive1 + self.punizioni_difensive2
        self.cross1 = self.cross1A + self.cross1B
        self.cross2 = self.cross2A + self.cross2B
        self.cross = self.cross1 + self.cross2
        self.corners = self.corners1 + self.corners2
        self.corners1 = self.corners1A + self.corners1B
        self.corners2 = self.corners2A + self.corners2B
        self.parate = self.parate1 + self.parate2
        self.parate1 = self.parate1A + self.parate1B
        self.parate2 = self.parate2A + self.parate2B
        self.fuorigioco = self.fuorigioco1 + self.fuorigioco2
        self.fuorigioco1 = self.fuorigioco1A + self.fuorigioco1B
        self.fuorigioco2 = self.fuorigioco2A + self.fuorigioco2B
        self.tiri_in_portaA = self.tiri_in_porta1A + self.tiri_in_porta2A
        self.tiri_in_fuoriA = self.tiri_in_fuori1A + self.tiri_in_fuori2A
        self.punizioni_offensiveA = self.punizioni_offensive1A + self.punizioni_offensive2A
        self.punizioni_difensiveA = self.punizioni_difensive1A + self.punizioni_difensive2A
        self.crossA = self.cross1A + self.cross2A
        self.cornersA = self.corners1A + self.corners2A
        self.parateA = self.parate1A + self.parate2A
        self.fuorigiocoA = self.fuorigioco1A + self.fuorigioco2A
        self.tiri_in_portaB = self.tiri_in_porta1B + self.tiri_in_porta2B
        self.tiri_in_fuoriB = self.tiri_in_fuori1B + self.tiri_in_fuori2B
        self.punizioni_offensiveB = self.punizioni_offensive1B + self.punizioni_offensive2B
        self.punizioni_difensiveB = self.punizioni_difensive1B + self.punizioni_difensive2B
        self.crossB = self.cross1B + self.cross2B
        self.cornersB = self.corners1B + self.corners2B
        self.parateB = self.parate1B + self.parate2B
        self.fuorigiocoB = self.fuorigioco1B + self.fuorigioco2B
        self.possessionA = (((datetime.datetime.strptime(self.possession1A, '%H:%M:%S')) + datetime.timedelta(hours=datetime.datetime.strptime(self.possession2A,'%H:%M:%S').hour, minutes=datetime.datetime.strptime(self.possession2A,'%H:%M:%S').minute, seconds=datetime.datetime.strptime(self.possession2A,'%H:%M:%S').second)).time())
        self.possessionB = (((datetime.datetime.strptime(self.possession1B, '%H:%M:%S')) + datetime.timedelta(hours=datetime.datetime.strptime(self.possession2B,'%H:%M:%S').hour, minutes=datetime.datetime.strptime(self.possession2A,'%H:%M:%S').minute, seconds=datetime.datetime.strptime(self.possession2B,'%H:%M:%S').second)).time())

        super(Stats,self).save(*args, **kwargs)
    class Meta:
            verbose_name_plural = "Statistiche"

class Event(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='event')
    event = models.CharField(max_length=200, null=True, blank=True, verbose_name="Nuovo evento")
    eventtime = models.TimeField(blank=True, null=True, verbose_name = 'Minuto del nuovo evento')
    team =  models.CharField(max_length=200, verbose_name = 'Squadra')

    def __str__(self):
        return(f"Nuovo evento della partita {self.match} nel minuto {self.eventtime.strftime('%H: %M: %S')}: {self.event} della squadra {self.team}")