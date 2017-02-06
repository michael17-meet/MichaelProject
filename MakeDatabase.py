from sqlalchemy import Column,Integer,String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, func
from passlib.apps import custom_app_context as pwd_context
import string
from itsdangerous import(TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)

Base=declarative_base()

class Users(Base):
	__tablename__='users'
	id=Column(Integer, primary_key=True)
	name=Column(String(100))
	password=Column(String(100))
	job=Column(String(100))
	#user_group_id=Column(Integer, ForeignKey('groups.id)'))

	def passwordF(self, password):
		self.password=pwd_context.encrypt(password)

	def verify_password(self, password):
		return pwd_context.verify(password, self.password)

class Groups(Base):
	__tablename__='groups'
	id=Column(Integer, primary_key=True)
	age_of_group=Column(String(10))
	#camper_id=Column(Integer, ForeignKey('campers.id)'))

class Campers(Base):
	__tablename__='campers'
	id=Column(Integer, primary_key=True)
	name=Column(String(100))
	sex=Column(String(10))
	#camper_group=relationship()
	cell_phone=Column(Integer)

class Activities(Base):
	__tablename__='activities'
	id=Column(Integer, primary_key=True)
	subject=Column(String(100))
	name=Column(String(100))
	recommend_age=Column(String(100))
	name_of_game_1=(String(100))
	explanation_of_game_1=(String(50000))
	game_1_equipment=(String(1000))
	time_for_game_1=(String(100))
	game_1_leader=(String(100))
	name_of_game_2=(String(100))
	explanation_of_game_2=(String(50000))
	game_2_equipment=(String(1000))
	time_for_game_2=(String(100))
	game_2_leader=(String(100))
	name_of_game_3=(String(100))
	explanation_of_game_3=(String(50000))
	game_3_equipment=(String(1000))
	time_for_game_3=(String(100))
	game_3_leader=(String(100))
	name_of_game_4=(String(100))
	explanation_of_game_4=(String(50000))
	game_4_equipment=(String(1000))
	time_for_game_4=(String(100))
	game_4_leader=(String(100))
	name_of_game_5=(String(100))
	explanation_of_game_5=(String(50000))
	game_5_equipment=(String(1000))
	time_for_game_5=(String(100))
	game_5_leader=(String(100))

class Events(Base):
	__tablename__='events'
	id=Column(Integer, primary_key=True)
	date=Column(String(10))
	name=Column(String(100))
	event_for=Column(String(100))
	explanation_of_event=Column(String(10000))
	

engine = create_engine('sqlite:///Database.db')
Base.metadata.create_all(engine)
