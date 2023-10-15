FROM python:3.11

WORKDIR app

COPY . .

ENV message 100

CMD ["python", "main.py"]