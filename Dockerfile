FROM python:3.8-alpine

# Install necessary utilities: procps for free and ps, util-linux for lsblk
RUN apk add --no-cache procps util-linux bash

# Create and set the working directory
RUN mkdir /app
ADD . /app
WORKDIR /app

# Run the Python script when the container starts
CMD ["python3", "app.py"]
