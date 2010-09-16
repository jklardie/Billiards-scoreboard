from jongGeleerd.backend.models import Pub, Club, Player, AgendaItem, Match, MatchTurn
from django.contrib import admin

class PubAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ['name', 'address']
        
    fieldsets = [
        (None,                  {'fields': ['name'] }),
        ('Contact information', {'fields': ['phone', 'email'] }),
        ('Address',             {'fields': ['address', 'postal_code', 'city'] }),
        ('Location',            {'fields': ['latitude', 'longitude'] })
    ]

class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'pub')
    search_fields = ['name', 'pub']
    
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'club', 'moyenne')
    search_fields = ['fullname', 'club']
        
    fieldsets = [
        ('Person',                  {'fields': ['firstname', 'lastname'] }),
        ('Billiard information',    {'fields': ['club', 'moyenne'] }),
        ('Contact information',     {'fields': ['phone', 'email'] }),
        ('Address',                 {'fields': ['address', 'postal_code', 'city'] })
    ]
    
class AgendaItemAdmin(admin.ModelAdmin):
    list_display = ('date', 'pub')
    search_fields = ['date', 'pub']
        
    fieldsets = [
        (None,          {'fields': ['date'] }),
        ('Location',    {'fields': ['pub'] }),
        ('Clubs',       {'fields': ['home_club', 'away_club'] })
    ]

class MatchTurnInline(admin.TabularInline):
    model = MatchTurn
    extra = 1
    
class MatchAdmin(admin.ModelAdmin):
    inlines = [MatchTurnInline]
    list_display = ('date', 'home_player', 'away_player')
    search_fields = ['date', 'home_player', 'away_player']
        
    fieldsets = [
        ('Players',                 {'fields': ['home_player', 'home_player_moyenne', 
                                                'away_player', 'away_player_moyenne'] }),
        ('Date and location',       {'fields': ['date', 'pub'] }),
        ('Competition match info',  {'fields': ['arbiter', 'writer', 'agenda_item'] })
    ]
    

admin.site.register(Pub, PubAdmin)
admin.site.register(Club, ClubAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(AgendaItem, AgendaItemAdmin)
admin.site.register(Match, MatchAdmin)