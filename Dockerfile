#Python image to use
FROM python:3.9-slim

ENV PYTHONUNBUFFERED True

#copy the local code
ENV APP_HOME /app 
WORKDIR $APP_HOME
COPY . ./

#install all required package 
RUN pip install -r requirements.txt

#Run web service using gunicorn
CMD exec gunicorn -b-bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
