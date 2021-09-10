# eIQ Mobility SWE Take-Home Assignment

This repository includes instructions for the eIQ Mobility take home assignment.

## SWE Take-Home Assignment

A simple Flask-Kubernetes-Docker web application that allows the user to upload a .CSV file. On successful file upload, the application should perform the following validations:

* Checks whether the uploaded is a .CSV and not any other format.
* Check whether the .CSV file has exactly 10 rows and 3 columns.
* Checks whether the data is present in each cell (.CSV file is "complete"). A "complete" sample test.csv is available in this repository for testing purposes.

## Links
- [DockerHub](https://hub.docker.com/r/crypticwoodwhite/eiqmobility_takehome_backend)
- [Github](https://github.com/CrypticWoodWhite/eiqmobility_takehome_backend)
## Commands

1. `docker build [OPTIONS] PATH | URL | -`
  - this builds a docker image using instructions found in the Dockerfile and the context. The context consists of the files found at the specified `PATH` or `URL`.
  - so for this app we're using `docker build -f Dockerfile https://github.com/CrypticWoodWhite/eiqmobility_takehome_backend.git#master`

2. `docker push [OPTIONS] NAME[:TAG]`
  - this command pushes a docker image or a repo to a registry such as Docker Hub, same idea as the `git push` command
  - before using the `push` command, we have to commit the image and tag it appropriately.
  - here we're using `docker push crypticwoodwhite/eiqmobility_takehome_backend:initial`