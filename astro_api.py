import requests

def get_astrology_report(sign):
    params = (('sign', sign.lower()), ('day', 'today'))
    response = requests.post('https://aztro.sameerkumar.website/', params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "API call failed"}
