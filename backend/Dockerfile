FROM python:3.12
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /code/app
COPY backend/requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY . /code/app/.
ENV PYTHONPATH "/code/app"