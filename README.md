# REST API by FastAPI 


This is a RESTful API written in FastAPI with two POST request. The entire application is contained in the `pool_api` directory.

A full interactive Docs UI can be checked  at http://localhost:8000/docs once you run the server with `uvicorn` , courtesy of Swagger UI and OpenAPI. The app is not connected to any database for the simplicity purpose, but based on `data.csv` file, which stimulate a database, to implement all the operations. 


## Install


    cd pool_api
    pip3 install -r requirments.txt

## Run the App

    uvicorn main:app --reload


## Rest API Documentations

    open docs.pdf
