
FROM python:3.10.4


WORKDIR /code



COPY ./requirements.txt /code/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


COPY ./api.py /code/api.py


CMD ["fastapi", "run", "api.py", "--port", "8090"]
