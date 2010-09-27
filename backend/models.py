from django.db import models
from django.contrib.auth.models import User

# see http://code.activestate.com/recipes/577268-python-data-structure-to-xml-serialization/
# form model to xml serialization

class Pub(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(blank=True, null=True, max_length=255)
    postal_code = models.CharField(blank=True, null=True, max_length=6)
    city = models.CharField(blank=True, null=True, max_length=255)
    phone = models.CharField(blank=True, null=True, max_length=25)
    email = models.EmailField(blank=True, null=True, max_length=255)
    latitude = models.FloatField(blank=True, null=True, max_length=8)
    longitude = models.FloatField(blank=True, null=True, max_length=8)
    
    def __unicode__(self):
        return self.name
 
class Club(models.Model):
    name = models.CharField(max_length=255)
    pub = models.ForeignKey(Pub)
    
    def __unicode__(self):
        return self.name
    
class Player(models.Model):
    user = models.ForeignKey(User, unique=True)
    moyenne = models.IntegerField(blank=True, null=True, max_length=3)
    club = models.ForeignKey(Club, null=True, blank=True)
    address = models.CharField(blank=True, null=True, max_length=255)
    postal_code = models.CharField(blank=True, null=True, max_length=6)
    city = models.CharField(blank=True, null=True, max_length=255)
    phone = models.CharField(blank=True, null=True, max_length=25)
    
    def fullname(self):
        return self.__unicode__()
    
    def __unicode__(self):
        return self.user.first_name + " " + self.user.last_name

class AgendaItem(models.Model):
    date = models.DateField()
    is_competition = models.BooleanField()
    pub = models.ForeignKey(Pub, null=True, blank=True)
    home_club = models.ForeignKey(Club, related_name="home_agenda_items", null=True, blank=True)
    away_club = models.ForeignKey(Club, related_name="away_agenda_items", null=True, blank=True)
    
    def __unicode__(self):
        return self.date.strftime("%Y-%m-%d") + " @" + self.pub.__unicode__()
    
class Match(models.Model):
    home_player = models.ForeignKey(Player, related_name="home_match")
    home_player_moyenne = models.IntegerField(blank=True, null=True, max_length=3)
    away_player = models.ForeignKey(Player, related_name="away_match")
    away_player_moyenne = models.IntegerField(blank=True, null=True, max_length=3)
    arbiter = models.ForeignKey(Player, related_name="arbiter_at_match", null=True, blank=True)
    writer = models.ForeignKey(Player, related_name="writer_at_match", null=True, blank=True)
    agenda_item = models.ForeignKey( AgendaItem)
    
    def __unicode__(self):
        return self.agenda_item.date.strftime("%Y-%m-%d") + ": " + self.home_player.__unicode__() + " vs. " + self.away_player.__unicode__()
    
class MatchTurn(models.Model):
    match = models.ForeignKey(Match)
    player = models.ForeignKey(Player)
    turn = models.IntegerField(max_length=2)
    score = models.IntegerField(max_length=2)
    
    def __unicode__(self):
        return self.match.__unicode__() + " - " + self.player.__unicode__() + " turn: " + str(self.turn)
    
