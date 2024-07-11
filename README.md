# Python Server

This project contains a FastAPI server implemented in Python. It provides two routes for managing a task list.

## Project Structure

The project has the following files and directories:

- `src/main.py`: This file contains the implementation of the FastAPI server with two routes. It handles adding a task to a list and retrieving the list.

- `src/__init__.py`: This file is an empty file that marks the `src` directory as a Python package.

- `requirements.txt`: This file lists the dependencies required for the FastAPI server and other dependencies.

- `Dockerfile`: This file is used to build a Docker image for the FastAPI server. It specifies the base image, copies the source code into the image, installs the dependencies, and sets the command to run the server.

- `docker-compose.yml`: This file is used to define and run multi-container Docker applications. It specifies the services to run, their configurations, and any dependencies between them.

## Getting Started

To run the FastAPI server using Docker, follow these steps:

1. Make sure you have Docker installed on your machine.

2. Clone this repository.

3. Navigate to the `python-server` directory.

4. Build the Docker image by running the following command:

   ```shell
   docker build -t python-server .
   ```

5. Start the Docker containers by running the following command:

   ```shell
   docker-compose up
   ```

6. The FastAPI server should now be running. You can access it at `http://localhost:8000`.

## API Routes

The FastAPI server provides the following API routes:

- `POST /tasks`: Adds a task to the task list. The request body should contain the task details.

- `GET /tasks`: Retrieves the task list.

Please refer to the API documentation for more details on the request and response formats.

## Dependencies

The FastAPI server has the following dependencies:

- FastAPI: A modern, fast (high-performance) web framework for building APIs with Python.

- Other dependencies listed in the `requirements.txt` file.

```
This README.md file provides an overview of the project structure, instructions for running the server using Docker, information about the API routes, and the dependencies used in the project.