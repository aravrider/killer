# Dockerfile for CentOS with OpenJDK 11

This repository contains a Dockerfile to create a Docker image based on CentOS 7 with OpenJDK 11 installed. The image is designed to run Java applications.

## Prerequisites

- Docker installed on your machine. You can follow the instructions [here](https://docs.docker.com/get-docker/) to install Docker.

## Dockerfile Details

### Base Image

The Dockerfile uses the official CentOS 7 image as the base image.

### Environment Variables

The following environment variables are set to ensure the Java installation is recognized:

- `JAVA_HOME`: Specifies the location of the Java installation.
- `PATH`: Adds the Java `bin` directory to the system path.

### Installing OpenJDK 11

The `yum` package manager is used to update the system and install OpenJDK 11. After installation, the `yum clean all` command is used to remove cached data to reduce the image size.

### Verifying Java Installation

A command is run to verify that Java has been installed correctly.

### Working Directory

The working directory inside the container is set to `/app`.

### Copy Application Files

The Dockerfile includes a commented-out `COPY` instruction to copy your application files into the container. Adjust the source and destination paths as needed.

### Running the Application

The `CMD` instruction specifies the command to run your Java application. Replace `"your-application.jar"` with the name of your JAR file.

## Usage

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. Build the Docker image:

    ```bash
    docker build -t your-image-name .
    ```

    Replace `your-image-name` with your desired image name.

3. Run the Docker container:

    ```bash
    docker run -d --name your-container-name your-image-name
    ```

    Replace `your-container-name` with your desired container name and `your-image-name` with the name of the image you built.

## Example

### Build the Image

```bash
docker build -t my-java-app .
