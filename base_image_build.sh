cd gar_base_image

REGION=us-central1
PROJECT_ID=example-project
REPO_NAME=gar-vertex-repo
IMAGE_NAME=gar-base-image

gcloud builds submit . \
  --substitutions="_IMAGE_NAME=$REGION-docker.pkg.dev/$PROJECT_ID/$REPO_NAME/$IMAGE_NAME" \
  --project=$PROJECT_ID