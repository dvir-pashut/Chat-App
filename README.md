# Chat-App-DevOps Training
## Description
- Chat Service with rooms, built using Flask.
- Dockerized using python-slim image

## What is the Chat service?
The service exposes three apis:
1. `GET /<room>` - Will return the static HTML (provided to you), regardless of the room provided.
2. `POST /chat/<room>` - Accepts a chat line from a user:
   - Will accept 2 form fields - username & message.
   - Will save date, time, username & message per room.
3. `GET /chat/<room>` - Returns the full chat in a room:
   - Chat formatted as a list of "\n" delimited lines (1 per message).
   - Each line formatted according to the example: "[2018-02-25 14:00:51] omri: hi everybody!"



## How to run
- Make sure docker is installed
- Run init_app.sh
- Acess localhost:80

enjoy:) !



