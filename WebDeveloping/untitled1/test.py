import requests

requests.post(
        "https://api.mailgun.net/v3/sandbox93a99ddd61064e9b9655832322ef13b6.mailgun.org/messages",
        auth=("api", "key-060550c6-dd98ad20 "),
        data={"from": "Mailgun Sandbox <postmaster@sandbox93a99ddd61064e9b9655832322ef13b6.mailgun.org>",
              "to": ["obsteter.jana@gmail.com"],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomeness!"})