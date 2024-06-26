# Developed by Franz Ayestaran - http://franz.ayestaran.co.uk

# You may use this code in your own projects and upon doing so, you the programmer are solely
# responsible for determining it's worthiness for any given application or task. Here clearly
# states that the code is for learning purposes only and is not guaranteed to conform to any
# programming style, standard, or be an adequate answer for any given problem.

import os
import requests
import json
import sqlite3

try:
    connection = sqlite3.connect("OpenWeather.db")
    print("connection.total_change: " + str(connection.total_changes))

    cursor = connection.cursor()

    SqlCreateTable = "CREATE TABLE IF NOT EXISTS tblForecast( fldId INTEGER UNIQUE, fldLatitude TEXT, fldLongitude TEXT, fldUnixTime INTEGER, fldIcon TEXT, fldDescription TEXT, fldTemp TEXT, fldUV TEXT, fldWindDirection TEXT, fldPressure TEXT, fldHumidity TEXT, fldDewPoint TEXT, fldCloudCover TEXT, fldVisibility TEXT, fldPrecipitationProbability TEXT, fldPrecipitationIntensity TEXT, fldJSON TEXT, PRIMARY KEY(fldId AUTOINCREMENT));"
    
    cursor.execute(SqlCreateTable)

    # ** Insert Sample Data Record
    #cursor.execute("INSERT INTO tblForecast(fldLatitude, fldLongitude, fldUnixTime, fldIcon, fldDescription, fldTemp, fldUV, fldWindDirection, fldPressure, fldHumidity, fldDewPoint, fldCloudCover, fldVisibility, fldPrecipitationProbability, fldPrecipitationIntensity, fldJSON) VALUES ('51.5099', '-0.1181', '1684321839', '10d', 'light rain', '11°C', '0.27', 'N-N-W Bearing: 340° Speed: 9.22 mph', '1021 hPa', '90%', '9°C', '100%', '6.21 miles', '0% pop/h', '0.17mm/h', '')")
    #connection.commit()

    # ** Reset auto-increment sequence number in sqlite
    #UPDATE SQLITE_SEQUENCE SET SEQ = '3' WHERE NAME = 'tblForecast' 

    #RecordId = 1
    #SqlRetrieveForecast = "SELECT fldLatitude, fldLongitude, fldUnixTime, fldIcon, fldDescription, fldTemp, fldUV, fldWindDirection, fldPressure, fldHumidity, fldDewPoint, fldCloudCover, fldVisibility, fldPrecipitationProbability, fldPrecipitationIntensity FROM tblForecast WHERE fldId = " + str(RecordId)
    #forecast = "\nForecast Record Id: " + str(RecordId) + " -> " + str(cursor.execute(SqlRetrieveForecast).fetchall())

    SqlRetrieveForecast = "SELECT fldId, fldLatitude, fldLongitude, fldUnixTime, fldIcon, fldDescription, fldTemp, fldUV, fldWindDirection, fldPressure, fldHumidity, fldDewPoint, fldCloudCover, fldVisibility, fldPrecipitationProbability, fldPrecipitationIntensity FROM tblForecast ORDER BY fldId DESC LIMIT 1"

    forecast = "\nForecast Latest Record -> " + str(cursor.execute(SqlRetrieveForecast).fetchall())
    print(forecast)

except sqlite3.Error as e:
        print("\n" + e + "\n")

api_key = "{API key}"

lat = "51.509865" #London, UK
lon = "-0.118092"

url = "https://api.openweathermap.org/data/3.0/onecall?lat=%s&lon=%s&appid=%s" % (lat, lon, api_key)

TempUnitType = 0
TimeOffset = 0.0
TempValue = 0.0
WindSpeed = 0.00
WindSpeedValue = 0.00
WindBearing = 0.0
Millibar = 0.0
Humidity = 0.0
DewPoint = 0.0
DewPointValue = 0.0
Ozone = 0.0
mmh = 0.0
CloudCover = 0.0
PrecipProbability = ""
PrecipProbabilityValue = 0.0
PrecipIntensity = 0.0
selectedUnixTime = 0.0
sunriseTime = 0.0
sunsetTime = 0.0
UVindex = 0.0
Visibility = 0.0
Icon = ""
Description = ""
TempValue = 0.00

useSampleData = True
sampleDataType = "rain"
lineFeed = "\n"

