import requests
import json
import Asteroid

def createAsteroids:
    asteroids = [];

    # Parameters for the search, feel free to edit <3
    startDate = "2015-09-07"
    endDate = "2015-09-08"
    apiKey = "jWyOLoAzhBbJ82DBDMFLS47BL5juRll6uUrVeUic"
    parameters = {"start_date": startDate, "end_date": endDate, "api_key": apiKey}

    # Gets response in a string <3
    response = requests.get("https://api.nasa.gov/neo/rest/v1/feed", params=parameters)
    print(response.status_code)

    # Puts response in data object that is of type JSON <3
    data = json.loads(response.content);

    # Obtains all the asteroids in a JSON array
    asteroidData = data['near_earth_objects']


    # Loops through every date, and for every date gets each asteroid and prints data
    asteroidNum = 0;
    for date in asteroidData:
            print(date);
            dateArray = asteroidData[date]
            for asteroid in dateArray:
                asteroidNum += 1
                minDistance = asteroid['estimated_diameter']['kilometers']['estimated_diameter_min']
                maxDistance = asteroid['estimated_diameter']['kilometers']['estimated_diameter_max']
                closeApproachData = asteroid['close_approach_data'][0] #Don't mind this...
                relativeVelocity = closeApproachData['relative_velocity']['kilometers_per_second']
                missDistance = closeApproachData['miss_distance']['kilometers']
                a = Asteroid(minDistance, maxDistance, relativeVelocity, missDistance)
                asteroids.append(a)
    return asteroids
