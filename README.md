## Celero-challange
This project is a challange to join the Celero Team!
Enjoy It and I hope you can learn a lot! I really had fun and learned a lot from this project and appoint a little bit of my experience with that!

## Technology 

Here are the technologies used in this project.

* Django version  4.0.3
* Django Rest Frameword version 3.13.1
* PostgreSQL version 13
* Psycopg2 version 1.13
* Docker
* Docker-compose
* Portainer

## List with all activites:
To help me stay focused, i divide all project in little peaces and assinalete any one then here

- [X] Create a Athlete model 
- [X] Make a CRUD to Athletes
  - [X] GET
  - [X] POST
  - [X] PATCH
  - [X] DELETE
- [X] Implements a Postgres Database
- [X] Up application and database using Docker
  - [X] Add portrainer to monitor logs and interage with individual containers
- [X] Run a routine to populate database based on csv file
  - [X] Improved performance by bulk insert

- [ ] Make some filters - need more details
- [ ] Unitary tests
- [ ] Up the project in a online server

## Getting started
### Clone application using a following command: 
$ git clone <https://github.com/JeffersonSLacerda/Celero-challange.git>

### Create a virtual enviroment: 
$ python3 -m venv venv 

### Start the venv: 
$ souce venv/bin/activate

### Build and up the containers:
$ docker-compose up -d --build

### Verify your containers is allredy, access: 
 <http://localhost:9000> - in the first access to need set a user and password.
 ![Portainer Access](https://github.com/JeffersonSLacerda/Celero-challange/blob/main/data/readme/passo5.1.jpeg)
 ![Portainer Access](https://github.com/JeffersonSLacerda/Celero-challange/blob/main/data/readme/passo5.2.jpeg)
 
### Verify if you app is runing: 
<http://localhost:8000>
![First Access](https://github.com/JeffersonSLacerda/Celero-challange/blob/main/data/readme/passo6.jpeg)

### Run migrations inside the container with the following command: 
$ docker exec celero-challange_web_1 python3 manage.py migrate

### Access <http://localhost:8000/athletes> to verify if everythind was done
 ![Athlete Access](https://github.com/JeffersonSLacerda/Celero-challange/blob/main/data/readme/passo8.jpeg)

### Now populate the database using a csv file, use: 
$ docker exec celero-challange_web_1 python3 manage.py runscript populate --script-args ./data/athlete_events.csv

### Refresh the page localhost:8000/athletes to verify if all it's ok
- In this page you can see all athletes and create a new one
 ![Show Athlete](https://github.com/JeffersonSLacerda/Celero-challange/blob/main/data/readme/passo9.jpeg)

### Use <http://localhost:8080/athlete/:id> to access only athlete register, here it's possible edit or delete this data
 ![Athlete Data](https://github.com/JeffersonSLacerda/Celero-challange/blob/main/data/readme/passo11.jpeg)


## Any problems during the development aplication:
  1. When the docker-compose was up, the connection between app and container was refused!
  * Solution: The host option in the settings.py need be a name of database container
  2. To create superadmin user when i run code script outside the container return an error!
  * Solution: Enter in container docker to rum commands inside the container using a next script:
    - docker exec -it celero-challange_web_1 bash
    - python3 manage.py createsuperuser
  3. Redundant technologies!
  * During the app development i found very intrestant for to access the database inside the db cointainer, use the pgadmin. But it's became unnecessary when i finish CRUD task, so i remove it.
  4. How long is this going to take?
  * When i run the script to add the data in csv file one thing make me sad, the thime it took to run, about 45 minutes. So i decide reduce a little bit, and using bulk and alocate of data in arrays, i can reduce this time to a little less than a minute.
