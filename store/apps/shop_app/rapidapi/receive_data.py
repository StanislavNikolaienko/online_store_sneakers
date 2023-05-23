import requests
from config.settings import XRapidAPIKey, XRapidAPIHost, XRapidAPI_URL


def get_sneakers(limit: int = "100"):
    querystring = {"limit": limit}
    headers = {
        "X-RapidAPI-Key": f"{XRapidAPIKey}",
        "X-RapidAPI-Host": f"{XRapidAPIHost}",
    }
    response = requests.request(
        "GET", XRapidAPI_URL, headers=headers, params=querystring
    )
    return response.json()
