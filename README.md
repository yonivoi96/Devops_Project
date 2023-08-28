# Devops_Project

In this project I've deployed a web app to present your IP.

The app is based on Python and Flask framework.

Every time some code is being pushed into the repository, a CI pipleine implemented with github actions is being triggered.

## The pipeline:
1. At the first step, all the requirements that are needed for this app and placed in the requirements.txt are being installed.

2. At the next step, some unit tests are triggered to test the functionallity of the program and the coverage of the tests are presented.

3. Next, we perform a login to docker hub that is needed for the next step (credentials are stored in the repository's secrets).

4. Now, using the bash script build_my_image we build the Docker image and push it to docker hub 

5. Lastly, an email is sent to my personal account reporting the build is over and if it succeeded or failed.

### Dockerfile

Inside this Dockerfile we make sure we have our app's code and the requirements file.

We then install the requirements, expose port 5000 and set an environment variable for the flask app.

And finally we trigger the web application.

### build_my_image.sh

This is a bash shell script that builds our image using the Dockerfile and uploads it to Docker Hub to my user's (yonatanv96) repository (project_dev).