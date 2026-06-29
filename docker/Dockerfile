#use a base image

FROM python:3.11-slim

#set the working directory

WORKDIR /app

#copy the files from the host to the container

COPY requirements.txt service/ ./

#install dependencies

RUN pip install --no-cache-dir -r requirements.txt

#Expose ports

EXPOSE 5000

#define the command to run the application

CMD ["python", "app.py"]

