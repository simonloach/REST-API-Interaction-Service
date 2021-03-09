# Task for Collabera recruitment
I have created a Python script(mac_get_manufacturer.py) that sends request to the API of https://macaddress.io/ in order to retrieve manufacturer from the given MAC Address.

The program returns the manufacturer without any additional comments, so the stdout can be used directly.

## Requirements
- Docker
- Git


## Instalation
1. ```bash
   git clone https://github.com/simonloach/TaskCollabera.git && cd TaskCollabera
   ```
2. ```bash
   docker build -t collabera:latest .
   ```
3. ```bash
   docker run collabera get_manufacturer <MAC_ADDRESS>
   ```
