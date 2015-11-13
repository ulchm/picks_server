from django.db import models
from django.contrib.auth.models import User
from schedule.models import Game, Team, Season
from django.utils import timezone

POOL_TYPE_CHOICES = (
    (0, 'Public'),
    (100, 'Private'),
)

PICK_LOCKING_CHOICES = (
    (1, 'Daily at set time'),
    (2, 'Weekly at a set time'),
    (3, 'Minutes before the game starts'),
)

GAMES_TO_INCLUDE_CHOICES = (
    (1, 'All Games'),
    (2, 'DOTW to DOTW (e.g. Thurs to Sun'),
    (3, 'Only date to date'),
)

SCORING_METHOD_CHOICES = (
    (1, 'Traditional - 2 for win, 1 for OT loss, 0 for reg loss'),
    (2, 'Modified - 3 for reg win, 2 for OT win, 1 for SO win, 0 for loss.'),
    (3, 'Precision - 3 for SO win, 2 for OT win, 1 for reg win, 0 for loss.'),
)


class Pool(models.Model):
    season = models.ForeignKey(Season, related_name="pools")
    created_by = models.ForeignKey(User, related_name="pools_created")
    created_at = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=255)
    type = models.IntegerField(choices=POOL_TYPE_CHOICES)
    password = models.CharField(max_length=255, blank=True, null=True)
    registration_opens_at = models.DateTimeField(default=timezone.now)
    pick_locking_type = models.IntegerField(choices=PICK_LOCKING_CHOICES)
    games_to_include = models.IntegerField(choices=GAMES_TO_INCLUDE_CHOICES)
    scoring_method = models.IntegerField(choices=SCORING_METHOD_CHOICES)
    allow_forgot_picks_notifications = models.BooleanField(default=True)
    show_others_picks = models.BooleanField(default=True)
    allow_manual_lock = models.BooleanField(default=True)
    players = models.ManyToManyField(User, related_name="pools_joined", blank=True, null=True)

    def __unicode__(self):
        return self.name


class Pick(models.Model):
    user = models.ForeignKey(User, related_name="picks")
    pool = models.ForeignKey('Pool', related_name="picks")
    game = models.ForeignKey(Game, related_name="picks")
    pick = models.ForeignKey(Team, related_name="picks")
    updated_at = models.DateTimeField(auto_now=True)
    is_locked = models.BooleanField(default=False)

    def __unicode__(self):
        return "Pick #%s" % self.pk
