import requests
import json
headers = {"Content-Type":"application/json",
           "Authorization":"key=AAAA9UgtesU:APA91bGBkep8RACVwZO00TAu5SIpgr287AmsgKhVO35JVR42eQiecDbNoq0k-co7ZoY5B0VGwuUKogjglg4tXdCcSoPDBcczLfFr0OjiBX8ICC5SxXz9lB4BIGpeNscSS-JFxPfo3VdH"
    }

url = "https://fcm.googleapis.com/fcm/send"

notification = {
  'title': 'Portugal vs. Denmark',
  'body': 'Portugal won the match'
}

data = {
        "notification":notification,
        "to":"eVl9J_HhYg4:APA91bFqB0fkEPMcwYMxoWDp_NwNNlElSJxn7_8u-PN_m3YuXHZ_QNVa0IJH5wBqSy5QXEbYpwfBF8GgJ8x3cJs-QimUgLNzocCeC3N_DxyXz3wX3Hi3eJuDYh-gFiFHTjSEg1RU_IGZ"
    }

print(data)
response = requests.post(url, data=json.dumps(data), headers=headers)

print(response.text)
