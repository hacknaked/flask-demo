FROM python:2.7
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y \
      binutils \
      libproj-dev \
      gdal-bin \
      postgis

RUN mkdir -p /flask-demo
WORKDIR /flask-demo

# Copy requirements.txt first (avoid Docker rebuild when source code changes).
COPY requirements.txt /flask-demo/requirements.txt
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy the source code.
COPY . /flask-demo
