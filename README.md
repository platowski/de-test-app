# DualEntry Test app

## Development setup

Requirements:

-   Python 3.10+
-   Poetry

Installation:
-   `make init` //warning: api key pushed to repo, should be moved i.e. to AWS SSM
-   `make build`
-   to set up Python env for IDE to work properly, run `poetry install` from main directory

Running project:

-  `make run`

Running project exposes Swagger interface at http://localhost:8008/docs


