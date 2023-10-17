import subprocess
import os
import dotenv

dotenv.load_dotenv()

os.environ[
    "GCS_PIPELINE_ROOT"
] = f"{os.environ['GCS_BUCKET']}/{os.environ['PIPELINE_ROOT_PREFIX']}"

os.environ[
    "GAR_AUTH_IMAGE_URL"
] = f"{os.environ['REGION']}-docker.pkg.dev/{os.environ['PROJECT_ID']}/{os.environ['IMAGE_REPO_NAME']}/{os.environ['IMAGE_NAME']}"

os.environ[
    "GAR_PYTHON_URL"
] = f"https://{os.environ['REGION']}-python.pkg.dev/{os.environ['PROJECT_ID']}/{os.environ['PYTHON_REPO_NAME']}"
os.environ["GAR_PYTHON_INDEX"] = f"{os.environ['GAR_PYTHON_URL']}/simple"


def main():
    # Note only run if GCS bucket and AR repos don't already exist
    setup()

    # Note the package version must be modified for future uploads
    build_and_upload_python_package()

    # Build base image that can authenticate with Artifact Registry, image stored in AR
    build_and_upload_gar_image()

    # Compile and run pipeline that uses the uploaded package
    build_and_run_pipeline()


def setup():
    os.chdir("scripts")

    try:
        subprocess.run("./setup.sh", check=True)
    except Exception as e:
        raise e
    finally:
        os.chdir("..")


def build_and_upload_python_package():
    os.chdir("scripts")

    try:
        subprocess.run("./py_build_and_upload.sh", check=True)
    except Exception as e:
        raise e
    finally:
        os.chdir("..")


def build_and_upload_gar_image():
    os.chdir("scripts")

    try:
        subprocess.run("./gar_image_build_and_upload.sh", check=True)
    except Exception as e:
        raise e
    finally:
        os.chdir("..")


def build_and_run_pipeline():
    os.chdir("scripts")

    try:
        subprocess.run("./run_pipeline.sh", check=True)
    except Exception as e:
        raise e
    finally:
        os.chdir("..")


if __name__ == "__main__":
    main()
