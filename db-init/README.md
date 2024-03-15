# How to use this folder

1. Place .sql files containing schema or seed data in this folder
2. Configure db service in docker-compose to run script on container startup

    ```yaml
    services:
      db:
        volumes:
          - ./db-init:/docker-entrypoint-initdb.d
    ```
