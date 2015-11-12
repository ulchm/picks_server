from pools.models import Pool, Pick
from rest_framework import serializers


class PoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pool
        fields = ('pk', 'created_by', 'created_at', 'name', 'type', 'registration_opens_at', 'pick_locking_type',
                  'scoring_method', 'games_to_include', 'allow_forgot_picks_notifications', 'show_others_picks',
                  'allow_manual_lock', 'players')


class PickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pick
        fields = ('pk', 'user', 'pool', 'game', 'pick', 'updated_at', 'is_locked')