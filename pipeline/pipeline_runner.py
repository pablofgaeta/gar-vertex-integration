from google.cloud import aiplatform

import kfp
from pipeline import hello_world_pipeline

REGION = "us-central1"
PROJECT_ID = "example-project"
GCS_PIPELINE_ROOT = "gs://demo_bucket/gar-pipeline"
DISPLAY_NAME = "gar-python-pipeline"
PIPELINE_PARAMETERS = {"value": 9}

kfp.compiler.Compiler().compile(hello_world_pipeline, "pipeline.yaml")

job = aiplatform.PipelineJob(
    display_name=DISPLAY_NAME,
    template_path="pipeline.py.yaml",
    pipeline_root=GCS_PIPELINE_ROOT,
    parameter_values=PIPELINE_PARAMETERS,
    project=PROJECT_ID,
    location=REGION,
)

job.submit()