ForecastJSONsampleSunnyString = '{"lat":23.9001,"lon":10.3358,"timezone":"Africa/Algiers","timezone_offset":3600,"current":{"dt":1684497576,"sunrise":1684470889,"sunset":1684518940,"temp":308.68,"feels_like":306.05,"pressure":1008,"humidity":12,"dew_point":274.94,"uvi":11.35,"clouds":76,"visibility":10000,"wind_speed":7.42,"wind_deg":258,"wind_gust":11.72,"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}]},"hourly":[{"dt":1684494000,"temp":308.56,"feels_like":305.99,"pressure":1008,"humidity":13,"dew_point":275.97,"uvi":11.63,"clouds":76,"visibility":10000,"wind_speed":7.06,"wind_deg":268,"wind_gust":12.18,"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"pop":0},{"dt":1684497600,"temp":308.68,"feels_like":306.05,"pressure":1008,"humidity":12,"dew_point":274.94,"uvi":11.35,"clouds":76,"visibility":10000,"wind_speed":7.42,"wind_deg":258,"wind_gust":11.72,"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"pop":0},{"dt":1684501200,"temp":308.57,"feels_like":305.94,"pressure":1008,"humidity":12,"dew_point":274.86,"uvi":8.92,"clouds":81,"visibility":10000,"wind_speed":8.4,"wind_deg":251,"wind_gust":10.22,"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"pop":0},{"dt":1684504800,"temp":308.68,"feels_like":306.05,"pressure":1008,"humidity":12,"dew_point":274.94,"uvi":6.21,"clouds":80,"visibility":10000,"wind_speed":8.02,"wind_deg":246,"wind_gust":10.58,"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"pop":0},{"dt":1684508400,"temp":308.47,"feels_like":305.85,"pressure":1007,"humidity":12,"dew_point":274.78,"uvi":3.45,"clouds":85,"visibility":10000,"wind_speed":8.14,"wind_deg":241,"wind_gust":9.78,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"pop":0},{"dt":1684512000,"temp":308.38,"feels_like":305.77,"pressure":1006,"humidity":12,"dew_point":274.71,"uvi":1.37,"clouds":88,"visibility":10000,"wind_speed":8.07,"wind_deg":235,"wind_gust":9.86,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"pop":0},{"dt":1684515600,"temp":307.74,"feels_like":305.18,"pressure":1005,"humidity":12,"dew_point":274.58,"uvi":0.33,"clouds":90,"visibility":10000,"wind_speed":7.27,"wind_deg":234,"wind_gust":10.3,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"pop":0},{"dt":1684519200,"temp":304.51,"feels_like":302.44,"pressure":1006,"humidity":17,"dew_point":276.99,"uvi":0,"clouds":90,"visibility":10000,"wind_speed":4.85,"wind_deg":279,"wind_gust":9.06,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04n"}],"pop":0},{"dt":1684522800,"temp":302.73,"feels_like":301.12,"pressure":1007,"humidity":22,"dew_point":279.55,"uvi":0,"clouds":98,"visibility":10000,"wind_speed":2.99,"wind_deg":322,"wind_gust":5.37,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04n"}],"pop":0},{"dt":1684526400,"temp":300.67,"feels_like":299.91,"pressure":1010,"humidity":30,"dew_point":281.45,"uvi":0,"clouds":87,"visibility":10000,"wind_speed":10.1,"wind_deg":308,"wind_gust":12.51,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04n"}],"pop":0},{"dt":1684530000,"temp":298.61,"feels_like":298.13,"pressure":1010,"humidity":35,"dew_point":282.65,"uvi":0,"clouds":91,"visibility":10000,"wind_speed":3.15,"wind_deg":336,"wind_gust":5.46,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04n"}],"pop":0},{"dt":1684533600,"temp":299.99,"feels_like":299.47,"pressure":1010,"humidity":30,"dew_point":281.63,"uvi":0,"clouds":92,"visibility":10000,"wind_speed":2.31,"wind_deg":314,"wind_gust":3,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04n"}],"pop":0},{"dt":1684537200,"temp":300.51,"feels_like":299.68,"pressure":1009,"humidity":27,"dew_point":280.56,"uvi":0,"clouds":94,"visibility":10000,"wind_speed":2.4,"wind_deg":316,"wind_gust":2.9,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04n"}],"pop":0},{"dt":1684540800,"temp":300.33,"feels_like":299.53,"pressure":1008,"humidity":26,"dew_point":279.74,"uvi":0,"clouds":95,"visibility":10000,"wind_speed":3.41,"wind_deg":323,"wind_gust":3.86,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04n"}],"pop":0},{"dt":1684544400,"temp":299.87,"feels_like":299.22,"pressure":1007,"humidity":25,"dew_point":278.72,"uvi":0,"clouds":100,"visibility":10000,"wind_speed":4.1,"wind_deg":323,"wind_gust":7.66,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04n"}],"pop":0},{"dt":1684548000,"temp":299.46,"feels_like":299.46,"pressure":1007,"humidity":23,"dew_point":277.33,"uvi":0,"clouds":100,"visibility":10000,"wind_speed":4.39,"wind_deg":306,"wind_gust":7.6,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04n"}],"pop":0},{"dt":1684551600,"temp":298.77,"feels_like":297.99,"pressure":1007,"humidity":23,"dew_point":276.52,"uvi":0,"clouds":100,"visibility":10000,"wind_speed":4.06,"wind_deg":307,"wind_gust":7.08,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04n"}],"pop":0},{"dt":1684555200,"temp":297.93,"feels_like":297.09,"pressure":1008,"humidity":24,"dew_point":276.1,"uvi":0,"clouds":100,"visibility":10000,"wind_speed":1.04,"wind_deg":330,"wind_gust":4.48,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04n"}],"pop":0},{"dt":1684558800,"temp":297.36,"feels_like":296.52,"pressure":1009,"humidity":26,"dew_point":276.83,"uvi":0,"clouds":100,"visibility":10000,"wind_speed":2.33,"wind_deg":67,"wind_gust":2.81,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"pop":0},{"dt":1684562400,"temp":298.71,"feels_like":297.97,"pressure":1010,"humidity":25,"dew_point":278.01,"uvi":0.63,"clouds":100,"visibility":10000,"wind_speed":3.39,"wind_deg":41,"wind_gust":5.58,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"pop":0},{"dt":1684566000,"temp":300.45,"feels_like":299.4,"pressure":1010,"humidity":19,"dew_point":275.34,"uvi":2.01,"clouds":100,"visibility":10000,"wind_speed":6.03,"wind_deg":33,"wind_gust":5.31,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"pop":0},{"dt":1684569600,"temp":301.4,"feels_like":299.99,"pressure":1010,"humidity":16,"dew_point":274.09,"uvi":4.45,"clouds":96,"visibility":10000,"wind_speed":6.41,"wind_deg":32,"wind_gust":5.24,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"pop":0},{"dt":1684573200,"temp":302.28,"feels_like":300.61,"pressure":1010,"humidity":14,"dew_point":272.15,"uvi":7.36,"clouds":88,"visibility":10000,"wind_speed":5.79,"wind_deg":27,"wind_gust":4.27,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"pop":0},{"dt":1684576800,"temp":303.05,"feels_like":301.2,"pressure":1010,"humidity":12,"dew_point":270.82,"uvi":9.44,"clouds":69,"visibility":10000,"wind_speed":4.31,"wind_deg":30,"wind_gust":3.42,"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"pop":0},{"dt":1684580400,"temp":303.88,"feels_like":301.87,"pressure":1009,"humidity":11,"dew_point":270.27,"uvi":10.74,"clouds":57,"visibility":10000,"wind_speed":2.62,"wind_deg":41,"wind_gust":3.22,"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"pop":0},{"dt":1684584000,"temp":305.08,"feels_like":302.86,"pressure":1008,"humidity":10,"dew_point":270.14,"uvi":10.49,"clouds":49,"visibility":10000,"wind_speed":0.67,"wind_deg":344,"wind_gust":4.37,"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],"pop":0},{"dt":1684587600,"temp":306.42,"feels_like":303.98,"pressure":1007,"humidity":9,"dew_point":270.12,"uvi":9.4,"clouds":8,"visibility":10000,"wind_speed":2.53,"wind_deg":266,"wind_gust":5.87,"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"pop":0},{"dt":1684591200,"temp":306.92,"feels_like":304.41,"pressure":1007,"humidity":9,"dew_point":269.58,"uvi":6.56,"clouds":11,"visibility":10000,"wind_speed":5.11,"wind_deg":276,"wind_gust":7.59,"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02d"}],"pop":0},{"dt":1684594800,"temp":306.81,"feels_like":304.32,"pressure":1006,"humidity":8,"dew_point":268.28,"uvi":3.65,"clouds":26,"visibility":10000,"wind_speed":5.67,"wind_deg":283,"wind_gust":7.35,"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],"pop":0},{"dt":1684598400,"temp":306.23,"feels_like":303.86,"pressure":1006,"humidity":7,"dew_point":267.35,"uvi":1.41,"clouds":45,"visibility":10000,"wind_speed":6.15,"wind_deg":284,"wind_gust":7.26,"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],"pop":0},{"dt":1684602000,"temp":305.17,"feels_like":302.96,"pressure":1006,"humidity":8,"dew_point":266.69,"uvi":0.34,"clouds":56,"visibility":10000,"wind_speed":5.75,"wind_deg":292,"wind_gust":6.2,"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"pop":0},{"dt":1684605600,"temp":303.07,"feels_like":301.27,"pressure":1007,"humidity":8,"dew_point":266.35,"uvi":0,"clouds":58,"visibility":10000,"wind_speed":3.25,"wind_deg":297,"wind_gust":3.88,"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],"pop":0},{"dt":1684609200,"temp":301.73,"feels_like":300.2,"pressure":1007,"humidity":9,"dew_point":266.35,"uvi":0,"clouds":77,"visibility":10000,"wind_speed":2.2,"wind_deg":311,"wind_gust":2.58,"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],"pop":0},{"dt":1684612800,"temp":300.75,"feels_like":299.47,"pressure":1008,"humidity":11,"dew_point":268.09,"uvi":0,"clouds":67,"visibility":10000,"wind_speed":4.34,"wind_deg":17,"wind_gust":5.54,"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],"pop":0},{"dt":1684616400,"temp":298.71,"feels_like":297.77,"pressure":1010,"humidity":17,"dew_point":272.18,"uvi":0,"clouds":48,"visibility":10000,"wind_speed":7.56,"wind_deg":28,"wind_gust":11.92,"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03n"}],"pop":0},{"dt":1684620000,"temp":297.46,"feels_like":296.44,"pressure":1010,"humidity":19,"dew_point":273.17,"uvi":0,"clouds":36,"visibility":10000,"wind_speed":9.39,"wind_deg":21,"wind_gust":13.78,"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03n"}],"pop":0},{"dt":1684623600,"temp":296.27,"feels_like":295.19,"pressure":1010,"humidity":21,"dew_point":273.29,"uvi":0,"clouds":29,"visibility":10000,"wind_speed":9.51,"wind_deg":24,"wind_gust":13.83,"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03n"}],"pop":0},{"dt":1684627200,"temp":295.31,"feels_like":294.13,"pressure":1009,"humidity":21,"dew_point":272.46,"uvi":0,"clouds":24,"visibility":10000,"wind_speed":9.39,"wind_deg":26,"wind_gust":13.37,"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02n"}],"pop":0},{"dt":1684630800,"temp":294.31,"feels_like":293,"pressure":1009,"humidity":20,"dew_point":271.34,"uvi":0,"clouds":2,"visibility":10000,"wind_speed":9.24,"wind_deg":25,"wind_gust":13.48,"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"pop":0},{"dt":1684634400,"temp":293.58,"feels_like":292.2,"pressure":1009,"humidity":20,"dew_point":270.6,"uvi":0,"clouds":3,"visibility":10000,"wind_speed":9.63,"wind_deg":22,"wind_gust":13.98,"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"pop":0},{"dt":1684638000,"temp":292.8,"feels_like":291.37,"pressure":1010,"humidity":21,"dew_point":270.24,"uvi":0,"clouds":2,"visibility":10000,"wind_speed":9.46,"wind_deg":23,"wind_gust":14.01,"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"pop":0},{"dt":1684641600,"temp":292.16,"feels_like":290.66,"pressure":1010,"humidity":21,"dew_point":270.1,"uvi":0,"clouds":2,"visibility":10000,"wind_speed":9.25,"wind_deg":24,"wind_gust":13.89,"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"pop":0},{"dt":1684645200,"temp":291.74,"feels_like":290.23,"pressure":1011,"humidity":22,"dew_point":270.03,"uvi":0,"clouds":1,"visibility":10000,"wind_speed":8.83,"wind_deg":26,"wind_gust":13.38,"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"pop":0},{"dt":1684648800,"temp":292.92,"feels_like":291.47,"pressure":1012,"humidity":20,"dew_point":269.79,"uvi":0.63,"clouds":1,"visibility":10000,"wind_speed":9.54,"wind_deg":29,"wind_gust":12.37,"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"pop":0},{"dt":1684652400,"temp":294.67,"feels_like":293.32,"pressure":1012,"humidity":17,"dew_point":269.53,"uvi":2.15,"clouds":0,"visibility":10000,"wind_speed":10.34,"wind_deg":34,"wind_gust":11.18,"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"pop":0},{"dt":1684656000,"temp":296.66,"feels_like":295.48,"pressure":1012,"humidity":16,"dew_point":269.48,"uvi":4.74,"clouds":10,"visibility":10000,"wind_speed":9.91,"wind_deg":39,"wind_gust":9.86,"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"pop":0},{"dt":1684659600,"temp":298.52,"feels_like":297.48,"pressure":1012,"humidity":14,"dew_point":269.48,"uvi":7.84,"clouds":7,"visibility":10000,"wind_speed":8.98,"wind_deg":42,"wind_gust":8.4,"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"pop":0},{"dt":1684663200,"temp":300.24,"feels_like":299.13,"pressure":1011,"humidity":13,"dew_point":269.47,"uvi":10.63,"clouds":6,"visibility":10000,"wind_speed":7.12,"wind_deg":47,"wind_gust":5.94,"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"pop":0}],"daily":[{"dt":1684494000,"sunrise":1684470889,"sunset":1684518940,"moonrise":1684469580,"moonset":1684519140,"moon_phase":0,"temp":{"day":308.56,"min":298.61,"max":308.68,"night":299.99,"eve":307.74,"morn":299.45},"feels_like":{"day":305.99,"night":299.47,"eve":305.18,"morn":299.45},"pressure":1008,"humidity":13,"dew_point":275.97,"wind_speed":10.1,"wind_deg":308,"wind_gust":12.51,"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"clouds":76,"pop":0,"uvi":11.63},{"dt":1684580400,"sunrise":1684557266,"sunset":1684605370,"moonrise":1684558560,"moonset":1684609140,"moon_phase":0.03,"temp":{"day":303.88,"min":297.36,"max":306.92,"night":297.46,"eve":305.17,"morn":297.36},"feels_like":{"day":301.87,"night":296.44,"eve":302.96,"morn":296.52},"pressure":1009,"humidity":11,"dew_point":270.27,"wind_speed":9.39,"wind_deg":21,"wind_gust":13.78,"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"clouds":57,"pop":0,"uvi":10.74},{"dt":1684666800,"sunrise":1684643644,"sunset":1684691799,"moonrise":1684647720,"moonset":1684699020,"moon_phase":0.06,"temp":{"day":301.44,"min":291.74,"max":304.59,"night":298.32,"eve":304.09,"morn":291.74},"feels_like":{"day":299.98,"night":297.26,"eve":302.06,"morn":290.23},"pressure":1011,"humidity":12,"dew_point":269.49,"wind_speed":10.34,"wind_deg":34,"wind_gust":14.01,"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02d"}],"clouds":14,"pop":0,"uvi":12.09},{"dt":1684753200,"sunrise":1684730024,"sunset":1684778229,"moonrise":1684737240,"moonset":1684788720,"moon_phase":0.09,"temp":{"day":307.81,"min":294.06,"max":308.48,"night":302.55,"eve":305.68,"morn":294.73},"feels_like":{"day":305.21,"night":300.84,"eve":303.41,"morn":293.44},"pressure":1007,"humidity":11,"dew_point":273.65,"wind_speed":7.74,"wind_deg":268,"wind_gust":12.96,"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],"clouds":29,"pop":0,"uvi":11.13},{"dt":1684839600,"sunrise":1684816404,"sunset":1684864658,"moonrise":1684826820,"moonset":1684878060,"moon_phase":0.12,"temp":{"day":307.92,"min":299.16,"max":308.11,"night":300.57,"eve":302.78,"morn":299.38},"feels_like":{"day":305.31,"night":299.36,"eve":301.03,"morn":299.38},"pressure":1007,"humidity":4,"dew_point":258.98,"wind_speed":8.51,"wind_deg":304,"wind_gust":12.44,"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],"clouds":39,"pop":0,"uvi":11.76},{"dt":1684926000,"sunrise":1684902786,"sunset":1684951088,"moonrise":1684916580,"moonset":1684967160,"moon_phase":0.15,"temp":{"day":307.94,"min":296.76,"max":307.94,"night":299.85,"eve":304.02,"morn":299.08},"feels_like":{"day":305.3,"night":298.73,"eve":302.12,"morn":297.94},"pressure":1008,"humidity":5,"dew_point":262.73,"wind_speed":8.27,"wind_deg":309,"wind_gust":10.55,"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],"clouds":25,"pop":0,"uvi":12},{"dt":1685012400,"sunrise":1684989169,"sunset":1685037517,"moonrise":1685006280,"moonset":0,"moon_phase":0.18,"temp":{"day":305.62,"min":295.79,"max":306.37,"night":299.45,"eve":302.14,"morn":297.16},"feels_like":{"day":303.39,"night":299.45,"eve":300.53,"morn":295.9},"pressure":1010,"humidity":6,"dew_point":263.57,"wind_speed":6.69,"wind_deg":37,"wind_gust":9,"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"clouds":1,"pop":0,"uvi":12},{"dt":1685098800,"sunrise":1685075553,"sunset":1685123946,"moonrise":1685095920,"moonset":1685055900,"moon_phase":0.21,"temp":{"day":305.69,"min":294.78,"max":306.62,"night":298.95,"eve":302.6,"morn":296.37},"feels_like":{"day":303.37,"night":298.03,"eve":300.86,"morn":295.22},"pressure":1009,"humidity":9,"dew_point":269.65,"wind_speed":7.43,"wind_deg":73,"wind_gust":10.17,"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"clouds":0,"pop":0,"uvi":12}],"alerts":[{"sender_name":"Office National de la Météorologie","event":"VENT DE SABLE","start":1684508400,"end":1684530000,"description":"","tags":["Sand/Dust"]},{"sender_name":"Office National de la Météorologie","event":"VENT VIOLENT","start":1684508400,"end":1684530000,"description":"","tags":["Other dangers"]}]}'

