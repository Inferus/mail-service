# Email Microservice

This repository contains a Dockerized FastAPI-based email microservice that sends emails via SMTP. The microservice is designed to be part of a larger system that communicates with an Elasticsearch cluster for logging or other purposes.

## Features

- **Send Emails**: Uses SMTP to send emails.
- **Error Handling**: Logs errors and raises HTTP exceptions if sending fails.

## Getting Started

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/) (version 20.10 or later)
- [Docker Compose](https://docs.docker.com/compose/install/) (version 1.27 or later)

### Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Inferus/mail-service.git
   cd mail-service
   docker-compose up --build
