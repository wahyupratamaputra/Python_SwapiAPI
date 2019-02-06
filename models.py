from sqlalchemy.orm import relationship, backref, joinedload
from sqlalchemy import Column, DateTime, String, Integer, Float, ForeignKey, func, desc

from base import Base, inverse_relationship, create_tables

# ADD MODELS
class Person(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    height = Column(String)
    mass = Column(Integer)
    hair_color = Column(String)
    skin_color = Column(String)
    eye_color = Column(String)
    birth_year = Column(String)
    gender = Column(String)
    films = Column(String)
    species = Column(String)
    vehicles = Column(String)
    # ######
    planet_id = Column(Integer,ForeignKey('planets.id'))
    homeworld = relationship('Planet', backref=inverse_relationship('residents'))
    # ######
    #####
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    url = Column(String)

    def parse(self, data):
        self.name = data['name']
        self.height = data['height']
        self.mass = data['mass']
        self.hair_color = data['hair_color']
        self.skin_color = data['skin_color']
        self.eye_color = data['eye_color']
        self.birth_year = data['birth_year']
        self.gender = data['gender']
        self.films = str(data['films'])
        self.species = str(data['species'])
        self.vehicles = str(data['vehicles'])
        self.starships = str(data['starships'])
        self.created = data['created']
        self.edited = data['edited']
        self.url = data['url']


class Film(Base):
    __tablename__ = 'films'
    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True)
    characters = Column(String)
    director = Column(String)
    episode_id = Column(Integer)
    opening_crawl = Column(String)
    planets = Column(String)
    producer = Column(String)
    release_date = Column(String)
    species = Column(String)
    vehicles = Column(String)
    starships = Column(String)
    url = Column(String)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def parse(self, data):
        self.title = data['title']
        self.characters = str(data['characters'])
        self.director = data['director']
        self.episode_id = data['episode_id']
        self.opening_crawl = data['opening_crawl']
        self.planets = str(data['planets'])
        self.producer = data['producer']
        self.release_date = data['release_date']
        self.species = str(data['species'])
        self.vehicles = str(data['vehicles'])
        self.starships = str(data['starships'])
        self.url = data['url']
        self.created = data['created']
        self.edited = data['edited']

class Starship(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    MGLT = Column(String)
    cargo_capacity = Column(Integer)
    consumables = Column(String)
    cost_in_credits = Column(Integer)
    crew = Column(Integer)
    length = Column(Integer)
    manufacturer = Column(String)
    max_atmosphering_speed = Column(Integer)
    model = Column(String)
    passengers = Column(Integer)
    films = Column(String)
    starship_class = Column(String)
    url = Column(String)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    
    def parse(self, data):
        self.name = data['name']
        self.MGLT = data['MGLT']
        self.cargo_capacity = data['cargo_capacity']
        self.consumables = data['consumables']
        self.cost_in_credits = data['cost_in_credits']
        self.crew = data['crew']
        self.hyperdrive_rating = data['hyperdrive_rating']
        self.length = data['length']
        self.manufacturer = data['manufacturer']
        self.max_atmosphering_speed = data['max_atmosphering_speed']
        self.model = data['model']
        self.passengers = data['passengers']
        self.films = str(data['films'])
        self.starship_class = data['starship_class']
        self.url = data['url']
        self.created = data['created']
        self.edited = data['edited']

    def __str__(self):
        return self.name
class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    cargo_capacity = Column(Integer)
    consumables = Column(String)
    cost_in_credits = Column(Integer)
    crew = Column(Integer)
    length = Column(String)
    manufacturer = Column(String)
    max_atmosphering_speed = Column(Integer)
    model = Column(String)
    passengers = Column(Integer)
    films = Column(String)
    vehicle_class = Column(String)
    url = Column(String)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def parse(self, data):
        self.name = data['name']
        self.cargo_capacity = data['cargo_capacity']
        self.consumables = data['consumables']
        self.cost_in_credits = data['cost_in_credits']
        self.crew = data['crew']
        self.length = data['length']
        self.manufacturer = data['manufacturer']
        self.max_atmosphering_speed = data['max_atmosphering_speed']
        self.model = data['model']
        self.passengers = data['passengers']
        self.films = str(data['films'])
        self.vehicle_class = data['vehicle_class']
        self.url = data['url']
        self.created = data['created']
        self.edited = data['edited']

    def __str__(self):
        return self.name
class Species(Base):
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    average_height = Column(String)
    average_lifespan = Column(Integer)
    classification = Column(String)
    designation = Column(String)
    eye_colors = Column(String)
    hair_colors = Column(String)
    homeworld = Column(String)
    language = Column(String)
    people = Column(String)
    films = Column(String)
    skin_colors = Column(String)
    url = Column(String)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def parse(self, data):
        self.name = data['name']
        self.average_height = data['average_height']
        self.average_lifespan = data['average_lifespan']
        self.classification = data['classification']
        self.designation = data['designation']
        self.eye_colors = data['eye_colors']
        self.hair_colors = data['hair_colors']
        self.homeworld = data['homeworld']
        self.language = data['language']
        self.people = str(data['people'])
        self.films = str(data['films'])
        self.skin_colors = data['skin_colors']
        self.url = data['url']
        self.created = data['created']
        self.edited = data['edited']

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    climate = Column(String)
    diameter = Column(Integer)
    films = Column(String)
    gravity = Column(String)
    orbital_period = Column(String)
    population = Column(Integer)
    rotation_period = Column(Integer)
    surface_water = Column(Integer)
    terrain = Column(String)
    url = Column(String)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def parse(self, data):
        self.name = data['name']
        self.climate = data['climate']
        self.diameter = data['diameter']
        self.films = str(data['films'])
        self.gravity = data['gravity']
        self.orbital_period = data['orbital_period']
        self.population = data['population']
        self.rotation_period = data['rotation_period']
        self.surface_water = data['surface_water']
        self.terrain = data['terrain']
        self.url = data['url']
        self.created = data['created']
        self.edited = data['edited']

    def __str__(self):
        return self.name

class Driver(Base):
    __tablename__ = 'drivers'
    id = Column(Integer, primary_key=True)

    vehicle_id = Column(Integer,ForeignKey('vehicles.id'))
    vehicle = relationship('Vehicle', backref=inverse_relationship('driven_by'))
    person_id = Column(Integer, ForeignKey('people.id'))
    person = relationship('Person', backref=inverse_relationship('driver_of'))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    def __str__(self):
        pass

class Pilot(Base):
    __tablename__ = 'pilots'
    id = Column(Integer, primary_key=True)
    starship_id = Column(Integer,ForeignKey('starships.id'))
    starship = relationship('Starship', backref=inverse_relationship('pilot_by'))
    person_id = Column(Integer, ForeignKey('people.id'))
    person = relationship('Person', backref=inverse_relationship('pilot_of'))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


class Member(Base):
    __tablename__ = 'members'
    id = Column(Integer, primary_key=True)
    species_id = Column(Integer,ForeignKey('species.id'))
    species = relationship('Species', backref=inverse_relationship('species_by'))
    person_id = Column(Integer, ForeignKey('people.id'))
    person = relationship('Person', backref=inverse_relationship('species_of'))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    film_id = Column(Integer,ForeignKey('films.id'))
    film = relationship('Film', backref=inverse_relationship('film_by'))
    person_id = Column(Integer, ForeignKey('people.id'))
    person = relationship('Person', backref=inverse_relationship('film_of'))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
# ADD MODELS 




if __name__ is not '__main__':
    create_tables()