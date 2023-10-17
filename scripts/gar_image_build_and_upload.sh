#!/bin/bash

cd ../gar_base_image

# Create templatized snippets for setting up python package index

echo "\
[distutils]
index-servers =
    $PYTHON_REPO_NAME

[$PYTHON_REPO_NAME]
repository: $GAR_PYTHON_URL" > .pypirc.snippet

echo "\
[global]
extra-index-url = $GAR_PYTHON_INDEX" > pip.conf.snippet

# Submit cloud build job to build image and store in Artifact Registry

gcloud builds submit . \
  --substitutions="_IMAGE_NAME=$GAR_AUTH_IMAGE_URL" \
  --project=$PROJECT_ID