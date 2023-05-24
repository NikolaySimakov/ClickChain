# API

## Usage

```
$ cd server
$ python src/app.py
```

## Requirements

- alembic 1.8.1
- fastapi 0.85.0
- hashids 1.3.1
- SQLAlchemy 1.4.41
- uvicorn 0.18.3
- pytest 5.3.5

## TODO

- [x] Link endpoint
- [ ] Statistics endpoint, clicks route
- [ ] Auth

## Project structure

Files related to application are in the `src` or `tests` directories. Application parts are:

```
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
