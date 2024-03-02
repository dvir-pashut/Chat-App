FROM python:3.13.0a4-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app


# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000


# #Run the database module
# CMD [ "python", "dbconnection.py" ]

# Run app.py when the container launches
ENTRYPOINT [ "python", "app.py"]
