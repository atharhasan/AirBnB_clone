# This the repo of our coool co-op project together for the 4th time.

In this project we aim to create a full website of booking flights and hotels... etc.

We will keep updating here till we finish the project.

## First step 
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
create the first abstracted storage engine of the project: File storage.
create all unittests to validate all our classes and storage engine

## create base model
Write a class BaseModel that defines all common attributes/methods for other classes:

models/base_model.py
Public instance attributes:
id: string - assign with an uuid when an instance is created:
you can use uuid.uuid4() to generate unique id but don’t forget to convert to a string
the goal is to have unique id for each BaseModel
created_at: datetime - assign with the current datetime when an instance is created
updated_at: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object
__str__: should print: [<class name>] (<self.id>) <self.__dict__>
Public instance methods:
save(self): updates the public instance attribute updated_at with the current datetime
to_dict(self): returns a dictionary containing all keys/values of __dict__ of the instance:
by using self.__dict__, only instance attributes set will be returned
a key __class__ must be added to this dictionary with the class name of the object
created_at and updated_at must be converted to string object in ISO format:
format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
you can use isoformat() of datetime object
This method will be the first piece of the serialization/deserialization process: create a dictionary representation with “simple object type” of our BaseModel

## Create BaseModel from dictionary
Update models/base_model.py:

__init__(self, *args, **kwargs):
you will use *args, **kwargs arguments for the constructor of a BaseModel. (more information inside the AirBnB clone concept page)
*args won’t be used
if kwargs is not empty:
each key of this dictionary is an attribute name (Note __class__ from kwargs is the only one that should not be added as an attribute. See the example output, below)
each value of this dictionary is the value of this attribute name
Warning: created_at and updated_at are strings in this dictionary, but inside your BaseModel instance is working with datetime object. You have to convert these strings into datetime object. Tip: you know the string format of these datetime
otherwise:
create id and created_at as you did previously (new instance)

## Store first object
Terms:

simple Python data structure: Dictionaries, arrays, number and string. ex: { '12': { 'numbers': [1, 2, 3], 'name': "John" } }
JSON string representation: String representing a simple data structure in JSON format. ex: '{ "12": { "numbers": [1, 2, 3], "name": "John" } }'
Write a class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances:

models/engine/file_storage.py
Private class attributes:
__file_path: string - path to the JSON file (ex: file.json)
__objects: dictionary - empty but will store all objects by <class name>.id (ex: to store a BaseModel object with id=12121212, the key will be BaseModel.12121212)
Public instance methods:
all(self): returns the dictionary __objects
new(self, obj): sets in __objects the obj with key <obj class name>.id
save(self): serializes __objects to the JSON file (path: __file_path)
reload(self): deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
Update models/__init__.py: to create a unique FileStorage instance for your application

import file_storage.py
create the variable storage, an instance of FileStorage
call reload() method on this variable
Update models/base_model.py: to link your BaseModel to FileStorage by using the variable storage

import the variable storage
in the method save(self):
call save(self) method of storage
__init__(self, *args, **kwargs):
if it’s a new instance (not from a dictionary representation), add a call to the method new(self) on storage
