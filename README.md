# Celero-challange
This project is a challange to work in a Celero Team

List with all activites:

[X] Create a Atletic model 
[] Make a CRUD to Atletics
  [] GET
  [] POST
  [] PATCH
  [] DELETE
[] Implements a Postgres Database
[X] Up application and database using Docker
[] Run a routine to populate database based on csv file
[] Make some filters - need more details 
[] Unitary tests

Any problems during the development aplication:
  1 - When the docker-compose was up, the connection between app and container was refused!
  Solution: The host option in the settings.py need be a name of database container