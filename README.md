# Discord Flask API

Minimal Docker container with Discord API implemented using Flask for some queries of my personal website. I will probably add more routes in the API as needed.

### Setup

```docker
docker build -t discord-flask-api .
docker run -d -p 5007:5007 discord-flask-api 
```
