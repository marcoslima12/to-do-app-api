# DO IT - API

## Running de project

1. Clone de repository by running
   ```bash
   https://github.com/marcoslima12/to-do-app-api.git
   
2. Create a .env and cpoy the following content to it:
   
     ```.env
      # environment variables
      POSTGRES_USER=user01
      POSTGRES_PASSWORD=pass01
      POSTGRES_DB=tododatabase
     ```

3. To run the development server, run
   ````bash
       docker-compose up --build
  If you are using Linux, make sure to use 
  ```bash
sudo docker compose up --build
