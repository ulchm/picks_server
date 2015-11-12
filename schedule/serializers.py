from schedule.models import Team, Game, Season, League
from rest_framework import serializers


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('pk', 'season', 'home_team', 'away_team', 'starts_at', 'home_score', 'away_score', 'was_overtime', 'was_shootout', 'is_final')


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('pk', 'city', 'name', 'short_name', 'small_logo', 'large_logo')


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ('pk', 'name', 'start_date', 'end_date', 'league')


class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = ('pk', 'name', 'short_name')

