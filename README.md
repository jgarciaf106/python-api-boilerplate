# WebApp boilerplate Flask API
[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io#https://github.com/jgarciaf106)

### Back-End Manual Installation:

It is recomended to install the backend first, make sure you have Python 3.8, Pipenv and a database engine (Posgress recomended)

1. Install the python packages: `$ pipenv install`
2. Create a .env file based on the .env.example: `$ cp .env.example .env`
3. Install your database engine and create your database, depending on your database you have to create a DATABASE_URL variable with one of the possible values, make sure yo replace the valudes with your database information:

| Engine	| DATABASE_URL 						|
| ------------- | ----------------------------------------------------- |
| Postgress	| postgres://username:password@localhost:5432/example 	|

4. Migrate the migrations: `$ pipenv run migrate` (skip if you have not made changes to the models on the `./src/api/models.py`)
5. Run the migrations: `$ pipenv run upgrade`
6. Run the application: `$ pipenv run start`


## Publish your website!

This boilerplate it's 100% integrated with Heroku, just by pushing your changes to the heroku repository it will deploy: `$ git push heroku main`
