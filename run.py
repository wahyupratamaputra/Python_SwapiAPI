import requests, json

from api import StarwarsApi
from models import Person, Planet

swapi = StarwarsApi()


#swapi.savePeople()

#swapi.getPeople(10)
#swapi.getVehicleAndStarship(10)
#swapi.getPeopleWhoRide("Millennium Falcon")

#swapi.listSpeciesByPlanet()

swapi.getFemalePilots()