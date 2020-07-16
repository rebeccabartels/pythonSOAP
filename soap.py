import requests
import json

def auth(clientId: str,
         clientSecret: str
    ) -> requests.Response:
   
    end_point = "https://??????/v2" + "/requestToken"
    headers = {'Content-type': 'application/json'}
    payload = {
        "clientId": clientId,
        "clientSecret": clientSecret,
        "accessType": "offline"
    }
         
    req = requests.post(
        end_point,
        headers=headers,
        data=json.dumps(payload)
    )
    print(req)
   

    return req