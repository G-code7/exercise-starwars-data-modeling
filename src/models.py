import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(120), nullable=False)
    first_name = Column(String(80), nullable=True)
    last_name = Column(String(80), nullable=True)
    subscription_date = Column(DateTime, default=datetime.utcnow)

    favorites = relationship('Favorite', backref='user', lazy=True)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    climate = Column(String(100), nullable=True)
    terrain = Column(String(100), nullable=True)
    population = Column(Integer, nullable=True)

    favorites = relationship('Favorite', backref='planet', lazy=True)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    gender = Column(String(10), nullable=True)
    birth_year = Column(String(10), nullable=True)
    height = Column(Integer, nullable=True)

    favorites = relationship('Favorite', backref='character', lazy=True)

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)

# Diagrama ERD
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem generating the diagram")
    raise e
