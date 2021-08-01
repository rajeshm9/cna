# docker build --network=host -f docker/Dockerfile . -t cna:1.0
FROM python:3.8-slim-buster
WORKDIR /app
COPY src/ /app
RUN pip3 install -r requirements.txt
#flask run --host=0.0.0.0 --port=80

#CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
#EXPOSE 5000
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]