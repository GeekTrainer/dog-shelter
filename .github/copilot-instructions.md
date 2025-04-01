# Dog shelter

This application is built to support people wanting to adopt dogs from a shelter. It's a mono-repo with a client and server.

## Client

Client is built with the following technologies:

- TypeScript
- Astro for routing and hosting
- Svelte for dynamic displays
- Tailwind to make it all look pretty

Client notes:

- UI should use dark mode, rounded corners, and have a modern feel

## Server

Server is written with:

- Python/Flask for the API
- SQLAlchemy as the ORM
- Unit tests written using unittest

Server testing notes

- Tests are required for the API
- All database calls should be mocked in tests
- When running tests, make sure to activate the virtual environment in venv (located in the root of the project)