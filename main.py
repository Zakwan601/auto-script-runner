import requests

url = "https://www.playmartbd.com/"

try:
    response = requests.get(url)
    print("Pinged site! Status code:", response.status_code)
except Exception as e:
    print("Error:", e)
