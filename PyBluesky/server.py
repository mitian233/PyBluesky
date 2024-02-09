import requests
import json

# BASE_URL
BASE_URL = "https://bsky.social/xrpc/"

class Server:
    def createSession(identifier, password):
        url = BASE_URL + "com.atproto.server.createSession"
        payload = {
            "identifier": identifier,
            "password": password
        }
        content_type = "application/json"
        req = requests.post(url, data=json.dumps(payload), headers={"Content-Type": content_type})
        content = req.content
        json_content = json.loads(content)
        return json_content

    def getProfile(handle, accessJwt):
        url = BASE_URL + "com.atproto.server.getProfile"
        payload = {
            "handle": handle
        }
        content_type = "application/json"
        headers = {"Content-Type": content_type, "Authorization": "Bearer " + accessJwt}
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