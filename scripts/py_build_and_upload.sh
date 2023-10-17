#!/bin/bash

cd ../gar_example_package

# gcloud config set artifacts/repository $PYTHON_REPO_NAME
# gcloud config set artifacts/location $REGION

# python3 -m build && python3 -m twine upload --verbose --repository-url $GAR_PYTHON_URL dist/*

gcloud builds submit . \
  --substitutions="_REGION=$REGION,_REPO=$PYTHON_REPO_NAME" \
  --project=$PROJECT_ID