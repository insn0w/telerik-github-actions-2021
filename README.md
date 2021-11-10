# telerik-github-actions-2021
A repository created for practicing Github Actions  
Feel free to fork this repository and work in the forked version.

Credits to Tom Reid for the Python Code.

Create pre-build stage to print information
Add environment variables:
Workflow:
WORKSPACE_ENVIRONMENT_VARIABLE: 'custom workspace environment variable'

Job:
JOB_ENVIRONMENT_VARIABLE: 'custom job environment variable for ubuntu'

Step:
STEP_ENVIRONMENT_VARIABLE: 'custom step environment variable for bash'

Print the environment variables.

Add secret
PASSWORD


Print the secret.

Create parallel checks for style and code lint

Build stage to depend on lint and style

Build stage to upload artifact

upload factorial.py

Unit test to depend on build stage

Make deploy stage to depend on unit-test

Add style check with python 2.7, 3.8, 3.9

Add SAST with SonarCloud after unit-tests

Add database integration

Create workflow for pull_request - excluding the deploy step

Scheduled pipeline for Snyk - scan once a day
