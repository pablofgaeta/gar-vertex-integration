import kfp
from kfp import dsl

REGION = "us-central1"
PROJECT_ID = "example-project"

IMAGE_REPO_NAME = "gar-vertex-repo"
IMAGE_NAME = "gar-base-image"

PYTHON_REPO_NAME = "gar-python-repo"
GAR_PYTHON_PACKAGES = ["gar-example-package"]

GAR_AUTH_BASE_IMAGE = (
    f"{REGION}-docker.pkg.dev/{PROJECT_ID}/{IMAGE_REPO_NAME}/{IMAGE_NAME}"
)

GAR_PYTHON_REPO = (
    f"https://{REGION}-python.pkg.dev/{PROJECT_ID}/{PYTHON_REPO_NAME}/simple"
)


@dsl.component(
    # Custom image that is set up to authenticate with the GAR repo
    base_image=GAR_AUTH_BASE_IMAGE,
    # Private package from GAR
    packages_to_install=GAR_PYTHON_PACKAGES,
    # Indicate that pip should try both repos
    pip_index_urls=[
        "https://pypi.org/simple",
        GAR_PYTHON_REPO,
    ],
)
def add_one_op(value: int) -> int:
    import logging

    # Private package gar-cvs-test-pablogaeta from GAR
    from gar_cvs_test import add_one

    value_plus_one = add_one(value)
    logging.info(f"add_one({value}) = {value_plus_one}")

    return int(value_plus_one)


@dsl.pipeline(
    name="gar-python-pipeline",
    description="A pipeline that imports a python package from GAR.",
)
def hello_world_pipeline(value: int):
    add_one_op(value=value)
