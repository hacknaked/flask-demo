# flask-demo
A small start project for Flask and Docker.

## Prerequisites

Requires Docker Engine 1.10+ and Docker Compose 1.6+

## Clone, setup and run

1. Clone the repo
```
$ https://github.com/hacknaked/flask-demo.git
$ cd flask-demo
```

1. Build Docker containers
```
$ docker-compose build
```

1. (optional, first time only) Start the database service in first place 
in order to build the database, tables, schemas into disk.
 
```
$ docker-compose start postgresql
```
1. Start all services

```
$ docker-compose up
```
1. Try

Open a browser and go to http://0.0.0.0:5000  


