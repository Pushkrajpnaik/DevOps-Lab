# Assignment 10: Docker Volumes and Data Persistence

## Objective
To demonstrate persistent data storage using a Docker named volume.

## Procedure
1. Created a named volume called `devops-data`.
2. Mounted the volume at `/data` in a temporary Alpine Linux container.
3. Created `message.txt` containing a test message.
4. Removed the container without deleting the volume.
5. Mounted the same volume in a new container and read the file.
6. Inspected the volume using Docker CLI commands.

## Result
Successfully verified that data persisted after the original container was removed.