ForecastJSONsampleRainString = '{"lat":0,"lon":0,"timezone":"Etc/GMT","timezone_offset":0,"current":{"dt":1684321839,"sunrise":1684302778,"sunset":1684346400,"temp":300.54,"feels_like":304.01,"pressure":1013,"humidity":82,"dew_point":297.19,"uvi":8.14,"clouds":100,"visibility":10000,"wind_speed":4.63,"wind_deg":147,"wind_gust":5.1,"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"rain":{"1h":0.94}},"hourly":[{"dt":1684321200,"temp":300.54,"feels_like":304.01,"pressure":1013,"humidity":82,"dew_point":297.19,"uvi":8.14,"clouds":100,"visibility":10000,"wind_speed":4.63,"wind_deg":147,"wind_gust":5.1,"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"pop":0.6,"rain":{"1h":0.94}},{"dt":1684324800,"temp":300.59,"feels_like":304.14,"pressure":1013,"humidity":82,"dew_point":297.24,"uvi":8.9,"clouds":100,"visibility":10000,"wind_speed":5.27,"wind_deg":140,"wind_gust":5.8,"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"pop":0.64,"rain":{"1h":0.38}},{"dt":1684328400,"temp":300.67,"feels_like":304.21,"pressure":1013,"humidity":81,"dew_point":297.12,"uvi":10.81,"clouds":100,"visibility":10000,"wind_speed":5.37,"wind_deg":145,"wind_gust":5.7,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"pop":0.24},{"dt":1684332000,"temp":300.8,"feels_like":304.52,"pressure":1012,"humidity":81,"dew_point":297.24,"uvi":8.19,"clouds":93,"visibility":10000,"wind_speed":5.46,"wind_deg":146,"wind_gust":5.72,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"pop":0.12},{"dt":1684335600,"temp":301.02,"feels_like":304.93,"pressure":1011,"humidity":80,"dew_point":297.25,"uvi":4.91,"clouds":94,"visibility":10000,"wind_speed":4.81,"wind_deg":150,"wind_gust":5.1,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"pop":0.08},{"dt":1684339200,"temp":301.15,"feels_like":305.25,"pressure":1010,"humidity":80,"dew_point":297.31,"uvi":2.01,"clouds":78,"visibility":10000,"wind_speed":4.72,"wind_deg":145,"wind_gust":5,"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"pop":0.04},{"dt":1684342800,"temp":301.11,"feels_like":305.3,"pressure":1011,"humidity":81,"dew_point":297.51,"uvi":0.49,"clouds":82,"visibility":10000,"wind_speed":4.88,"wind_deg":139,"wind_gust":5.22,"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"pop":0.04},{"dt":1684346400,"temp":301.1,"feels_like":305.28,"pressure":1011,"humidity":81,"dew_point":297.6,"uvi":0,"clouds":85,"visibility":10000,"wind_speed":5.46,"wind_deg":137,"wind_gust":5.71,"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"pop":0.24,"rain":{"1h":0.13}},{"dt":1684350000,"temp":301.06,"feels_like":305.33,"pressure":1012,"humidity":82,"dew_point":297.74,"uvi":0,"clouds":25,"visibility":10000,"wind_speed":5.52,"wind_deg":144,"wind_gust":5.81,"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03n"}],"pop":0.48},{"dt":1684353600,"temp":301.04,"feels_like":305.27,"pressure":1012,"humidity":82,"dew_point":297.61,"uvi":0,"clouds":63,"visibility":10000,"wind_speed":5.6,"wind_deg":146,"wind_gust":6.02,"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],"pop":0.48},{"dt":1684357200,"temp":300.91,"feels_like":304.94,"pressure":1012,"humidity":82,"dew_point":297.6,"uvi":0,"clouds":75,"visibility":10000,"wind_speed":6.15,"wind_deg":150,"wind_gust":6.32,"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],"pop":0.52},{"dt":1684360800,"temp":300.81,"feels_like":304.82,"pressure":1012,"humidity":83,"dew_point":297.7,"uvi":0,"clouds":81,"visibility":10000,"wind_speed":6.16,"wind_deg":153,"wind_gust":6.53,"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"pop":0.64,"rain":{"1h":0.13}},{"dt":1684364400,"temp":300.82,"feels_like":304.71,"pressure":1012,"humidity":82,"dew_point":297.51,"uvi":0,"clouds":85,"visibility":10000,"wind_speed":6.36,"wind_deg":156,"wind_gust":6.7,"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"pop":0.8,"rain":{"1h":0.13}},{"dt":1684368000,"temp":300.67,"feels_like":304.33,"pressure":1012,"humidity":82,"dew_point":297.38,"uvi":0,"clouds":88,"visibility":10000,"wind_speed":6.09,"wind_deg":152,"wind_gust":6.5,"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"pop":0.96,"rain":{"1h":0.25}},{"dt":1684371600,"temp":300.32,"feels_like":303.7,"pressure":1011,"humidity":84,"dew_point":297.42,"uvi":0,"clouds":100,"visibility":10000,"wind_speed":5.41,"wind_deg":145,"wind_gust":6.31,"weather":[{"id":501,"main":"Rain","description":"moderate rain","icon":"10n"}],"pop":1,"rain":{"1h":1.69}},{"dt":1684375200,"temp":300.36,"feels_like":303.8,"pressure":1010,"humidity":84,"dew_point":297.4,"uvi":0,"clouds":100,"visibility":10000,"wind_speed":5.67,"wind_deg":147,"wind_gust":6.41,"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"pop":1,"rain":{"1h":0.81}},{"dt":1684378800,"temp":300.77,"feels_like":304.45,"pressure":1010,"humidity":81,"dew_point":297.26,"uvi":0,"clouds":100,"visibility":10000,"wind_speed":5.51,"wind_deg":149,"wind_gust":6.01,"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"pop":1,"rain":{"1h":0.25}},{"dt":1684382400,"temp":300.8,"feels_like":304.52,"pressure":1010,"humidity":81,"dew_point":297.29,"uvi":0,"clouds":100,"visibility":10000,"wind_speed":5.28,"wind_deg":152,"wind_gust":5.8,"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"pop":1,"rain":{"1h":0.38}},{"dt":1684386000,"temp":300.7,"feels_like":304.41,"pressure":1011,"humidity":82,"dew_point":297.3,"uvi":0,"clouds":100,"visibility":10000,"wind_speed":5.61,"wind_deg":141,"wind_gust":6.2,"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"pop":1,"rain":{"1h":0.81}},{"dt":1684389600,"temp":300.62,"feels_like":304.21,"pressure":1012,"humidity":82,"dew_point":297.2,"uvi":0,"clouds":100,"visibility":3617,"wind_speed":6.17,"wind_deg":140,"wind_gust":6.8,"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"pop":1,"rain":{"1h":0.88}},{"dt":1684393200,"temp":300.61,"feels_like":304.06,"pressure":1013,"humidity":81,"dew_point":297.06,"uvi":0.5,"clouds":100,"visibility":10000,"wind_speed":6.45,"wind_deg":137,"wind_gust":7.3,"weather":[{"id":501,"main":"Rain","description":"moderate rain","icon":"10d"}],"pop":0.88,"rain":{"1h":1.88}},{"dt":1684396800,"temp":300.96,"feels_like":304.64,"pressure":1014,"humidity":79,"dew_point":296.97,"uvi":2.01,"clouds":100,"visibility":10000,"wind_speed":7,"wind_deg":136,"wind_gust":7.61,"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"pop":0.88,"rain":{"1h":0.25}},{"dt":1684400400,"temp":301,"feels_like":304.88,"pressure":1014,"humidity":80,"dew_point":297.2,"uvi":4.66,"clouds":100,"visibility":10000,"wind_speed":6.94,"wind_deg":137,"wind_gust":7.3,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"pop":0.88},{"dt":1684404000,"temp":300.9,"feels_like":304.77,"pressure":1014,"humidity":81,"dew_point":297.3,"uvi":5.3,"clouds":100,"visibility":10000,"wind_speed":6.55,"wind_deg":140,"wind_gust":7.11,"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"pop":0.92,"rain":{"1h":0.44}},{"dt":1684407600,"temp":301.16,"feels_like":305.27,"pressure":1013,"humidity":80,"dew_point":297.33,"uvi":6.99,"clouds":100,"visibility":10000,"wind_speed":6.77,"wind_deg":142,"wind_gust":7,"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"pop":0.88,"rain":{"1h":0.44}},{"dt":1684411200,"temp":301.05,"feels_like":305,"pressure":1013,"humidity":80,"dew_point":297.34,"uvi":7.64,"clouds":100,"visibility":10000,"wind_speed":7,"wind_deg":145,"wind_gust":7.2,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"pop":0.88},{"dt":1684414800,"temp":301.16,"feels_like":305.12,"pressure":1012,"humidity":79,"dew_point":297.26,"uvi":9.39,"clouds":99,"visibility":10000,"wind_speed":6.92,"wind_deg":148,"wind_gust":7.12,"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"pop":0.52,"rain":{"1h":0.19}},{"dt":1684418400,"temp":301.22,"feels_like":305.11,"pressure":1011,"humidity":78,"dew_point":297.06,"uvi":7.11,"clouds":100,"visibility":10000,"wind_speed":6.77,"wind_deg":148,"wind_gust":6.93,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"pop":0.48},{"dt":1684422000,"temp":301.15,"feels_like":304.8,"pressure":1011,"humidity":77,"dew_point":296.88,"uvi":4.27,"clouds":100,"visibility":10000,"wind_speed":6.31,"wind_deg":153,"wind_gust":6.33,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"pop":0.48},{"dt":1684425600,"temp":301.12,"feels_like":304.58,"pressure":1011,"humidity":76,"dew_point":296.68,"uvi":2.09,"clouds":100,"visibility":10000,"wind_speed":5.92,"wind_deg":157,"wind_gust":5.95,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"pop":0.44},{"dt":1684429200,"temp":301.12,"feels_like":304.73,"pressure":1011,"humidity":77,"dew_point":296.62,"uvi":0.51,"clouds":96,"visibility":10000,"wind_speed":5.81,"wind_deg":158,"wind_gust":5.9,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"pop":0.44},{"dt":1684432800,"temp":301.06,"feels_like":304.59,"pressure":1012,"humidity":77,"dew_point":296.67,"uvi":0,"clouds":88,"visibility":10000,"wind_speed":6.12,"wind_deg":160,"wind_gust":6.21,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"pop":0.44},{"dt":1684436400,"temp":301.06,"feels_like":304.73,"pressure":1012,"humidity":78,"dew_point":296.8,"uvi":0,"clouds":45,"visibility":10000,"wind_speed":6.31,"wind_deg":159,"wind_gust":6.33,"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03n"}],"pop":0},{"dt":1684440000,"temp":301,"feels_like":304.59,"pressure":1013,"humidity":78,"dew_point":296.8,"uvi":0,"clouds":44,"visibility":10000,"wind_speed":6.63,"wind_deg":163,"wind_gust":6.6,"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03n"}],"pop":0},{"dt":1684443600,"temp":300.91,"feels_like":304.38,"pressure":1013,"humidity":78,"dew_point":296.71,"uvi":0,"clouds":63,"visibility":10000,"wind_speed":6.83,"wind_deg":160,"wind_gust":6.7,"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],"pop":0},{"dt":1684447200,"temp":300.91,"feels_like":304.38,"pressure":1013,"humidity":78,"dew_point":296.71,"uvi":0,"clouds":62,"visibility":10000,"wind_speed":6.76,"wind_deg":164,"wind_gust":6.9,"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],"pop":0},{"dt":1684450800,"temp":300.87,"feels_like":304.29,"pressure":1013,"humidity":78,"dew_point":296.7,"uvi":0,"clouds":53,"visibility":10000,"wind_speed":6.4,"wind_deg":168,"wind_gust":6.6,"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],"pop":0},{"dt":1684454400,"temp":300.81,"feels_like":304.28,"pressure":1012,"humidity":79,"dew_point":296.8,"uvi":0,"clouds":47,"visibility":10000,"wind_speed":6.43,"wind_deg":166,"wind_gust":6.91,"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03n"}],"pop":0},{"dt":1684458000,"temp":300.8,"feels_like":304.13,"pressure":1011,"humidity":78,"dew_point":296.51,"uvi":0,"clouds":33,"visibility":10000,"wind_speed":6.25,"wind_deg":159,"wind_gust":6.83,"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03n"}],"pop":0},{"dt":1684461600,"temp":300.8,"feels_like":304,"pressure":1011,"humidity":77,"dew_point":296.4,"uvi":0,"clouds":47,"visibility":10000,"wind_speed":5.54,"wind_deg":157,"wind_gust":6.3,"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03n"}],"pop":0},{"dt":1684465200,"temp":300.77,"feels_like":303.93,"pressure":1011,"humidity":77,"dew_point":296.5,"uvi":0,"clouds":64,"visibility":10000,"wind_speed":5.21,"wind_deg":149,"wind_gust":6.11,"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],"pop":0.08},{"dt":1684468800,"temp":300.76,"feels_like":304.04,"pressure":1011,"humidity":78,"dew_point":296.62,"uvi":0,"clouds":65,"visibility":10000,"wind_speed":4.85,"wind_deg":148,"wind_gust":5.9,"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],"pop":0.16},{"dt":1684472400,"temp":300.76,"feels_like":304.17,"pressure":1011,"humidity":79,"dew_point":296.71,"uvi":0,"clouds":72,"visibility":10000,"wind_speed":5.2,"wind_deg":154,"wind_gust":6.11,"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],"pop":0.16},{"dt":1684476000,"temp":300.97,"feels_like":304.52,"pressure":1012,"humidity":78,"dew_point":296.82,"uvi":0,"clouds":77,"visibility":10000,"wind_speed":5.52,"wind_deg":155,"wind_gust":6.5,"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"pop":0.12},{"dt":1684479600,"temp":301.07,"feels_like":304.61,"pressure":1013,"humidity":77,"dew_point":296.72,"uvi":0.53,"clouds":67,"visibility":10000,"wind_speed":5.63,"wind_deg":156,"wind_gust":6.62,"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"pop":0},{"dt":1684483200,"temp":301.25,"feels_like":305.18,"pressure":1013,"humidity":78,"dew_point":297,"uvi":2.13,"clouds":83,"visibility":10000,"wind_speed":5.67,"wind_deg":153,"wind_gust":6.91,"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"pop":0.04},{"dt":1684486800,"temp":301.26,"feels_like":305.21,"pressure":1014,"humidity":78,"dew_point":297.02,"uvi":4.94,"clouds":89,"visibility":10000,"wind_speed":6.22,"wind_deg":156,"wind_gust":7.12,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"pop":0.08},{"dt":1684490400,"temp":301.19,"feels_like":305.04,"pressure":1014,"humidity":78,"dew_point":297,"uvi":8.38,"clouds":92,"visibility":10000,"wind_speed":6.67,"wind_deg":162,"wind_gust":7.31,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"pop":0.16}],"daily":[{"dt":1684321200,"sunrise":1684302778,"sunset":1684346400,"moonrise":1684295820,"moonset":1684340340,"moon_phase":0.93,"temp":{"day":300.54,"min":300.46,"max":301.15,"night":300.82,"eve":301.11,"morn":300.65},"feels_like":{"day":304.01,"night":304.71,"eve":305.3,"morn":304.03},"pressure":1013,"humidity":82,"dew_point":297.19,"wind_speed":6.36,"wind_deg":156,"wind_gust":6.7,"weather":[{"id":501,"main":"Rain","description":"moderate rain","icon":"10d"}],"clouds":100,"pop":0.8,"rain":3.59,"uvi":10.81},{"dt":1684407600,"sunrise":1684389180,"sunset":1684432803,"moonrise":1684385040,"moonset":1684429680,"moon_phase":0.96,"temp":{"day":301.16,"min":300.32,"max":301.22,"night":300.87,"eve":301.12,"morn":300.7},"feels_like":{"day":305.27,"night":304.29,"eve":304.73,"morn":304.41},"pressure":1013,"humidity":80,"dew_point":297.33,"wind_speed":7,"wind_deg":136,"wind_gust":7.61,"weather":[{"id":501,"main":"Rain","description":"moderate rain","icon":"10d"}],"clouds":100,"pop":1,"rain":8.27,"uvi":9.39},{"dt":1684494000,"sunrise":1684475583,"sunset":1684519207,"moonrise":1684474440,"moonset":1684519080,"moon_phase":0,"temp":{"day":301.29,"min":300.41,"max":301.5,"night":300.41,"eve":300.76,"morn":300.76},"feels_like":{"day":305.12,"night":303.37,"eve":304.3,"morn":304.17},"pressure":1013,"humidity":77,"dew_point":296.96,"wind_speed":7.06,"wind_deg":174,"wind_gust":7.41,"weather":[{"id":501,"main":"Rain","description":"moderate rain","icon":"10d"}],"clouds":93,"pop":1,"rain":5.76,"uvi":12.09},{"dt":1684580400,"sunrise":1684561987,"sunset":1684605610,"moonrise":1684563900,"moonset":1684608660,"moon_phase":0.03,"temp":{"day":300.67,"min":298.82,"max":300.69,"night":299.12,"eve":298.82,"morn":300.32},"feels_like":{"day":304.21,"night":299.12,"eve":299.69,"morn":303.48},"pressure":1012,"humidity":81,"dew_point":297.1,"wind_speed":6.31,"wind_deg":149,"wind_gust":7.01,"weather":[{"id":501,"main":"Rain","description":"moderate rain","icon":"10d"}],"clouds":87,"pop":1,"rain":9.45,"uvi":11.39},{"dt":1684666800,"sunrise":1684648390,"sunset":1684692015,"moonrise":1684653540,"moonset":1684698300,"moon_phase":0.06,"temp":{"day":300.7,"min":299.62,"max":300.92,"night":300.78,"eve":300.92,"morn":300.36},"feels_like":{"day":303.9,"night":304.21,"eve":304.41,"morn":303.36},"pressure":1012,"humidity":78,"dew_point":296.4,"wind_speed":7.62,"wind_deg":164,"wind_gust":7.42,"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":88,"pop":0.52,"rain":0.45,"uvi":11.7},{"dt":1684753200,"sunrise":1684734795,"sunset":1684778420,"moonrise":1684743180,"moonset":1684787880,"moon_phase":0.09,"temp":{"day":300.65,"min":300.42,"max":300.65,"night":300.47,"eve":300.46,"morn":300.42},"feels_like":{"day":303.21,"night":303.07,"eve":302.84,"morn":302.97},"pressure":1013,"humidity":73,"dew_point":295.4,"wind_speed":7.96,"wind_deg":170,"wind_gust":8,"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"clouds":74,"pop":0.28,"uvi":12},{"dt":1684839600,"sunrise":1684821199,"sunset":1684864825,"moonrise":1684832760,"moonset":1684877460,"moon_phase":0.12,"temp":{"day":300.1,"min":299.88,"max":300.59,"night":300.59,"eve":300.28,"morn":299.99},"feels_like":{"day":302.34,"night":303.43,"eve":302.88,"morn":302.13},"pressure":1012,"humidity":75,"dew_point":295.3,"wind_speed":5.91,"wind_deg":187,"wind_gust":5.9,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"clouds":100,"pop":0,"uvi":12},{"dt":1684926000,"sunrise":1684907605,"sunset":1684951231,"moonrise":1684922220,"moonset":1684966800,"moon_phase":0.15,"temp":{"day":300.41,"min":300.16,"max":300.72,"night":300.72,"eve":300.69,"morn":300.21},"feels_like":{"day":303.05,"night":303.95,"eve":303.88,"morn":302.64},"pressure":1011,"humidity":76,"dew_point":295.8,"wind_speed":6.39,"wind_deg":174,"wind_gust":6.22,"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":100,"pop":0.2,"rain":0.13,"uvi":12}]}'

