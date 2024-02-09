import json
import requests
from pybluesky.server import BASE_URL

class Feed(object):
    def __init__(self, sessionJson):
        self.handle = sessionJson["handle"]
        self.accessJwt = sessionJson["accessJwt"]
        self.refreshJwt = sessionJson["refreshJwt"]
        self.httpHeaders = {"Content-Type": "application/json", "Authorization": "Bearer " + self.accessJwt}

    def getAuthorFeed(self, actor, limit = 18):
        url = BASE_URL + "app.bsky.feed.getAuthorFeed?actor=" + actor + "&limit=" + str(limit)
        req = requests.get(url, headers=self.httpHeaders)
        json_contents = json.loads(req.content)
        return json_contents["feed"]