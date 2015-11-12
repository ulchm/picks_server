from django.core.management import BaseCommand
from schedule.models import Game, Team
from datetime import timedelta
from hockeystreams_api.games import HockeyStreamsGames
from django.utils import timezone


class Command(BaseCommand):
    help = 'Sets the scores / winners / overtimes for games that occurred on the previous day.'

    def handle(self, *args, **options):
        today = Game.objects.filter(starts_at__lte=timezone.now(), is_final=False).order_by('starts_at').first().starts_at.date()
        end_date = Game.objects.filter(starts_at__lte=timezone.now(), is_final=False).order_by('-starts_at').first().starts_at.date()

        while True:
            for score in HockeyStreamsGames().get_scores(date=today):
                #Get the game, update the scores no matter what
                home_team = Team.objects.get(short_name=score['shortHomeTeam'])
                away_team = Team.objects.get(short_name=score['shortAwayTeam'])
                game = Game.objects.get(home_team = home_team, away_team = away_team,
                                        starts_at__lte=today+timedelta(days=1), starts_at__gte=today, is_final=False)
                game.home_score = score['homeScore']
                game.away_score = score['awayScore']

                if 'SO' in score['period'].upper():
                    game.was_shootout = True
                    game.was_overtime = True
                if 'OT' in score['period'].upper():
                    game.was_overtime = True
                if 'FINAL' in score['period'].upper():
                    game.is_final = True
                    game.period = None
                    if game.home_score > game.away_score:
                        game.winning_team = game.home_team
                        game.losing_team = game.away_team
                    if game.away_score > game.home_score:
                        game.winning_team = game.away_team
                        game.losing_Team = game.home_team
                else:
                    game.period = score['period']
                game.save()
            today = today + timedelta(days=1)
            if today >= end_date:
                break