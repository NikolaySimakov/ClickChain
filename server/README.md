# Server

Link shortener api written in FastAPI.

## Usage

Rename `.env.example` to `.env` and change variables.

### Run app:

Install deps:

```bash
pip install -r requirements.txt
```

Update migrations:

```bash
alembic upgrade +1
```

Run app manually:

```bash
cd server
python src/app.py
```

To create migrations folder:

```bash
alembic init -t async migrations
```

## TODO

- [x] Link endpoint
- [x] Statistics endpoint, clicks route
- [ ] Basic statistics
- [ ] Auth

## Project structure

Files related to application are in the `src` or `tests` directories. Application parts are:

```md
src
├── api - web related stuff.
│ ├── dependencies - dependencies for routes definition.
│ ├── errors - definition of error handlers.
│ └── routes - web routes.
├── core - application configuration, startup events, logging.
├── db - db related stuff.
│ ├── migrations - manually written alembic migrations.
│ └── repositories - all crud stuff.
├── schemas - schemas for using in web routes.
├── resources - strings, enums, constants that are used in web responses.
├── services - logic that is not just crud related.
└── main.py - FastAPI application creation and configuration.
```

<!-- ├── models - pydantic models for this application.
│ ├── domain - main models that are used almost everywhere.
│ └── schemas - schemas for using in web routes. -->
