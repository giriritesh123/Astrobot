import requests

def get_astrology_report(sign):
    url = "https://best-daily-astrology-and-horoscope-api.p.rapidapi.com/api/Detailed-Horoscope/"

    querystring = {"zodiacSign": sign.lower()}  # e.g., 'leo'

    headers = {
        "x-rapidapi-host": "best-daily-astrology-and-horoscope-api.p.rapidapi.com",
        "x-rapidapi-key": "b18a9b3721msh531816298cc20a1p17b496jsn143ef513e88d"  # 🔐 your API key
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "API call failed"}
