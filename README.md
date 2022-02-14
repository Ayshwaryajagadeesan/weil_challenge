# Challenge1: Develop The API


to invoke the pipfile environment

pipenv shell


to run the api 

python app.py


### Api Walkthough GIF

https://recordit.co/hLHYfMuqtu

* [x]  GIF of the challenge 1(REST API)in demonstration:


* [x]    I have developed a single REST API endpoint to return data from the database. The
API should be written in python3 (preferably 3.8, but flexible if there is a technical reason to do
so) and may use any python libraries that are readily available through pip. The endpoint should
accept a comma-separated list of IDs that will be used to look up corresponding Chart_Data
records. The data returned via the API should include the following columns:
- Chart_Data
- Id
- ChartTime
- ValueNum
- Error
- Warning
- Stopped
- Observation_Type
- Name
- Result_Status
- Name
- Unit_Of_Measure
- Name

Aside from the code itself, I also included:

* [x]  A requirements.txt file containing all of the libraries required to run the application 

* [x]   A script (e.g. bash or powershell) with a command to run the application

-  A script (e.g. bash or powershell) with a sample command (e.g. curl) to query the API

* [x]   A readme file describing how the code works and any design decisions you made along
with the rationale for those decisions

* [x] Any other scripts with useful commands that you find yourself using repeatedly during
development

# Challenge 2: Containerize the API
command To build docker image

<b>docker build . -t flask_app_dev</b>

command to run the docker image in debug environment

<b>docker run -p 5000:5000 -e DEBUG=1 flask_app_dev</b>

### Api Walkthough GIF

https://recordit.co/FSqNUyehzU


* [x] For this challenge, you will take the application from the previous challenge, build a docker
image from it, and run the application as a container using docker-compose.

* [x] The docker file should:

* [x]  be based on the python:3.8-slim-buster image unless there is a technical reason to use
another image (make sure you document your reasoning for this)

* [x] include only the files required to run the application

* [x]  not include the database

The docker-compose file should:
* [x]  mount the database

* [x]   expose the API on a different port from the container so that we can run them in
parallel on the same machine

* [x] In addition to the files from challenge 1, you should include:

* [x]  A script (e.g. bash or powershell) with a command to build the image

* [x]   Any other scripts with useful commands that you find yourself using repeatedly during


