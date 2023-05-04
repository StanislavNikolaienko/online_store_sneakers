## Online Store Django Project

This is a Django project that uses Docker and Docker Compose for easy development and deployment. The application uses
PostgreSQL as the database.

### Prerequisites

Before getting started, make sure you have the following software installed on your system:

* Docker: https://docs.docker.com/get-docker/
* Docker Compose: https://docs.docker.com/compose/install/

#### Setup

###### Clone the repository:

> git clone https://gitlab.com/Stas_ON/online_store_sneakers.git

##### Create a .env file in the project root directory with the following content:

> DATABASE_URL=postgres://postgres:123@localhost:5432/sneakers

##### Build and run the application :

> build the image from the source code:
>
>> docker build
>
>Run the application using Docker Compose:
>
>> docker-compose up
>
> Create a superuser in the Django application:
>> docker exec -it django_app python /python_docker/store/manage.py createsuperuser

This command will build your Django application container, start the PostgreSQL container, link them together and create
a superiser for access do Django Admin application. Your
Django application should now be able to connect to the PostgreSQL server.

Open your browser and navigate to http://localhost:8000. You should see your Django application running.
Stopping the Application
To stop the application, press Ctrl+C in the terminal where you ran docker-compose up. This will stop and remove the
containers.

> To stop the containers without removing them, press Ctrl+C and then run:
>
>> docker-compose down

##### Data Persistence

By default, the data in the PostgreSQL container will be lost when the container is removed. To persist the data, the
provided docker-compose.yml file includes a Docker volume called pgdata that stores the PostgreSQL data.

>If you need to remove the volume and start with a fresh database, run:
>
>>docker-compose down -v
