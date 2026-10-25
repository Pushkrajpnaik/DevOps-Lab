# Assignment 10: Docker Volumes & Data Persistence

## Objective
To demonstrate persistent storage using Docker named volumes.

## Files
- app.py: Flask application that writes timestamped greetings to a log file.
- requirements.txt: Flask dependency.
- Dockerfile: Builds the application image and exposes port 5001.

## Implementation
1. Created the Flask application with `/` and `/logs` routes.
2. Built the Docker image `my-flask-app:v2`.
3. Created the named volume `my-app-data`.
4. Ran `flask-volume-demo` with the volume mounted at `/app/data`.
5. Accessed the application repeatedly to create log entries.
6. Stopped and removed the first container.
7. Started `flask-volume-demo2` using the same volume.
8. Verified that the previous log entries were preserved.

## Verification
Command: `curl http://localhost:8082/logs`

Result: Previously written timestamped log entries remained available after the original container was removed.

## Conclusion
Docker named volumes preserve application data independently of a container's lifecycle.
