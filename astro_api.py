import requests

def get_astrology_report(sign):
    url = "https://best-daily-astrology-and-horoscope-api.p.rapidapi.com/api/Detailed-Horoscope/"

    querystring = {"zodiacSign": sign}

    headers = {
        "x-rapidapi-host": "best-daily-astrology-and-horoscope-api.p.rapidapi.com",
        "x-rapidapi-key": "b18a9b3721msh531816298cc20a1p17b496jsn143ef513e88d"  # 🔐 Your key
    }

    response = requests.get(url, headers=headers, params=querystring)

    try:
        return response.json()
    except:
        return {"error": "Failed to decode JSON"}