ForecastJSONsampleSnowString = '{"lat":80.5536,"lon":60.9828,"timezone":"Europe/Moscow","timezone_offset":10800,"current":{"dt":1684345031,"temp":270.24,"feels_like":270.24,"pressure":1000,"humidity":98,"dew_point":270,"uvi":0.37,"clouds":100,"visibility":301,"wind_speed":1.18,"wind_deg":147,"wind_gust":2.61,"weather":[{"id":600,"main":"Snow","description":"light snow","icon":"13n"}],"snow":{"1h":0.13}},"hourly":[{"dt":1684342800,"temp":270.15,"feels_like":267.59,"pressure":1000,"humidity":98,"dew_point":269.91,"uvi":0.44,"clouds":100,"visibility":225,"wind_speed":1.73,"wind_deg":110,"wind_gust":2.91,"weather":[{"id":600,"main":"Snow","description":"light snow","icon":"13d"}],"pop":0.76,"snow":{"1h":0.17}},{"dt":1684346400,"temp":270.24,"feels_like":270.24,"pressure":1000,"humidity":98,"dew_point":270,"uvi":0.37,"clouds":100,"visibility":301,"wind_speed":1.18,"wind_deg":147,"wind_gust":2.61,"weather":[{"id":600,"main":"Snow","description":"light snow","icon":"13d"}],"pop":0.76,"snow":{"1h":0.13}},{"dt":1684350000,"temp":270.35,"feels_like":268.25,"pressure":1000,"humidity":98,"dew_point":270.11,"uvi":0.3,"clouds":100,"visibility":276,"wind_speed":1.47,"wind_deg":178,"wind_gust":3.07,"weather":[{"id":600,"main":"Snow","description":"light snow","icon":"13d"}],"pop":0.44,"snow":{"1h":0.17}},{"dt":1684353600,"temp":270.49,"feels_like":267.53,"pressure":1000,"humidity":98,"dew_point":270.25,"uvi":0.28,"clouds":100,"visibility":203,"wind_speed":2.05,"wind_deg":208,"wind_gust":4.48,"weather":[{"id":600,"main":"Snow","description":"light snow","icon":"13d"}],"pop":0.48,"snow":{"1h":0.14}},{"dt":1684357200,"temp":270.94,"feels_like":267.38,"pressure":999,"humidity":97,"dew_point":270.58,"uvi":0.3,"clouds":100,"visibility":2051,"wind_speed":2.62,"wind_deg":230,"wind_gust":4.6,"weather":[{"id":600,"main":"Snow","description":"light snow","icon":"13d"}],"pop":0.6,"snow":{"1h":0.14}},{"dt":1684360800,"temp":270.94,"feels_like":268.19,"pressure":998,"humidity":97,"dew_point":270.58,"uvi":0.33,"clouds":100,"visibility":1679,"wind_speed":1.95,"wind_deg":243,"wind_gust":3.29,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"pop":0.56},{"dt":1684364400,"temp":269.96,"feels_like":269.96,"pressure":998,"humidity":98,"dew_point":269.77,"uvi":0.4,"clouds":99,"visibility":7518,"wind_speed":0.83,"wind_deg":269,"wind_gust":1.49,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"pop":0.52},{"dt":1684368000,"temp":269.37,"feels_like":269.37,"pressure":997,"humidity":97,"dew_point":269.03,"uvi":0.5,"clouds":99,"visibility":9692,"wind_speed":1.2,"wind_deg":350,"wind_gust":1.58,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"pop":0.44},{"dt":1684371600,"temp":269.73,"feels_like":266.53,"pressure":997,"humidity":96,"dew_point":269.26,"uvi":0.63,"clouds":100,"visibility":3101,"wind_speed":2.13,"wind_deg":16,"wind_gust":2.31,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"pop":0},{"dt":1684375200,"temp":269.68,"feels_like":265.73,"pressure":997,"humidity":96,"dew_point":269.21,"uvi":0.79,"clouds":100,"visibility":240,"wind_speed":2.76,"wind_deg":26,"wind_gust":3.11,"weather":[{"id":600,"main":"Snow","description":"light snow","icon":"13d"}],"pop":0.24,"snow":{"1h":0.11}},{"dt":1684378800,"temp":269.48,"feels_like":265.01,"pressure":997,"humidity":95,"dew_point":268.8,"uvi":0.99,"clouds":100,"visibility":311,"wind_speed":3.24,"wind_deg":23,"wind_gust":3.85,"weather":[{"id":600,"main":"Snow","description":"light snow","icon":"13d"}],"pop":0.35,"snow":{"1h":0.19}},{"dt":1684382400,"temp":269.52,"feels_like":264.57,"pressure":997,"humidity":94,"dew_point":268.67,"uvi":1.18,"clouds":100,"visibility":481,"wind_speed":3.8,"wind_deg":21,"wind_gust":4.58,"weather":[{"id":600,"main":"Snow","description":"light snow","icon":"13d"}],"pop":0.83,"snow":{"1h":0.14}},{"dt":1684386000,"temp":269.39,"feels_like":264.09,"pressure":997,"humidity":92,"dew_point":268.34,"uvi":1.38,"clouds":100,"visibility":835,"wind_speed":4.2,"wind_deg":20,"wind_gust":5.1,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"pop":0.87},{"dt":1684389600,"temp":269.13,"feels_like":263.38,"pressure":997,"humidity":91,"dew_point":267.91,"uvi":1.55,"clouds":100,"visibility":1432,"wind_speed":4.74,"wind_deg":21,"wind_gust":5.98,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"pop":0.71},{"dt":1684393200,"temp":268.77,"feels_like":262.45,"pressure":997,"humidity":90,"dew_point":267.3,"uvi":1.81,"clouds":100,"visibility":3349,"wind_speed":5.48,"wind_deg":20,"wind_gust":6.85,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"pop":0.4},{"dt":1684396800,"temp":268.36,"feels_like":261.36,"pressure":998,"humidity":90,"dew_point":266.86,"uvi":1.85,"clouds":100,"visibility":4472,"wind_speed":6.75,"wind_deg":20,"wind_gust":8.08,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"pop":0.32},{"dt":1684400400,"temp":267.81,"feels_like":260.81,"pressure":998,"humidity":89,"dew_point":266.28,"uvi":1.81,"clouds":100,"visibility":5656,"wind_speed":7.31,"wind_deg":20,"wind_gust":8.94,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"pop":0.33},{"dt":1684404000,"temp":267.14,"feels_like":260.14,"pressure":999,"humidity":90,"dew_point":265.64,"uvi":1.84,"clouds":100,"visibility":1720,"wind_speed":7.6,"wind_deg":19,"wind_gust":9.39,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"pop":0.36},{"dt":1684407600,"temp":266.5,"feels_like":259.5,"pressure":1000,"humidity":89,"dew_point":264.87,"uvi":1.63,"clouds":100,"visibility":3352,"wind_speed":7.75,"wind_deg":16,"wind_gust":9.78,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"pop":0.36},{"dt":1684411200,"temp":266,"feels_like":259,"pressure":1000,"humidity":88,"dew_point":264.16,"uvi":1.4,"clouds":100,"visibility":10000,"wind_speed":6.8,"wind_deg":13,"wind_gust":9.43,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"pop":0.35},{"dt":1684414800,"temp":265.44,"feels_like":258.44,"pressure":1001,"humidity":86,"dew_point":263.3,"uvi":1.16,"clouds":100,"visibility":10000,"wind_speed":6,"wind_deg":8,"wind_gust":8.65,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"pop":0.16},{"dt":1684418400,"temp":264.61,"feels_like":257.63,"pressure":1002,"humidity":86,"dew_point":262.35,"uvi":0.93,"clouds":100,"visibility":10000,"wind_speed":4.9,"wind_deg":2,"wind_gust":8.58,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"pop":0.16},{"dt":1684422000,"temp":263.24,"feels_like":256.77,"pressure":1003,"humidity":88,"dew_point":261.15,"uvi":0.74,"clouds":99,"visibility":10000,"wind_speed":3.92,"wind_deg":350,"wind_gust":6.49,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"pop":0.03},{"dt":1684425600,"temp":261.77,"feels_like":255.06,"pressure":1004,"humidity":91,"dew_point":260,"uvi":0.56,"clouds":99,"visibility":10000,"wind_speed":3.82,"wind_deg":342,"wind_gust":5.18,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"pop":0},{"dt":1684429200,"temp":261.42,"feels_like":254.81,"pressure":1004,"humidity":92,"dew_point":259.66,"uvi":0.46,"clouds":98,"visibility":10000,"wind_speed":3.65,"wind_deg":341,"wind_gust":4.91,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"pop":0},{"dt":1684432800,"temp":260.86,"feels_like":254.44,"pressure":1005,"humidity":90,"dew_point":258.81,"uvi":0.39,"clouds":99,"visibility":10000,"wind_speed":3.37,"wind_deg":336,"wind_gust":4.24,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"pop":0},{"dt":1684436400,"temp":259.71,"feels_like":253.34,"pressure":1006,"humidity":85,"dew_point":256.86,"uvi":0.35,"clouds":85,"visibility":10000,"wind_speed":3.13,"wind_deg":333,"wind_gust":2.93,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"pop":0},{"dt":1684440000,"temp":258.68,"feels_like":251.97,"pressure":1007,"humidity":80,"dew_point":255.01,"uvi":0.33,"clouds":72,"visibility":10000,"wind_speed":3.23,"wind_deg":327,"wind_gust":3.03,"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"pop":0},{"dt":1684443600,"temp":258.12,"feels_like":251.21,"pressure":1008,"humidity":78,"dew_point":254.01,"uvi":0.35,"clouds":56,"visibility":10000,"wind_speed":3.3,"wind_deg":320,"wind_gust":3.19,"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"pop":0},{"dt":1684447200,"temp":258.25,"feels_like":251.33,"pressure":1008,"humidity":77,"dew_point":254.02,"uvi":0.4,"clouds":43,"visibility":10000,"wind_speed":3.33,"wind_deg":313,"wind_gust":3.24,"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],"pop":0},{"dt":1684450800,"temp":258.55,"feels_like":251.65,"pressure":1009,"humidity":77,"dew_point":254.34,"uvi":0.48,"clouds":35,"visibility":10000,"wind_speed":3.36,"wind_deg":303,"wind_gust":3.29,"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],"pop":0},{"dt":1684454400,"temp":259.11,"feels_like":252.25,"pressure":1009,"humidity":77,"dew_point":254.94,"uvi":0.6,"clouds":29,"visibility":10000,"wind_speed":3.43,"wind_deg":297,"wind_gust":3.39,"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],"pop":0},{"dt":1684458000,"temp":259.88,"feels_like":253.22,"pressure":1010,"humidity":77,"dew_point":255.82,"uvi":0.77,"clouds":3,"visibility":10000,"wind_speed":3.4,"wind_deg":290,"wind_gust":3.6,"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"pop":0},{"dt":1684461600,"temp":260.34,"feels_like":253.53,"pressure":1011,"humidity":77,"dew_point":256.23,"uvi":0.96,"clouds":5,"visibility":10000,"wind_speed":3.62,"wind_deg":286,"wind_gust":4.89,"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"pop":0},{"dt":1684465200,"temp":260.74,"feels_like":253.99,"pressure":1011,"humidity":76,"dew_point":256.69,"uvi":1.21,"clouds":6,"visibility":10000,"wind_speed":3.64,"wind_deg":285,"wind_gust":5.35,"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"pop":0},{"dt":1684468800,"temp":261.29,"feels_like":254.87,"pressure":1012,"humidity":75,"dew_point":257.12,"uvi":1.46,"clouds":7,"visibility":10000,"wind_speed":3.45,"wind_deg":281,"wind_gust":5.14,"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"pop":0},{"dt":1684472400,"temp":261.75,"feels_like":255.62,"pressure":1012,"humidity":74,"dew_point":257.53,"uvi":1.7,"clouds":8,"visibility":10000,"wind_speed":3.28,"wind_deg":278,"wind_gust":5.07,"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"pop":0},{"dt":1684476000,"temp":262.29,"feels_like":256.38,"pressure":1013,"humidity":73,"dew_point":257.91,"uvi":1.91,"clouds":9,"visibility":10000,"wind_speed":3.19,"wind_deg":272,"wind_gust":5.02,"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"pop":0},{"dt":1684479600,"temp":262.68,"feels_like":256.88,"pressure":1013,"humidity":73,"dew_point":258.31,"uvi":1.99,"clouds":8,"visibility":10000,"wind_speed":3.16,"wind_deg":267,"wind_gust":4.91,"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"pop":0},{"dt":1684483200,"temp":262.99,"feels_like":257.18,"pressure":1013,"humidity":75,"dew_point":258.92,"uvi":2.03,"clouds":7,"visibility":10000,"wind_speed":3.23,"wind_deg":262,"wind_gust":5.52,"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"pop":0},{"dt":1684486800,"temp":263.22,"feels_like":257.29,"pressure":1014,"humidity":79,"dew_point":259.85,"uvi":1.98,"clouds":5,"visibility":10000,"wind_speed":3.38,"wind_deg":258,"wind_gust":6.21,"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"pop":0},{"dt":1684490400,"temp":263.41,"feels_like":257.22,"pressure":1014,"humidity":85,"dew_point":260.93,"uvi":1.91,"clouds":7,"visibility":10000,"wind_speed":3.67,"wind_deg":252,"wind_gust":8.23,"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"pop":0},{"dt":1684494000,"temp":263.55,"feels_like":257.14,"pressure":1014,"humidity":86,"dew_point":261.25,"uvi":1.7,"clouds":7,"visibility":10000,"wind_speed":3.93,"wind_deg":249,"wind_gust":8.6,"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"pop":0},{"dt":1684497600,"temp":263.56,"feels_like":257.13,"pressure":1014,"humidity":85,"dew_point":261.16,"uvi":1.45,"clouds":7,"visibility":10000,"wind_speed":3.95,"wind_deg":245,"wind_gust":7.28,"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"pop":0},{"dt":1684501200,"temp":263.53,"feels_like":256.97,"pressure":1014,"humidity":87,"dew_point":261.34,"uvi":1.22,"clouds":7,"visibility":10000,"wind_speed":4.08,"wind_deg":244,"wind_gust":7.28,"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"pop":0},{"dt":1684504800,"temp":263.63,"feels_like":256.81,"pressure":1014,"humidity":91,"dew_point":262.01,"uvi":0.97,"clouds":6,"visibility":10000,"wind_speed":4.4,"wind_deg":242,"wind_gust":7.28,"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"pop":0},{"dt":1684508400,"temp":263.68,"feels_like":256.68,"pressure":1013,"humidity":93,"dew_point":262.37,"uvi":0.78,"clouds":8,"visibility":10000,"wind_speed":4.7,"wind_deg":239,"wind_gust":7.44,"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"pop":0},{"dt":1684512000,"temp":263.33,"feels_like":256.33,"pressure":1013,"humidity":94,"dew_point":262.18,"uvi":0.61,"clouds":11,"visibility":10000,"wind_speed":4.81,"wind_deg":238,"wind_gust":7.46,"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02d"}],"pop":0}],"daily":[{"dt":1684314000,"sunrise":0,"sunset":0,"moonrise":0,"moonset":0,"moon_phase":0.92,"temp":{"day":266.22,"min":261.86,"max":270.49,"night":270.49,"eve":269.61,"morn":265.12},"feels_like":{"day":262.35,"night":267.53,"eve":266.37,"morn":261.78},"pressure":1004,"humidity":87,"dew_point":264.39,"wind_speed":3,"wind_deg":319,"wind_gust":4.48,"weather":[{"id":600,"main":"Snow","description":"light snow","icon":"13d"}],"clouds":42,"pop":0.76,"snow":1.4,"uvi":1.93},{"dt":1684400400,"sunrise":0,"sunset":0,"moonrise":0,"moonset":0,"moon_phase":0.96,"temp":{"day":267.81,"min":258.68,"max":270.94,"night":258.68,"eve":263.24,"morn":269.48},"feels_like":{"day":260.81,"night":251.97,"eve":256.77,"morn":265.01},"pressure":998,"humidity":89,"dew_point":266.28,"wind_speed":7.75,"wind_deg":16,"wind_gust":9.78,"weather":[{"id":600,"main":"Snow","description":"light snow","icon":"13d"}],"clouds":100,"pop":0.87,"snow":0.58,"uvi":1.85},{"dt":1684486800,"sunrise":0,"sunset":0,"moonrise":0,"moonset":0,"moon_phase":0,"temp":{"day":263.22,"min":258.12,"max":263.68,"night":261.96,"eve":263.68,"morn":260.74},"feels_like":{"day":257.29,"night":254.96,"eve":256.68,"morn":253.99},"pressure":1014,"humidity":79,"dew_point":259.85,"wind_speed":4.9,"wind_deg":243,"wind_gust":8.6,"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"clouds":5,"pop":0,"uvi":2.03},{"dt":1684573200,"sunrise":0,"sunset":0,"moonrise":0,"moonset":0,"moon_phase":0.02,"temp":{"day":268.59,"min":261.96,"max":268.75,"night":268.38,"eve":268.27,"morn":265.3},"feels_like":{"day":264.53,"night":263.4,"eve":264.28,"morn":259.78},"pressure":1011,"humidity":82,"dew_point":266.01,"wind_speed":4.79,"wind_deg":247,"wind_gust":8.08,"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02d"}],"clouds":24,"pop":0,"uvi":2.1},{"dt":1684659600,"sunrise":0,"sunset":0,"moonrise":0,"moonset":0,"moon_phase":0.06,"temp":{"day":273.35,"min":269.82,"max":273.35,"night":272.56,"eve":272.96,"morn":271.26},"feels_like":{"day":266.35,"night":265.56,"eve":265.96,"morn":264.26},"pressure":998,"humidity":98,"dew_point":273.16,"wind_speed":13.12,"wind_deg":279,"wind_gust":20.78,"weather":[{"id":616,"main":"Snow","description":"rain and snow","icon":"13d"}],"clouds":100,"pop":1,"rain":2.65,"snow":0.68,"uvi":1.56},{"dt":1684746000,"sunrise":0,"sunset":0,"moonrise":0,"moonset":0,"moon_phase":0.09,"temp":{"day":272.98,"min":272.52,"max":273.12,"night":272.84,"eve":272.9,"morn":272.77},"feels_like":{"day":268.31,"night":268.08,"eve":268.07,"morn":267.91},"pressure":1006,"humidity":96,"dew_point":272.58,"wind_speed":9.45,"wind_deg":262,"wind_gust":13.84,"weather":[{"id":600,"main":"Snow","description":"light snow","icon":"13d"}],"clouds":100,"pop":0.37,"snow":0.23,"uvi":2},{"dt":1684832400,"sunrise":0,"sunset":0,"moonrise":0,"moonset":0,"moon_phase":0.12,"temp":{"day":273.39,"min":270.59,"max":273.39,"night":272.72,"eve":273.21,"morn":272.36},"feels_like":{"day":270.06,"night":270.81,"eve":271.69,"morn":268.61},"pressure":1013,"humidity":95,"dew_point":272.81,"wind_speed":3.91,"wind_deg":267,"wind_gust":5.77,"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"clouds":58,"pop":0,"uvi":2},{"dt":1684918800,"sunrise":0,"sunset":0,"moonrise":0,"moonset":0,"moon_phase":0.15,"temp":{"day":272.82,"min":272.27,"max":273.15,"night":272.27,"eve":272.34,"morn":273.15},"feels_like":{"day":269.11,"night":267.24,"eve":267.59,"morn":270.15},"pressure":1015,"humidity":99,"dew_point":272.87,"wind_speed":4.82,"wind_deg":140,"wind_gust":10.3,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"clouds":100,"pop":0,"uvi":2}]}'


