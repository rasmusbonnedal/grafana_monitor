# Grafana Sensor Logger and Visualizer

This repo is a docker-compose setup for a Grafana/MariaDB/Python logger which
stores data from temperature and humdity sensors in a database for display
in a Grafana instance.

![image](https://user-images.githubusercontent.com/4532327/175360346-45d0dc20-a96d-47c7-b205-59579d755e4d.png)

## Directory layout
* [grafana](grafana) - Grafana Docker setup with sensor visualization dashboard.
* [mariadb](mariadb) - MariaDB Docker setup which initializes a db for sensor
storage.
* [temp-producer](temp-producer) - Python Docker which currently produces random
log data and stores in db.

## Running
```$ docker-compose up```

When the system is running, connect to http://localhost:9000/ and select "Last
5 minutes" to see test data.
