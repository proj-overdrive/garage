# garage

A database for parkade.

Docker compose is used to start a Postgres database and apply any pending migrations,
using [Flyway](https://flywaydb.org/). The goal being to use the same database migrations locally
and in the cloud.

Database migrations are defined in the [migrations](/migrations) directory. Migrations
are applied in order, based on version number. Each new migration should use the next sequence
number. For example, the first migration is named `V1__Create_tables.sql`, so the next
migration would begin with a prefix of `V2__`.

## Running the database

Scripts are provided to start, stop, and delete the local database. The database persists state in local
files that remain across starts and stops, using a docker volume (named `garage_db`). Note, you can list
docker volumes using the `docker volume ls` command. Deleting the database will cause all migrations to 
be run on the next start.

To start the local database and apply and pending migrations, run the following shell script
from the `db-tracks` directory.

```shell
./start-db.sh
```

To stop the local database:

```shell
./stop-db.sh
```

To delete the local database:

```shell
./delete-db.sh
```

## Connecting to the database

### Within docker

The database is run as a container using docker compose, on the default network (named `garage_default`)
Note, you can list docker networks using the `docker network ls` command.

### Externally
The database container exposes port `5432` locally. An application launched from the command line can
connect to the database at `localhost:5432`.

## Seeding the database

The utility to seed the database requires Make and Python. Make is included with XCode.

To seed the local database with random test data (spots):

1. Start the database from the `garage` directory.
    ```shell
    ./start-db.sh
    ```
 
1. Run the following command from the `garage` directory.

    ```shell
    make init-spots
    ```

This executes a Python program that inserts random test data into the database.
