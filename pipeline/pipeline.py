import kfp
from kfp import dsl

import os


@dsl.component(
    # Custom image that is set up to authenticate with the GAR repo
    base_image=os.environ["GAR_AUTH_IMAGE_URL"],
    # Private package from GAR
    packages_to_install=[os.environ["PYTHON_PACKAGE_NAME"]],
    # Indicate that pip should try both repos
    pip_index_urls=[
        "https://pypi.org/simple",
        os.environ["GAR_PYTHON_INDEX"],
    ],
)
def add_one_op(value: int) -> int:
    import logging

    # Import private package (os.environ["PYTHON_PACKAGE_NAME"]) from GAR
    from example import add_one

    value_plus_one = add_one(value)
    logging.info(f"add_one({value}) = {value_plus_one}")

    return int(value_plus_one)


@dsl.pipeline(
    name=os.environ["PIPELINE_DISPLAY_NAME"],
    description="A pipeline that imports a python package from GAR.",
)
def hello_world_pipeline(value: int):
    add_one_op(value=value)
