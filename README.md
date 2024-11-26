# Setup env

- Create venv environment to install packages: `python -m venv .venv`
- Activate local environment, run this command: `. .venv/bin/activate`
- Install pacakge: `pip install -r requirements.txt`


## env variables
- Copy file `.env.example` to  `.env` and edit information inside

## Run project locally
- Then go to /src folder and run this command: `python -m uvicorn app.main:app --reload --port 8000`
- Go to `http://localhost:8000/docs` to access swagger api list.

## Run in docker
- Update `docker-compose.yml` if needed
- Run this command: `docker-compose up --build`
- Go to `http://localhost:8000/docs` to access swagger api list.

