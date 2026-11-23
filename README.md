# Project 08: Build and Run a Docker App Locally

A small Python web app with no third-party dependencies. The homepage shows the
container hostname, and `/health` returns a JSON health status.

## Build and run

From this directory, run:

```powershell
docker build -t project-08 .
docker run --rm -d --name project-08-app -p 8000:8000 project-08
```

Open [http://localhost:8000](http://localhost:8000) in a browser. Verify the
health endpoint at [http://localhost:8000/health](http://localhost:8000/health).
The hostname shown on the homepage confirms the app is running in its container.

To stop the app:

```powershell
docker stop project-08-app
```

## Deliverable screenshot

After starting the container, open the homepage and capture a screenshot showing
the app and its container hostname. Include the successful `docker build` and
`docker run` output in the submission if your assessment expects terminal proof.

## Run without Docker

```powershell
python app.py
```

Then open `http://localhost:8000`.

## Tests

```powershell
python -m unittest
```
