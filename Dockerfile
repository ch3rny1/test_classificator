FROM python:3.8-slim 

COPY app ./

RUN python -m pip install -r requirements.txt

CMD python server.py
