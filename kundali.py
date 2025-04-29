from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos

def get_kundali_table(date, time, latitude, longitude):
    pos = GeoPos(latitude, longitude)
    chart = Chart(Datetime(date, time, '+05:30'), pos)

    planets = ['SUN', 'MOON', 'MERCURY', 'VENUS', 'MARS', 'JUPITER', 'SATURN', 'RAHU', 'KETU', 'ASC']
    result = []

    for body in planets:
        obj = chart.get(body)
        result.append({
            "Planet": body.title(),
            "Sign": obj.sign,
            "Degree": round(obj.lon, 2)
        })

    return result
