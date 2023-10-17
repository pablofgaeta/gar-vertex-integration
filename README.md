# gar-vertex-integration

Example Code to build a custom Python package, upload it to a private repository in Google Artifact Registry, and then import those packages within Vertex Pipeline components.

# Required environment variables

-   `REGION`: GCP Region
-   `PROJECT_ID`: GCP Project ID
-   `GCS_BUCKET`: GCS Bucket URI for Vertex Pipelines artifacts (e.g. `gs://my-bucket`)
-   `PIPELINE_ROOT_PREFIX`: A prefix in GCS_BUCKET where pipeline artifacts will be stored (e.g. pipelines/gar-python-pipeline)
-   `PIPELINE_DISPLAY_NAME`: The display name for the Vertex Pipeline
-   `PYTHON_REPO_NAME`: Name for the Artifact Registry Python repository
-   `PYTHON_PACKAGE_NAME`: Name of the package that will be used in the Vertex Pipeline
-   `IMAGE_REPO_NAME`: Name for the Artifact Registry Docker repository to store the base image for Vertex components
-   `IMAGE_NAME`: Name of the base image for authenticating with Google Artifact Registry
