# Use an official CentOS as a parent image
FROM centos:7

# Set environment variables for Java installation
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk
ENV PATH $JAVA_HOME/bin:$PATH

# Install OpenJDK 11
RUN yum update -y && \
    yum install -y java-11-openjdk-devel && \
    yum clean all

# Verify Java installation
RUN java -version

# Set the working directory
WORKDIR /app

# Copy your application files (if any) to the container
# COPY . /app

# Command to run your application (if any)
 CMD ["java", "-jar", "your-application.jar"]
