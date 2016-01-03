from django.db import models


class League(models.Model):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=10)
    is_active=models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


class Season(models.Model):
    name = models.CharField(max_length=255, help_text="The name of the season.")
    start_date = models.DateField(help_text="The first day of the season.")
    end_date = models.DateField(help_text="The last day of the season")
    league = models.ForeignKey('League', related_name="seasons")
    is_active=models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=255, help_text="The name of the team, without the city")
    short_name = models.CharField(max_length=3, help_text="The short name / code for the team.  3 Letters.")
    city = models.CharField(max_length=255, blank=True, null=True, help_text="The city the team is from")
    logo = models.FileField(upload_to="team_logos", blank=True, null=True, help_text="SVG Vector Image logo")
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        if self.city:
            return "%s %s" % (self.city, self.name)
        return "%s: %s" % (self.short_name, self.name)

    def get_active_away_record(self):
        #TODO: Look up current leagues / seasons and return active win, loss and ties as a dictionary
        return {'wins': 0,
                'losses': 0,
                'overtime_losses': 0}


    def get_active_home_record(self):
        #TODO: Look up current leagues / seasons and return active win, loss and ties as a dictionary
        return {'wins': 0,
                'losses': 0,
                'overtime_losses': 0}


class Game(models.Model):
    season = models.ForeignKey('Season', related_name="games")
    home_team = models.ForeignKey('Team', related_name="home_games")
    away_team = models.ForeignKey('Team', related_name="away_games")
    starts_at = models.DateTimeField()
    is_playing = models.BooleanField(default=False)
    home_score = models.IntegerField(blank=True, null=True)
    away_score = models.IntegerField(blank=True, null=True)
    period = models.CharField(max_length=255, blank=True, null=True)
    is_final = models.BooleanField(default=False)
    was_shootout = models.BooleanField(default=False)
    was_overtime = models.BooleanField(default=False)
    winning_team = models.ForeignKey('Team', related_name="games_won", blank=True, null=True)
    losing_team = models.ForeignKey('Team', related_name="games_lost", blank=True, null=True)

    def __unicode__(self):
        return "%s @ %s - %s" % (self.away_team, self.home_team, self.starts_at)

    def get_season_team_history(self):
        #TODO: Look up games in active system and history between these teams, building list of home / away wins and losses
        return {
            "home_wins": 0,
            "away_wins": 0,
            "home_losses": 0,
            "away_losses": 0
        }

    def get_all_team_history(self):
        #TODO: Look up all games in system and return how many games the home team and away team have won / lost
        return {
            "home_wins": 0,
            "away_wins": 0,
            "home_losses": 0,
            "away_losses": 0
        }
