To run network
```
docker-compose -p docbrowse up --build
```
To inspect database, go to PGAdmin at `localhost:8050`. To find out what address postgres is running on, do
```
docker network inspect docbrowse_default
```
and find the IPv4Address for the database container.