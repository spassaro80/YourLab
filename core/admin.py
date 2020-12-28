from django.contrib import admin
from core.models import Match, Stats

# Register your models here.

class MatchAdmin(admin.ModelAdmin):
    model = Match

class StatsAdmin(admin.ModelAdmin):
    model = Stats

admin.site.register(Match)
admin.site.register(Stats)
