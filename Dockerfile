FROM python:3.10.0
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
COPY ./app/controllers /code/app/controllers
COPY ./app/models /code/app/models
COPY ./app/data /code/app/data
COPY ./app/img /code/app/img
COPY ./app/pages /code/app/pages
COPY ./app/utils /code/app/utils
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]