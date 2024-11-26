FROM python:3.12

RUN apt update -y && apt upgrade -y && \
    apt-get install -y poppler-utils && \
    rm -rf /var/lib/apt/lists/*
#    apt-get install -y mariadb-server && \

WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .
# COPY ./requirements.txt /app/requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt
# RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Based on how Uvicorn works, /app/src will become /app in Docker container
COPY ./app ./app

# COPY entrypoint.sh /
# ENTRYPOINT ["bash", "/entrypoint.sh"]

# Command to run the FastAPI application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]