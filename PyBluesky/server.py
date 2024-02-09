import requests
import json

# BASE_URL
BASE_URL = "https://bsky.social/xrpc/"
content_type = "application/json"

class Server:
    def createSession(self, identifier, password, base_url = BASE_URL):
        url = BASE_URL + "com.atproto.server.createSession"
        payload = {
            "identifier": identifier,
            "password": password
        }
        content_type = "application/json"
        req = requests.post(url, data=json.dumps(payload), headers={"Content-Type": content_type})
        content = req.content
        json_content = json.loads(content)
        self.accessJwt = json_content["accessJwt"]
        self.refreshJwt = json_content["refreshJwt"]
        return json_content

    def getSession(self):
        url = BASE_URL + "com.atproto.server.getSession"
        req = requests.get(url, headers={"Content-Type": content_type, "Authorization": "Bearer " + self.accessJwt})

    def getProfile(self, handle):
        url = BASE_URL + "com.atproto.server.getProfile"
        payload = {
            "handle": handle
        }
        headers = {"Content-Type": content_type, "Authorization": "Bearer " + self.accessJwt}
        req = requests.post(url, data=json.dumps(payload), headers=headers)
        content = req.content
        json_content = json.loads(content)
        return json_content

def formatUrl(BASE_URL):
    if BASE_URL[-1] != "/":
        BASE_URL += "/"
    if not BASE_URL[:8] == "https://" or BASE_URL[:7] == "http://":
        BASE_URL = "https://" + BASE_URL
    return BASE_URL