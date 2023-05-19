FROM python:3.9.7-alpine3.14

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt
EXPOSE 5000
CMD [ "python3", "app.py"]