def twoDecimalPlaces(x):
    return ('%.2f' % x).rstrip('0').rstrip('.')


def colouredText(r, g, b, text):
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"


def ColourTable():
    x = 0
    for i in range(24):
        colors = ""
        for j in range(5):
            code = str(x + j)
            colors = colors + "\33[" + code + "m\\33[" + code + "m\033[0m "
        print(i, colors)
        x = x + 5


def UVIndexLevel(UVindexParameter):
    UVIndexLevelString = ""

    if (UVindexParameter == 0):
        UVIndexLevelString = ""

    if (UVindexParameter == 1):
        UVIndexLevelString = "UV Index " + str(round(UVindex)) + " Low"

    if (UVindexParameter == 2):
        UVIndexLevelString = "UV Index " + str(round(UVindex)) + " Low"

    if (UVindexParameter == 3):
        UVIndexLevelString = "UV Index " + str(round(UVindex)) + " Moderate"

    if (UVindexParameter == 4):
        UVIndexLevelString = "UV Index " + str(round(UVindex)) + " Moderate"

    if (UVindexParameter == 5):
        UVIndexLevelString = "UV Index " + str(round(UVindex)) + " Moderate"

    if (UVindexParameter == 6):
        UVIndexLevelString = "UV Index " + str(round(UVindex)) + " High"

    if (UVindexParameter == 7):
        UVIndexLevelString = "UV Index " + str(round(UVindex)) + " High"

    if (UVindexParameter == 8):
        UVIndexLevelString = "UV Index " + str(round(UVindex)) + " Very High"

    if (UVindexParameter == 9):
        UVIndexLevelString = "UV Index " + str(round(UVindex)) + " Very High"

    if (UVindexParameter == 10):
        UVIndexLevelString = "UV Index " + str(round(UVindex)) + " Very High"

    if (UVindexParameter >= 11):
        UVIndexLevelString = "UV Index " + str(round(UVindex)) + " Extreme"

    return UVIndexLevelString

