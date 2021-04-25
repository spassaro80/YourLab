from django.contrib import admin
from core.models import Match, Stats, Event

# Register your models here.

class MatchAdmin(admin.ModelAdmin):
    model = Match

class StatsAdmin(admin.ModelAdmin):
    model = Stats

class EventAdmin(admin.ModelAdmin):
    model = Event

admin.site.register(Match)
admin.site.register(Stats)
admin.site.register(Event)
