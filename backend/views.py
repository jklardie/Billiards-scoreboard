from django.core import serializers
from django.http import HttpResponse

from jongGeleerd.backend.models import Pub, Club, Player, Match, MatchTurn, AgendaItem
from backend.objects import Moyenne
from django.contrib.comments.models import Comment
from django.contrib.contenttypes.models import ContentType

def pub(request):
    return HttpResponse(serializers.serialize("json", Pub.objects.all(), indent=4))

def pub_details(request, id):
    pub = Pub.objects.filter(id=id)
    content_type = ContentType.objects.get(name='pub')
    
    all_objects = list(pub) + list(Comment.objects.filter(content_type=content_type, object_pk=id))
    return HttpResponse(serializers.serialize("json", all_objects, indent=4))


def club(request):
    return HttpResponse(serializers.serialize("json", Club.objects.all(), indent=4))

def club_details(request, id):
    club = Club.objects.filter(id=id)
    content_type = ContentType.objects.get(name='club')
    
    all_objects = list(club) + list(Comment.objects.filter(content_type=content_type, object_pk=id))
    return HttpResponse(serializers.serialize("json", all_objects, indent=4, relations=('pub')))

def club_players(request, club_id):
    all_objects = list(Club.objects.filter(id=club_id)) + list(Player.objects.filter(club=club_id))
    return HttpResponse(serializers.serialize("json", all_objects, indent=4, relations={'pub':{}, 'user':{'fields':('first_name', 'last_name', 'email') }}))


def player(request):
    return HttpResponse(serializers.serialize("json", Player.objects.all(), indent=4, relations={'user':{'fields':('first_name', 'last_name', 'email') }} ))

def player_details(request, id):
    player = Player.objects.filter(id=id)
    content_type = ContentType.objects.get(name='player')
    
    all_objects = list(player) + list(Comment.objects.filter(content_type=content_type, object_pk=id))
    
    return HttpResponse(serializers.serialize("json", all_objects, indent=4, relations={'club':{}, 'user':{'fields':('first_name', 'last_name', 'email') }}))

def player_moyenne(request, id):
    player = Player.objects.get(id=id)
    match_turns = MatchTurn.objects.filter(player=id)
    total_score = 0
    for turn in match_turns:
        total_score += turn.score
    
    moyenne = total_score / len(match_turns) 
    m = Moyenne(moyenne)
    return HttpResponse(serializers.serialize("json", (m,m), indent=4))


def match(request):
    return HttpResponse(serializers.serialize("json", Match.objects.all(), indent=4))

def match_details(request, id):
    match = Match.objects.filter(id=id)
    content_type = ContentType.objects.get(name='match')
    
    all_objects = list(match) + list(MatchTurn.objects.filter(match=id)) + list(Comment.objects.filter(content_type=content_type, object_pk=id))
    return HttpResponse(serializers.serialize("json", all_objects, indent=4, relations=('home_player', 'away_player', 'arbiter', 'writer') ) )


def agenda(request):
    return HttpResponse(serializers.serialize("json", AgendaItem.objects.all(), indent=4 ))

def agenda_details(request, id):
    agenda = AgendaItem.objects.filter(id=id)
    content_type = ContentType.objects.get(name='agenda item')
    
    all_objects = list(agenda) + list(Comment.objects.filter(content_type=content_type, object_pk=id))
    return HttpResponse(serializers.serialize("json", all_objects, indent=4, relations=('pub', 'home_club', 'away_club')))
