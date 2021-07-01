FROM python:3.7-slim
COPY . .
RUN pip install -r requirements.txt
RUN python manage.py migrate --settings=config.settings.prod
CMD ["python", "manage.py", "runserver", "0.0.0.0:80", "--settings=config.settings.prod", "--insecure"]
