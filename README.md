# Celero-challange
This project is a challange to work in a Celero Team

List with all activites:

[X] Create a Atletic model 
[X] Make a CRUD to Atletics
  [X] GET
  [X] POST
  [X] PATCH
  [X] DELETE
[X] Implements a Postgres Database
[X] Up application and database using Docker
  [X] Add portrainer to monitor logs and interage with individual containers
[] Run a routine to populate database based on csv file

[] Make some filters - need more details
[] Create a superuser outside the container 
[] Unitary tests
[] Up the project in a online server

Any problems during the development aplication:
  1 - When the docker-compose was up, the connection between app and container was refused!
  Solution: The host option in the settings.py need be a name of database container
  2 - To create superadmin user when i run code script outside the container return an error!
  Solution: Enter in container docker to rum commands inside the container using a next script:
    - docker exec -it celero-challange_web_1 bash
    - python3 manage.py createsuperuser
  3 - Redundant solutions!
    - During the app development i found very intrestant for to access the database inside the db cointainer,
      using the pgadmin. But it's became unnecessary when i finish CRUD task, so i remove pgadmin.