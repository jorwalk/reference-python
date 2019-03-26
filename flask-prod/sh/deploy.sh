#!/bin/bash

# Define the source repository role.
PROJECT_NAME=<PROJECT>

# Source Repository Roles
# roles/source.admin

#
# source the gcloud sdk
#
source $HOME/Code/google-cloud-sdk/completion.bash.inc
source $HOME/Code/google-cloud-sdk/path.bash.inc

#
# configure Cloud Shell to use your project.
#
gcloud config set project ${PROJECT_NAME}
gcloud components update

#
# In Cloud Shell, enable the required APIs.
#
gcloud services enable container.googleapis.com \
    cloudbuild.googleapis.com \
    sourcerepo.googleapis.com \
    containeranalysis.googleapis.com

#
#  create a GKE cluster that you will use to deploy the application
#
gcloud container clusters create hello-cloudbuild \
    --num-nodes 1 --zone us-central1-b


# Create the Git repositories in Cloud Source Repositories
#
# create the two Git repositories.
gcloud source repos create develop-fre-app
gcloud source repos create develop-fre-env

# Configure Cloud Source Repositories as a remote.
PROJECT_ID=$(gcloud config get-value project)
git remote add google \
    "https://source.developers.google.com/p/${PROJECT_ID}/r/hello-cloudbuild-app"



#
# Clean Up
#

#gcloud container clusters delete hello-cloudbuild \
#    --zone us-central1-b

#PROJECT_NUMBER="$(gcloud projects describe ${PROJECT_ID} \
#    --format='get(projectNumber)')"
#gcloud projects remove-iam-policy-binding ${PROJECT_NUMBER} \
#    --member=serviceAccount:${PROJECT_NUMBER}@cloudbuild.gserviceaccount.com \
#    --role=roles/container.developer


echo "OUTPUT"