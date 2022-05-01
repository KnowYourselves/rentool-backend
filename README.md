# Backend

## Editor Tooling

To activate the text editor tooling, I recommend to use a local virtual environment.

```sh
python3 -m virtualenv .venv

. .venv/bin/activate

poetry install
```

Use the interpreter from the `.venv` folder inside `vscode` to have all the necessary tooling.

## Docker Usage

To use Docker correctly, you need to first build the project:

```sh
docker compose build
```

Run this command every time you add or remove a Python dependency.

To run commands inside the container, run:

```sh
docker compose run web <command>
```

Keep in mind that you're using a containerized database on development, so you need to run migrations and stuff like that through Docker.

To start the server, run the following command:

```sh
docker compose up
```

## Heroku Deployment

To deploy to Heroku, use the following commands:

```sh
heroku container:push web
heroku container:release web
```

Notice that in Heroku the application will use a provisioned database, so don't forget to add a PostgresQL database to the Heroku application.
