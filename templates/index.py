# Copy & run this in your Python terminal.
import json
import requests
url = "https://api2.juvlon.com/v4/httpSendMail"
data = {"ApiKey":"INSERT_YOUR_JUVLON_ACCOUNT_API_KEY",
        "requests":[{"subject":"Hello",
                        "from":"support@juvlon.com",
                        "body":"This is an API test from Juvlon",
                          "to":"sales@nichelive.com"}]}
data_json = json.dumps(data)
r = requests.post(url, data=data_json)

print(r)