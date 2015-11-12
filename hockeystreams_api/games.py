from base import HockeyStreamsAPIBase
from django.conf import settings
from django.utils import timezone


class HockeyStreamsGames(HockeyStreamsAPIBase):

    def get_scores(self, date=timezone.now().date(), event="nhl"):
        self.url = "Scores?event=%s" % event
        if date:
            date = date.strftime("%m/%d/%Y")
            self.url += "&date=%s" % date
        self.url += "&key=%s" % (settings.HOCKEYSTREAMS_SCORES_TOKEN, )
        success, response = self.get_response(login_required=False)
        if not success:
            print "Warning: Likely no games on day %s" % date
            return []
        else:
            return response['scores']

    def get_teams(self, league="NHL"):
        if not self.key:
            self.login()
        self.url = "ListTeams?league=%s&token=%s" % (league, self.key)
        success, response = self.get_response(login_required=True)
        if success:
            return response['teams']
        else:
            print "ERROR: %s" % response