def UVIndexLevelColouredText(UVindexParameter):
    UVIndexLevelString = ""

    if (UVindexParameter == 0):
        UVIndexLevelString = ""

    if (UVindexParameter == 1):
        UVIndexLevelString = colouredText(int("00", 16), int("FF", 16), int("00", 16), "UV Index " + " Low")

    if (UVindexParameter == 2):
        UVIndexLevelString = colouredText(int("00", 16), int("FF", 16), int("00", 16),
                                          "UV Index " + str(round(UVindex)) + " Low")

    if (UVindexParameter == 3):
        UVIndexLevelString = colouredText(int("FF", 16), int("EB", 16), int("3B", 16),
                                          "UV Index " + str(round(UVindex)) + " Moderate")

    if (UVindexParameter == 4):
        UVIndexLevelString = colouredText(int("FF", 16), int("EB", 16), int("3B", 16),
                                          "UV Index " + str(round(UVindex)) + " Moderate")

    if (UVindexParameter == 5):
        UVIndexLevelString = colouredText(int("FF", 16), int("EB", 16), int("3B", 16),
                                          "UV Index " + str(round(UVindex)) + " Moderate")

    if (UVindexParameter == 6):
        UVIndexLevelString = colouredText(int("FF", 16), int("98", 16), int("00", 16),
                                          "UV Index " + str(round(UVindex)) + " High")

    if (UVindexParameter == 7):
        UVIndexLevelString = colouredText(int("FF", 16), int("98", 16), int("00", 16),
                                          "UV Index " + str(round(UVindex)) + " High")

    if (UVindexParameter == 8):
        UVIndexLevelString = colouredText(int("FF", 16), int("00", 16), int("00", 16),
                                          "UV Index " + str(round(UVindex)) + " Very High")

    if (UVindexParameter == 9):
        UVIndexLevelString = colouredText(int("FF", 16), int("00", 16), int("00", 16),
                                          "UV Index " + str(round(UVindex)) + " Very High")

    if (UVindexParameter == 10):
        UVIndexLevelString = colouredText(int("FF", 16), int("00", 16), int("00", 16),
                                          "UV Index " + str(round(UVindex)) + " Very High")

    if (UVindexParameter >= 11):
        UVIndexLevelString = colouredText(int("C7", 16), int("27", 16), int("E3", 16),
                                          "UV Index " + str(round(UVindex)) + " Extreme")

    return UVIndexLevelString


