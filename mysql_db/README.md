Running MySQL Using Docker 🐳📊
In this project, we will deploy a MySQL database using Docker, a powerful platform for containerizing applications. Docker ensures that your database is portable, scalable, and independent of the underlying system. This guide will walk you through the process of setting up a MySQL database inside a Docker container, initializing it with a sample dataset, and interacting with it using SQL queries.

By the end of this tutorial, you will have a fully functional MySQL database running inside a Docker container, ready for development or production use. 🚀

Project Overview 📖
This project demonstrates how to containerize a MySQL database using Docker. The database is initialized with a sample schema and data, allowing you to interact with it using SQL queries. The setup is ideal for development, testing, or even production environments where portability and scalability are critical.

Documentation 📚
For more information, refer to the official documentation:

Docker Documentation
MySQL Documentation
Docker Desktop Documentation
Prerequisites 📋
Before we begin, ensure you have the following installed on your system:

Docker: A platform for developing, shipping, and running applications in containers.
Docker Desktop: A tool to manage Docker containers on your local machine.
Installation and Setup 🛠️
Step 1: Verify Docker Installation
Run the following command in your terminal to check if Docker is installed:

docker --version
You should see an output similar to:

Docker version 20.10.17, build 100c701
Project Structure 🗂️
The project consists of the following files:

database_students.sql: A SQL script to create a database and insert sample data.
Dockerfile: A script containing instructions for Docker to build an image.
Create the SQL Script 📄
The database_students.sql file contains the SQL commands to create a database and insert sample data. Below is the content of the file:

CREATE DATABASE student;
USE student;

CREATE TABLE students (
    StudentID INT NOT NULL AUTO_INCREMENT,
    FirstName VARCHAR(100) NOT NULL,
    Surname VARCHAR(100) NOT NULL,
    PRIMARY KEY (StudentID)
);

INSERT INTO students (FirstName, Surname)
VALUES ("John", "Andersen"), ("Emma", "Smith");
Explanation of the SQL Script:

CREATE DATABASE student;: Creates a new database named student.
USE student;: Switches to the student database.
CREATE TABLE students (...);: Creates a table named students with columns StudentID, FirstName, and Surname.
INSERT INTO students (...);: Inserts sample data into the students table.
Dockerfile 📄
The Dockerfile is a script that contains instructions for Docker to build an image. Below is the Dockerfile for this project:

# Use the official MySQL image as the base image
FROM mysql:latest

# Set the root password for MySQL
ENV MYSQL_ROOT_PASSWORD=root

# Copy the SQL script to initialize the database
COPY ./database_students.sql /docker-entrypoint-initdb.d/
Explanation of the Dockerfile:

FROM mysql:latest: Specifies the base image (official MySQL image).
ENV MYSQL_ROOT_PASSWORD=root: Sets the root password for MySQL.
COPY ./database_students.sql /docker-entrypoint-initdb.d/: Copies the SQL script to the docker-entrypoint-initdb.d directory, which automatically executes the script when the container starts.
Deployment 🚀
Step 1: Build the Docker Image

Navigate to the directory containing the Dockerfile and run the following command:

docker build -t mysql_db .
The -t flag tags the image with the name mysql_db.
The . specifies the build context (current directory). Step 2: Verify the Docker Image
Run the following command to list all Docker images:

docker images
You should see an output similar to:

REPOSITORY   TAG       IMAGE ID       CREATED          SIZE
mysql_db     latest    abc123def456   10 seconds ago   500MB
Step 3: Run the Docker Container

Start the Docker container using the following command:

docker run -d --name mysql_container mysql_db
The -d flag runs the container in detached mode.
The --name flag assigns a name (mysql_container) to the container. Step 4: Access the MySQL Container
To interact with the MySQL database, access the container's shell:

docker exec -it mysql_container /bin/bash
Step 5: Connect to MySQL

Connect to the MySQL server using the following command:

mysql -u root -p
Enter the root password (root) when prompted. Step 6: Query the Database
Switch to the student database and query the students table:

USE student;
SELECT * FROM students;
You should see the following output:

+-----------+-----------+----------+
| StudentID | FirstName | Surname  |
+-----------+-----------+----------+
|         1 | John      | Andersen |
|         2 | Emma      | Smith    |
+-----------+-----------+----------+
Conclusion 🎉
Congratulations! 🎉 You’ve successfully deployed a MySQL database using Docker. This setup ensures that your database is portable, scalable, and independent of the underlying system. Docker and MySQL together provide a powerful combination for building and deploying database-driven applications.

Keep exploring and building more complex applications with Docker and MySQL! 🚀📊

Happy coding! 💻✨
