FROM python:3.9-alpine

RUN apk add --no-cache \
    libgpiod \
    libgpiod-dev \
    build-base \
    python3-dev \
    py3-pip

RUN pip3 install gpiod

WORKDIR /app

COPY app.py .

CMD ["python3", "app.py"]
