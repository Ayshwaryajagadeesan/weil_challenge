# Challenge1: completed user stories

to run the api 


pipenv shell

to invoke the pipfile environment

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

# Challenge 2:
command To build docker image

<b>docker build . -t flask_app_dev</b>

command to run the docker image in debug environment

<b>docker run -p 5000:5000 -e DEBUG=1 flask_app_dev</b>

