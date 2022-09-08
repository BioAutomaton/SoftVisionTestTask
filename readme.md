To build using Docker:
1. cd into project root
2. execute "docker build --tag soft-vision ."
3. execute "docker run --name test-task -p 8000:8000 soft-vision"

**Test task API.**

Postman collection: https://www.getpostman.com/collections/479691f27625a095713f

Requirements:

Part 1.
1. Create FastAPI base project
2. Create User model (id, name, age(min=0, max=100), email)
3. Create Game model (id, name)
4. Create Endpoints:
   - Get games (get list of all games and users who connected to these games)
   - Get me (get info about current user and info about all connected games)
   - Connect to game. Create one object like User - Game.

Part 2 (Advanced).
1. Use SQLAlchemy to store your models
2. Use docker to run your code
