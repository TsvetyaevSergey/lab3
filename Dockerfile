FROM python:3.11

WORKDIR app

COPY . .

ENV message simonov_roman

CMD ["python", "main.py"]