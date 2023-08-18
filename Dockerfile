#Create a ubuntu base image with python 3 installed.
FROM python:3.10

#Set the working directory
WORKDIR /app

#copy all the files
COPY . .

#Install the dependencies
RUN apt-get -y update
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install -r requirements.txt

#Run the command
CMD ["uwsgi", "app.ini"]