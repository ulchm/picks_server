from django.contrib import admin
from .models import Season, Team, Game, League
from hockeystreams_api.games import HockeyStreamsGames
import datetime
import pytz


def import_games_hockeystreams(modeladmin, request, queryset):
    hsg=HockeyStreamsGames()
    for item in queryset:
        today = item.start_date
        end_date = item.end_date
        tz = pytz.timezone('America/Toronto')
        while True:
            for g in hsg.get_scores(date=today):
                if not g['shortHomeTeam'] or not g['shortAwayTeam']: #Skip blank days.
                    continue
                away_team, created = Team.objects.get_or_create(short_name=g['shortAwayTeam'], name=g['awayTeamName'])
                home_team, created = Team.objects.get_or_create(short_name=g['shortHomeTeam'], name=g['homeTeamName'])
                if "Final" not in g['period']:
                    try:
                        if int(g['period'].split(':')[0] != 12):
                            starts_at = datetime.datetime.combine(today, datetime.time(int(g['period'].split(':')[0]) + 12,
                                                              int(g['period'].split(':')[1].split(' ')[0])))
                        else:
                            starts_at = datetime.datetime.combine(today, datetime.time(int(g['period'].split(':')[0]),
                                                                                      int(g['period'].split(':')[1].split(' ')[0])))
                    except ValueError, error:
                        print "Could not parse start time from: %s: %s" % (g['period'], error )
                        starts_at = datetime.datetime.combine(today, datetime.time(int(g['period'].split(':')[0]),
                                                                                   int(g['period'].split(':')[1].split(' ')[0])))
                else:
                    starts_at = datetime.datetime.combine(today, datetime.time(19, 00))
                starts_at = tz.localize(starts_at)
                game, created = Game.objects.get_or_create(
                    season=item,
                    home_team = home_team,
                    away_team = away_team,
                    starts_at = starts_at,
                )
            today = today + datetime.timedelta(days=1)
            if today > end_date:
                break
import_games_hockeystreams.short_description = "Import games for seasons from hockeystreams.com"


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'end_date', 'league']
    actions=[import_games_hockeystreams, ]


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['city', 'name', 'short_name']


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['season', 'away_team', 'home_team', 'away_score', 'home_score', 'is_playing', 'starts_at', 'period',
                    'is_final', 'was_overtime', 'was_shootout', 'winning_team']
    list_filter = [ 'is_final', 'season', 'is_playing', 'winning_team', 'losing_team',]

@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_name']