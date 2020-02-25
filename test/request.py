import requests
import json


if __name__ == "__main__":
    url = "http://localhost:5000/search"
    d = {'data': '债券'}
    r = requests.post(url, data=d)
    print (r.text)