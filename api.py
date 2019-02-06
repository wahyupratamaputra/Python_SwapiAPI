import requests, json
from sqlalchemy.exc import IntegrityError
from models import Person, Film, Vehicle, Starship, Species, Planet, Driver, Pilot, Role, Member
from base import DbManager
import sys
from pprint import pprint


class StarwarsApi(DbManager):
    def __init__(self):
        super(StarwarsApi, self).__init__()


    def grabAllData(self, kategori):
        count = json.loads(requests.get("https://swapi.co/api/{}/".format(kategori)).text)['count']
        alldata = []
        for page in range(1, count):
            url2 = requests.get("https://swapi.co/api/{}/?page={}".format(kategori, page))
            if url2.status_code != 404:
                for data in json.loads(url2.text)['results']:
                    alldata.append(data)
            else:
                return alldata
        print("page {}".format(page))
        
    
    def savePeople(self): 
        alldata = self.grabAllData("people")
        for data in alldata:
            # get person from database
            person = self.find_or_create(data, Person)
            # get planet from database
            planet = self.find_or_create(json.loads(requests.get(data['homeworld']).text), Planet)

            
            for v in data['vehicles']:
                vehicle = self.find_or_create(json.loads(requests.get(v).text), Vehicle)
                try:
                    self.open().query(Driver).filter(Driver.person == person, Driver.vehicle == vehicle).one()
                    print("data already exist")
                except:
                    driver = Driver()
                    driver.vehicle = vehicle
                    driver.person = person
                    self.save(driver)
                    print("Driver Vehicle saved")
            
            for s in data['starships']:
                starship = self.find_or_create(json.loads(requests.get(s).text), Starship)
                try:
                    self.open().query(Driver).filter(Driver.person == person, Driver.starship == starship).one()
                    print("data already exist")
                except:
                    pilot = Pilot()
                    pilot.starship = starship
                    pilot.person = person
                    self.save(pilot)
                    print("Pilot Starships saved")
            

            for f in data['films']:
                film = self.find_or_create(json.loads(requests.get(f).text), Film)
                try:
                    self.open().query(Role).filter(Role.person == person, Role.film == film).one()
                    print("data film already exist")
                except:
                    role = Role()
                    role.film = film
                    role.person = person
                    self.save(role)
                    print("Role  saved")
            
            for s in data['species']:
                species = self.find_or_create(json.loads(requests.get(s).text), Species)
                try:
                    self.open().query(Member).filter(Member.person == person, Member.species == species).one()
                    print("data species already exist")
                except:
                    member = Member()
                    member.species = species
                    member.person = person
                    self.save(member)
                    print("Member saved")

            print(planet)
            if not person.homeworld:
                person.homeworld = planet
                self.save(person)
            

            #add planet based on vehicle
            vehicle = self.find_or_create(json.loads(requests.get(data['homeworld']).text), Planet)

    def saveVehicle(self):
        alldata = self.grabAllData("vehicles")
        for data in alldata:
            savingdata = Vehicle()
            savingdata.parse(data)
            self.save(savingdata)
            return savingdata

    def find_or_create(self, data, model):
        try:
            obj = self.open().query(model).filter(model.name == data['name']).one()
            print('-> found {} in db'.format(model.__name__))
            return obj
        except:
            try:
                obj = self.open().query(model).filter(model.title == data['title']).one()
                print('-> found {} in db'.format(model.__name__))
                return obj
            except:
                pass

        try:
            savingdata = model()
            savingdata.parse(data)
            self.save(savingdata)
            print('-> created {} in db'.format(model.__name__))
            return savingdata
        except Exception as e: 
            print(e)
        

    def getPeople(self, total):
        peoples = self.open().query(Person).order_by(Person.id).limit(total).all()
        for people in peoples:
            print(people.name)

    def getVehicleAndStarship(self, total): #Print out the vehicles and starships of the first 10 people
        peoples = self.open().query(Person).limit(total).all()
        for people in peoples:
            drivers = self.open().query(Driver).filter(Driver.person == people).all()
            print("------------\n{} can drive :".format(people.name))
            for driver in drivers:
                print(driver.vehicle.name)

            print("--starship--")
            pilots = self.open().query(Pilot).filter(Pilot.person == people).all()
            for pilot in pilots:
                print(pilot.starship.name)

    def getPeopleWhoRide(self, starshipname): #Print out the names of people who fly X-wing fighters
        starship = self.open().query(Starship).filter(Starship.name == starshipname).first()
        pilots = self.open().query(Pilot).filter(Pilot.starship == starship).all()
        print("These are name who can flying {} : ".format(starshipname))
        for pilot in pilots:
            print(pilot.person.name)

    def listSpeciesByPlanet(self): ##not yet
        planets = self.open().query(Planet).all()
        for planet in planets:
            members = self.open().query(Member).filter(Member.person == planet).all()
            print("--------{}--------".format(planet.name))
            for member in members:
                print(member.species.name)
    
    def getFemalePilots(self):
        pilots = self.open().query(Pilot).all()
        femalepilots = []
        for pilot in pilots:
            #female = self.open().query(Person).filter().all()
            if pilot.person.gender == "female":
                if pilot.person not in femalepilots:
                    femalepilots.append(pilot.person)

        for femalepilot in femalepilots:
            print(femalepilot.name)
        # for pilot in femalepilots:
        #     print(pilot)