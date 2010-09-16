from django.db import models

# see http://code.activestate.com/recipes/577268-python-data-structure-to-xml-serialization/
# form model to xml serialization

class Pub(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=6)
    city = models.CharField(max_length=255)
    phone = models.CharField(max_length=25)
    email = models.EmailField(max_length=255)
    latitude = models.FloatField(max_length=8)
    longitude = models.FloatField(max_length=8)
    
    def __unicode__(self):
        return self.name
 
class Club(models.Model):
    name = models.CharField(max_length=255)
    pub = models.ForeignKey(Pub)
    
    def __unicode__(self):
        return self.name
    
class Player(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    moyenne = models.IntegerField(max_length=3)
    club = models.ForeignKey(Club)
    address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=6)
    city = models.CharField(max_length=255)
    phone = models.CharField(max_length=25)
    email = models.EmailField(max_length=255)
    
    def fullname(self):
        return self.__unicode__()
    
    def __unicode__(self):
        return self.firstname + " " + self.lastname

class AgendaItem(models.Model):
    date = models.DateField()
    pub = models.ForeignKey(Pub)
    home_club = models.ForeignKey(Club, related_name="home_agenda_items")
    away_club = models.ForeignKey(Club, related_name="away_agenda_items")
    
    def __unicode__(self):
        return self.date.strftime("%Y-%m-%d") + " @" + self.pub.__unicode__()
    
class Match(models.Model):
    home_player = models.ForeignKey(Player, related_name="home_match")
    home_player_moyenne = models.IntegerField(max_length=3)
    away_player = models.ForeignKey(Player, related_name="away_match")
    away_player_moyenne = models.IntegerField(max_length=3)
    date = models.DateField()
    arbiter = models.ForeignKey(Player, related_name="arbiter_at_match")
    writer = models.ForeignKey(Player, related_name="writer_at_match")
    agenda_item = models.ForeignKey(AgendaItem)
    
    def __unicode__(self):
        return self.date.strftime("%Y-%m-%d") + ": " + self.home_player.__unicode__() + " vs. " + self.away_player.__unicode__()
    
class MatchTurn(models.Model):
    match = models.ForeignKey(Match)
    player = models.ForeignKey(Player)
    turn = models.IntegerField(max_length=2)
    score = models.IntegerField(max_length=2)
    
    def __unicode__(self):
        return self.match + " - " + self.player.__unicode__() + " turn: " + self.turn
    