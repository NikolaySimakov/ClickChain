# API

## TODO

- [x] Link endpoint
- [ ] Statistics endpoint, clicks route
- [ ] auth

## Project structure

Files related to application are in the `app` or `tests` directories. Application parts are:

```
app
├── api - web related stuff.
│ ├── dependencies - dependencies for routes definition.
│ ├── errors - definition of error handlers.
│ └── routes - web routes.
├── core - application configuration, startup events, logging.
├── db - db related stuff.
│ ├── migrations - manually written alembic migrations.
│ └── repositories - all crud stuff.
├── models - pydantic models for this application.
│ ├── domain - main models that are used almost everywhere.
│ └── schemas - schemas for using in web routes.
├── resources - strings, enums, constants that are used in web responses.
├── services - logic that is not just crud related.
└── main.py - FastAPI application creation and configuration.
```

<!-- ├── models - pydantic models for this application.
│ ├── domain - main models that are used almost everywhere.
│ └── schemas - schemas for using in web routes. -->