def BearingToDirection(WindBearingParameter):
    locCompassHorizPoints = ""

    if (WindBearingParameter == -1):
        locCompassHorizPoints = "NORTH"

    if ((WindBearingParameter >= 348) and (WindBearingParameter <= 360)):
        locCompassHorizPoints = "NORTH"

    if ((WindBearingParameter >= 0) and (WindBearingParameter <= 11)):
        locCompassHorizPoints = "NORTH"

    if ((WindBearingParameter > 11) and (WindBearingParameter < 33)):
        locCompassHorizPoints = "N-N-E"

    if ((WindBearingParameter >= 33) and (WindBearingParameter <= 56)):
        locCompassHorizPoints = "NORTHEAST"

    if ((WindBearingParameter > 56) and (WindBearingParameter < 78)):
        locCompassHorizPoints = "E-N-E"

    if ((WindBearingParameter >= 78) and (WindBearingParameter <= 101)):
        locCompassHorizPoints = "EAST"

    if ((WindBearingParameter > 101) and (WindBearingParameter < 123)):
        locCompassHorizPoints = "E-S-E"

    if ((WindBearingParameter >= 123) and (WindBearingParameter <= 146)):
        locCompassHorizPoints = "SOUTHEAST"

    if ((WindBearingParameter > 146) and (WindBearingParameter < 168)):
        locCompassHorizPoints = "S-S-E"

    if ((WindBearingParameter >= 168) and (WindBearingParameter <= 191)):
        locCompassHorizPoints = "SOUTH"

    if ((WindBearingParameter > 191) and (WindBearingParameter < 213)):
        locCompassHorizPoints = "S-S-W"

    if ((WindBearingParameter >= 213) and (WindBearingParameter <= 236)):
        locCompassHorizPoints = "SOUTHWEST"

    if ((WindBearingParameter > 236) and (WindBearingParameter < 258)):
        locCompassHorizPoints = "W-S-W"

    if ((WindBearingParameter >= 258) and (WindBearingParameter <= 281)):
        locCompassHorizPoints = "WEST"

    if ((WindBearingParameter > 281) and (WindBearingParameter < 303)):
        locCompassHorizPoints = "W-N-W"

    if ((WindBearingParameter >= 303) and (WindBearingParameter <= 326)):
        locCompassHorizPoints = "NORTHWEST"

    if ((WindBearingParameter > 326) and (WindBearingParameter < 348)):
        locCompassHorizPoints = "N-N-W"

    return locCompassHorizPoints


