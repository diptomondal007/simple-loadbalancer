FROM python:3

RUN pip install flask
RUN pip install requests

COPY app.py /app/app.py

CMD ["python", "/app/app.py"]