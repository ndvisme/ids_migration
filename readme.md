# Migrator
A tool for updating `app_instance_ids` in our Postgres DB

## Prerequisites
- Ensure you have Docker installed

## How to Run

1. **Build the Docker Image**
```bash
docker build -t migrator .
```
2. ** Run the Container
```bash
docker run migrator:latest
```
3. ** Run the App Interactively
```bash
docker run -it migrator::latest python main.py
```

## How to Test
1. **Run All Tests**
```bash
docker run migrator:latest pytest tests/
```
