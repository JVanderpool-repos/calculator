FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

# Install additional system dependencies if needed
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
        # Add any additional system packages here
        build-essential \
        curl \
        git \
    && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/*

# Set Python environment variables
ENV PYTHONPATH=/workspaces/calculator
ENV PYTHONUNBUFFERED=1

# Create a non-root user
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Set up the working directory
WORKDIR /workspaces/calculator

# Install Python dependencies will be handled by postCreateCommand
# This keeps the container build fast and allows for easy dependency updates