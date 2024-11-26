# Setup env

- Create venv environment to install packages: python -m venv .venv 
- Activate local environment, run this command: . .venv/bin/activate
- Install pacakge: pip install -r requirements.txt


## env variables
- Copy file .env.example to  src/.env and edit information inside

## Project config


## Run code locally

- Then go to /src folder and run this command: `python -m uvicorn api:app --reload --port 8000`
- Go to http://localhost:8000/docs to access swagger api list.

## Run in docker
- Update docker-compose.yml if needed
- Run this command: `docker-compose up --build`
- Go to http://localhost:8888/docs to access swagger api list.