print(lineFeed + url + lineFeed)

if useSampleData == True:
    print("Test Data... ")
    if sampleDataType == "sunny":
        ForecastJSON = json.loads(ForecastJSONsampleSunnyString)
        print("[Sunny] " + lineFeed)
    if sampleDataType == "rain":
        ForecastJSON = json.loads(ForecastJSONsampleRainString)
        print("[Rain] " + lineFeed)
    if sampleDataType == "snow":
        ForecastJSON = json.loads(ForecastJSONsampleSnowString)
        print("[Snow] " + lineFeed)
else:
    print("Web API Data..." + lineFeed)
    response = requests.get(url)
    ForecastJSON = json.loads(response.text)

print(colouredText(int("50", 16), int("50", 16), int("50", 16), "ForecastJSONweather: " + str(ForecastJSON) + lineFeed))

fldUnixTime = str(ForecastJSON["current"]["dt"])
print("Unix Time: " + fldUnixTime + lineFeed)

ForecastJSONweatherString = str(ForecastJSON["current"]["weather"])
ForecastJSONweatherString = ForecastJSONweatherString.replace('[', '')
ForecastJSONweatherString = ForecastJSONweatherString.replace(']', '')
ForecastJSONweatherString = ForecastJSONweatherString.replace('\'', '"')
print(colouredText(int("50", 16), int("50", 16), int("50", 16),
                   "ForecastJSONweatherString: " + ForecastJSONweatherString + lineFeed))

ForecastJSONweather = json.loads(ForecastJSONweatherString)
print(colouredText(int("50", 16), int("50", 16), int("50", 16),
                   "ForecastJSONweather: " + str(ForecastJSONweather) + lineFeed))

fldLatitude = str(ForecastJSON["lat"])
print("Lat: " + fldLatitude)

fldLongitude = str(ForecastJSON["lon"])
print("Lon: " + fldLongitude)

fldIcon = str(ForecastJSONweather["icon"])
print("Icon: " + fldIcon)

os.open("Icons/" + fldIcon + ".png", 0)

fldDescription = str(ForecastJSONweather["description"])
print("Description: " + fldDescription)
TempString = str(ForecastJSON["current"]["temp"])
TempValue = float(TempString)
TempValue = TempValue - 273.15
fldTemp = str(round(TempValue)) + "°C"
print("Temp: " + fldTemp)

UVindex = float(str(ForecastJSON["current"]["uvi"]))
if UVindex < 1:
    fldUV = str(UVindex)
    print(fldUV)
else:
    fldUV = str(UVIndexLevel(round(UVindex))).replace("UV Index ", "")
    print(str(UVIndexLevelColouredText(round(UVindex))))

WindSpeedString = str(ForecastJSON["current"]["wind_speed"])
WindSpeedValue = float(WindSpeedString)
WindSpeedValue = WindSpeedValue * 2.236936
WindBearingString = str(ForecastJSON["current"]["wind_deg"])
fldWindDirection = BearingToDirection(round(int(WindBearingString))) + " Bearing: " + str(round(int(WindBearingString))) + "° Speed: " + twoDecimalPlaces(WindSpeedValue) + " mph"
print(fldWindDirection)

MillibarString = str(ForecastJSON["current"]["pressure"])
fldPressure = str(round(int(MillibarString))) + " hPa"
print("Pressure: " + fldPressure)

HumidityString = str(ForecastJSON["current"]["humidity"])
fldHumidity = str(round(int(HumidityString))) + "%"
print("Humidity: " + fldHumidity)

DewPointString = str(ForecastJSON["current"]["dew_point"])
DewPointValue = float(DewPointString)
DewPointValue = DewPointValue - 273.15
fldDewPoint = str(round(DewPointValue)) + "°C"
print("DewPoint: " + fldDewPoint)

CloudCoverString = str(ForecastJSON["current"]["clouds"])
fldCloudCover = str(round(int(CloudCoverString))) + "%"
print("CloudCover: " + fldCloudCover)

VisibilityString = str(ForecastJSON["current"]["visibility"])
fldVisibility = twoDecimalPlaces(int(VisibilityString) * 0.0006213712) + " miles"

print("Visibility: " + fldVisibility + lineFeed)

ForecastJSONHourlyItem0String = str(ForecastJSON["hourly"][0])
ForecastJSONHourlyItem0String = ForecastJSONHourlyItem0String.replace('\'', '"')
print(colouredText(int("50", 16), int("50", 16), int("50", 16),
                   "ForecastJSONHourlyItem0String: " + ForecastJSONHourlyItem0String + lineFeed))

ForecastJSONhourlyItem0 = json.loads(ForecastJSONHourlyItem0String)
print(colouredText(int("50", 16), int("50", 16), int("50", 16),
                   "ForecastJSONhourlyItem0: " + str(ForecastJSONhourlyItem0) + lineFeed))

PrecipProbability = str(ForecastJSONhourlyItem0["pop"])
PrecipProbabilityValue = float(PrecipProbability) * 100
fldPrecipitationProbability = str(round(PrecipProbabilityValue)) + "% pop/h"

print("PrecipitationProbability: " + fldPrecipitationProbability + lineFeed)

fldPrecipIntensity = ""

try:
    ForecastJSONRainString = str(ForecastJSON["current"]["rain"])
    ForecastJSONRainString = ForecastJSONRainString.replace('\'', '"')
    print(colouredText(int("50", 16), int("50", 16), int("50", 16),
                       "ForecastJSONweatherString: " + ForecastJSONRainString + lineFeed))

    ForecastJSONrain = json.loads(ForecastJSONRainString)
    print(colouredText(int("50", 16), int("50", 16), int("50", 16),
                       "ForecastJSONrain: " + str(ForecastJSONrain) + lineFeed))

    PrecipIntensityString = str(ForecastJSONrain["1h"])
    fldPrecipIntensity = PrecipIntensityString + "mm/h"
    print("Rain Precipitation Intensity: " + fldPrecipIntensity + lineFeed)

except:
    fldPrecipIntensity = "0mm/h"
    print("No rain")

try:
    ForecastJSONSnowString = str(ForecastJSON["current"]["snow"])
    ForecastJSONSnowString = ForecastJSONSnowString.replace('\'', '"')
    print(colouredText(int("50", 16), int("50", 16), int("50", 16),
                       "ForecastJSONweatherString: " + ForecastJSONSnowString + lineFeed))

    ForecastJSONsnow = json.loads(ForecastJSONSnowString)
    print(colouredText(int("50", 16), int("50", 16), int("50", 16),
                       "ForecastJSONsnow: " + str(ForecastJSONsnow) + lineFeed))

    PrecipIntensityString = str(ForecastJSONsnow["1h"])
    fldPrecipIntensity = PrecipIntensityString + "mm/h"
    print("Snow Precipitation Intensity: " + fldPrecipIntensity + lineFeed)

except:
    fldPrecipIntensity = "0mm/h"
    print("No snow")

ForecastJSONString = str(ForecastJSON).replace("'", "''")

SqlInsertForecast = "INSERT INTO tblForecast (fldLatitude, fldLongitude, fldUnixTime, fldIcon, fldDescription, fldTemp, fldUV, fldWindDirection, fldPressure, fldHumidity, fldDewPoint, fldCloudCover, fldVisibility, fldPrecipitationProbability, fldPrecipitationIntensity, fldJSON) VALUES ('" + fldLatitude + "', '" + fldLongitude + "', '" + fldUnixTime + "', '" + fldIcon + "', '" + fldDescription + "', '" + fldTemp + "', '" + fldUV + "', '" + fldWindDirection + "', '" + fldPressure + "', '" + fldHumidity + "', '" + fldDewPoint + "', '" + fldCloudCover + "', '" + fldVisibility + "', '" + fldPrecipitationProbability + "', '" + fldPrecipIntensity + "', '" + ForecastJSONString + "')"

#print("\n" + SqlInsertForecast)

try:
    cursor.execute(SqlInsertForecast)
    connection.commit()
    print("\nForecast record inserted into SQLite database\n")

except sqlite3.Error as e:
        print("\n" + e + "\n")

# ColourTable()
