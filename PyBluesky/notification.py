import requests, json
from pybluesky.server import BASE_URL

class Notification(object):
    def __init__(self, sessionJson):
        self.handle = sessionJson["handle"]
        self.accessJwt = sessionJson["accessJwt"]
        self.refreshJwt = sessionJson["refreshJwt"]
        self.httpHeaders = {"Content-Type": "application/json", "Authorization": "Bearer " + self.accessJwt}

    def listNotifications(self, limit = 30):
        url = BASE_URL + "app.bsky.notification.listNotifications" + "?limit=" + str(limit)
        req = requests.get(url,headers=self.httpHeaders)
        json_content = json.loads(req.content)
        return json_content["notifications"]

