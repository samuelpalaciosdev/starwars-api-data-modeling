import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(50), nullable=False)

class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    height = Column(String(50))
    mass = Column(String(50))
    hair_color = Column(String(20))
    skin_color = Column(String(20))
    eye_color = Column(String(20))
    birth_year = Column(String(50))
    gender = Column(String(20))

class FavoriteCharacter(Base):
    __tablename__ = 'favorite_characters'
    character_id = Column(Integer, ForeignKey('characters.id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    rotation_period= Column(Integer)
    orbital_period= Column(Integer)
    diameter = Column(Integer)
    climate = Column(String(100))
    gravity = Column(String(50))
    terrain = Column(String(100))
    surface_water = Column(String(50))
    population = Column(Integer)

class FavoritePlanet(Base):
    __tablename__ = 'favorite_planets'
    planet_id = Column(Integer, ForeignKey('planets.id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)
    model = Column(String(100))
    manufacturer = Column(String(100))
    cost_in_credits = Column(Integer)
    length = Column(Integer)
    max_atmospheric_speed = Column(Integer)
    crew = Column(Integer)
    passengers = Column(Integer)
    cargo_capacity = Column(Integer)
    consumables = Column(String(100))
    vehicle_class = Column(String(100))

class FavoriteVehicle(Base):
    __tablename__ = 'favorite_vehicles'
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')