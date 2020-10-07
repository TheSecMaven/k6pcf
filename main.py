import requests
import os
from flask import Flask, Blueprint
import requests
app = Flask(__name__)

url = "https://service.service.com"

payload = "{\n    \"payload\": {\n        \"key\": [\"payload\"]\n    },\n    \"fileName\": \"test\",\n    \"referenceBranch\": \"master\",\n    \"targetBranch\": \"master\"\n}"
headers = {
  'token': '4e03bc83-bed2-436c-a793-affdda7bf7c4',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data = payload,verify=False)

print(response.text.encode('utf8'))


def main():
    port = int(os.getenv('PORT', '5000'))
    app.run(host='0.0.0.0', port=port)


if __name__ == "__main__":
    main()
