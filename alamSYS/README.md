# ABOUT THIS PROJECT
This project aims to develop a RESTful API (alamAPI) for the Philippine Stock Market Price Trend Forecasting (PH-SMPTF) System, developed by John Markton M. Olarte, as part of his requirement for his bachelor's degree in Computer Science at the University of the Philippines - Visayas.


## About the alamAPI
### What is alamAPI?
### Features
alamAPI is a RESTful API that provides the following features:
- <b> API endpoints are publicly accessible. </b> 
Since the goal of the alamAPI is to provide an easy access to information about the forecasted market trend in the Philippine Stock Market and help Filipinos in their investment journey.
- <b> API endpoints are secured. </b> The main system (PH-SMPTF System) is physically isolated from the API endpoints. This is to ensure that the API endpoints are not accessible from the main system. This is to prevent the main system from being compromised by malicious users.
- <b> Easy to develop, use, and integrate. </b> Third-party developers can easily adopt the API workflow since it is simplified to only having 3 endpoints: (a) Stocks to Buy, (b) Stocks to Sell, and (c) Stock Info. Moreover, anyone may add additional features in the API easily as it uses fastAPI framework.


## About the Philippine Stock Market Price Trend Forecasting (PH-SMPTF) System
### What is PH-SMPTF System?
### Features
The features of the underlying system (PH-SMPTF System) is as follows:
1. <b>Dockerized source codes</b> allows it to be deployed on any system.
2. <b>Systems processes are automatic</b>, as it utilizes CRON scheduler.
3. <b>All processes are logged in the system</b>, which makes it easier to maintain the system.
4. <b>Scalable</b>, since this is an open source project anyone can add additional features within the system
to make it better and more useable for their own specific use cases.
5. <b>At the core of the system it utilizes Machine Learning based on the Dynamic Mode Decomposition</b>, however other developers may add additional models or trading algorithms that the system can use, which in turn can automate their own trade/investing workflow.


# HOW TO RUN THE PROJECT

## FOR UNIT DEVELOPMENT/TESTING
For project development and testing, you can run the project using the following steps:
### Requirements
- Python 3.8.5
- Docker
- Docker Compose
- For Windows users, you need to install WSL2 and Ubuntu 20.04 LTS
### Clone the project
```
git clone <project_url>
```
### Install Python Virtual Environment
Do this on the root directory of the project
```bash
pip3 install virtualenv
```
### Create a virtual environment
```bash
virtualenv venv
```
### Activate the virtual environment
```bash
source venv/bin/activate
```
### From the virtual environment, install the project dependencies
```bash
# cd to the project root directory
cd src
# cd to desired module (API_DB_module or preprocessor)
cd <desired-module>
# install the dependencies
pip3 install -r requirements.txt
```

## FOR DEPLOYMENT (on local area network)
For deployment on a local area network, the following steps are required:
### Requirements
- Docker
- Docker Compose
### Prerequisites
- Clone the repository
- cd into the repository
- Create a .env file in the root directory of the repository, use the .env.example file as a reference
### Steps
1. From the root directory (src). Build the Docker Images for the alamAPI, PH-SMPTF System, and the Database (MongoDB) using the following commands:
```bash
docker-compose build
```
2. Run the Docker Containers for the alamAPI, PH-SMPTF System, and the Database (MongoDB) using the following commands:
```bash
docker-compose up
```
### Notes
- You may deploy this on a local server or a cloud server, however, the alamAPI is not yet fully secured (e.g. DoS attacks), so it is not recommended to deploy this on a public server.
- For cloud deployment, you may use any cloud service provider that supports Docker, such as AWS, Azure, Google Cloud, etc.
- The alamAPI is accessible at http://localhost:8000, you may access the API over WAN by using the IP address of the host device where the alamAPI is deployed.
- The PH-SMPTF System is accessible is not accesible on any port, you may use docker cli using the host device to access the container and its connected volumes for debugging and maintenance purposes.
- PH-SMPTF System is automatically scheduled to run every 6PM from Mondays to Fridays. However, you may need to manually update the forecasting model which can be done using the docker cli.