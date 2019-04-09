
def weathers1(sity):

    import pyowm

    owm = pyowm.OWM("b73b130c7e534d7ba0df924a43a92ba7")
    city = sity
    weather = owm.weather_at_place(city)
    w = weather.get_weather()
    temperature = w.get_temperature("celsius")["temp"]
    wind = w.get_wind()["speed"]
    hum = w.get_humidity()
    desc = w.get_detailed_status()
    return ( "Сейчас в городе " + str(city) +", температура - " \
     + str(temperature) + "°C, влажность - " + str(hum) + "%, скорость ветра - " \
     + str(wind) + "м/с.")


# res = weathers("Moscow")
#
# print(res)