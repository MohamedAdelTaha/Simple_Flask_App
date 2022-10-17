FROM python:latest

WORKDIR /app 

COPY requirements.txt .  

RUN pip install -r requirements.txt 

COPY flask_hello.py . 

EXPOSE 5000  

CMD python flask_hello.py 