# DualEntry Test app

Given the task main goal is to create API that allows to retrieve users managed by WorkOs and there is no other user story, 
I decided to not burden the app with persisting local copy of the data and instead to use WorkOs API directly.
It's a simple proxy app that forwards requests to WorkOs API and returns the response. 
There are no additional features like caching, monitoring, etc. However, cashing would be the first feature to add in case of further development.

Obvious downside of this approach is that the app is dependent on WorkOs API availability and performance.
My assumption is that WorkOs API is reliable and fast enough to be used directly (1,000 requests per 10 seconds sounds ok for a startup phase project).
The main advantage is that the app is simple and easy to maintain, and MVP was delivered quickly.

Yes, I leaked the API key to the repo on purpose. It should be moved to AWS SSM or similar.

Despite DualEntry uses Django, I have decided to use FastAPI. Main reason was that I have much more experience with it and I already had my personal boilerplate for it. 
Yet again, delivery speed won. 

Hexagonal Architecture is something I'm used to, so I followed the pattern even tho it's a bit overkill given the lack of the tests that replace adapters using interface in ports. 

## Development setup

Requirements:

-   Python 3.12+
-   Poetry

Installation:
-   `make init` //warning: api key pushed to repo, should be moved i.e. to AWS SSM 
- replace `WORKOS_API_KEY` and `WORKOS_CLIENT_ID` in `.env` with your own WorkOs credentials or use provided instance in dist 
-   `make build`
-   to set up Python env for IDE to work properly, run `poetry install` from main directory

Running project:

-  `make run`

Running project exposes Swagger interface at http://localhost:8008/docs





