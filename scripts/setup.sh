#!/bin/bash

# Only run once during creation. If resources already exist, script will fail

gcloud storage buckets create $GCS_BUCKET \
    --location=$REGION

gcloud artifacts repositories create $PYTHON_REPO_NAME \
    --repository-format=python \
    --location=$REGION \
    --project=$PROJECT_ID

gcloud artifacts repositories create $IMAGE_REPO_NAME \
    --repository-format=docker \
    --location=$REGION \
    --project=$PROJECT_ID
