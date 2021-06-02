FROM python:3.7-slim-buster
WORKDIR /app
COPY . /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 80

CMD [ "python", "./app.py" ]