cd gar_cvs_test

REGION=us-central1
PROJECT_ID=example-project
REPO_NAME=gar-python-repo

python3 -m pip install --upgrade build
python3 -m pip install --upgrade twine

python3 -m build
python3 -m twine upload --verbose --repository-url https://$REGION-python.pkg.dev/$PROJECT_ID/$REPO_NAME/ dist/*