from django.conf import settings
import urllib
import urllib2
import json


class HockeyStreamsAPIBase:
    token = settings.HOCKEYSTREAMS_GAMES_TOKEN
    key = None
    base_url = None

    def __init__(self):
        self.token = settings.HOCKEYSTREAMS_GAMES_TOKEN
        self.base_url = settings.HOCKEYSTREAMS_API_URL
        self.key = None
        self.url = ""

    def login(self):
        data = {
            'username': settings.HOCKEYSTREAMS_USERNAME,
            'password': settings.HOCKEYSTREAMS_PASSWORD,
            'key': settings.HOCKEYSTREAMS_GAMES_TOKEN
        }
        data = urllib.urlencode(data)
        self.url = "login"
        success, response = self.get_response(data=data, login_required=False)
        if not success:
            print "There was an error. %s" % response
        else:
            self.key = response['token']

    def get_response(self, data=None, login_required=True):
        """
        Gets the response using self.url and returns parsed json if applicable
        :param data: Post parameters, must be urlencoded
        :param login_required:  If login is required to hockey streams to execute the command
        :return:  A tuple True/False, Response   True/False based on if the command was successful.
        """
        if not self.token and login_required:
            self.login()
        try:
            if data:
                rows = json.loads(urllib2.urlopen(self.base_url + self.url, data).read())
            else:
                rows = json.loads(urllib2.urlopen(self.base_url + self.url).read())
            return True, rows
        except urllib2.HTTPError, error:
            if error.code == 406:
                return False, "ERROR: Invalid method, (Usually GET instead of POST)"
            elif error.code == 400:
                return False, "ERROR: %s." % (error.read())
            elif error.code == 204:
                return False, "ERROR: Empty response detected."
            else:
                return False, "ERROR: Unkown code: %s" % error.code
        except:
            return False, "Unkown Error" #Happens if the response is blank for some reason.
