# Assignment 9: Container Management and Networking

## Objective
To create and inspect a custom Docker network and verify communication between containers.

## Procedure
1. Created a custom bridge network named `devops-network`.
2. Started an Nginx container named `web-container`.
3. Started a Python container named `test-container`.
4. Connected both containers to the same Docker network.
5. Tested communication using Python's urllib module and the hostname `web-container`.

## Verification
Command:
`docker exec test-container python -c "import urllib.request; print(urllib.request.urlopen('http://web-container', timeout=5).status)"`

Expected output: `200`

Both containers were verified as running on `devops-network`.

## Result
Successfully established communication between two Docker containers using a custom network and Docker's internal DNS.
