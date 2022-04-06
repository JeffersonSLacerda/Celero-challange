# Celero-challange
This project is a challange to work in a Celero Team

List with all activites:

[X] Create a Athlete model 
[X] Make a CRUD to Athletes
  [X] GET
  [X] POST
  [X] PATCH
  [X] DELETE
[X] Implements a Postgres Database
[X] Up application and database using Docker
  [X] Add portrainer to monitor logs and interage with individual containers
[X] Run a routine to populate database based on csv file
  [X] Improved performance by bulk insert

[] Make some filters - need more details
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
  4 - How long is this going to take?
    - When i run the script to add the data in csv file one thing, make me sad, the thime it took to run, about 45 minutes,so i decide reduce a little bit, and using bulk and alocate of data in arrays, i can reduce this time to a little less than a minute.

executing this project step by step:
- pre reques: docker and docker-compose, I recommend up this application on WSL2, this is very importante to performance and development
- git clone https://github.com/JeffersonSLacerda/Celero-challange.git
- run: python3 -m venv venv 
- start the venv: souce venv/bin/activate
- build and up the containers: docker-compose up -d --build
- verify your containers is allredy, access: localhost:9000 - in the first access to need set a user and password, remember that.
- verify if you app is runing, access: localhost:8000
- run migrations inside the container with the following command: docker exec celero-challange_web_1 python3 manage.py migrate
- access localhost:8000/athletes to verify if everythind was done
- now populate the database using a csv file, use: docker exec celero-challange_web_1 python3 manage.py runscript populate --script-args ./data/athlete_events.csv
- refresh the page localhost:8000/athletes to verify if all it's ok
- in this page you can see all athletes and create a new one
- use localhost:8080/athlete/:id to access only athlete register, here it's possible edit or delete this data
