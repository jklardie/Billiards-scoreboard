from django.db import models
from jongGeleerd.backend.models import Pub, Club, Player, Match, MatchTurn, AgendaItem


class Moyenne(models.Model):
    def __init__(self, moyenne=0):
        self.moyenne = moyenne
