from google.cloud import aiplatform
import os

import kfp
from pipeline import hello_world_pipeline

PIPELINE_PARAMETERS = {"value": 9}
PIPELINE_SPEC_FILE = "pipeline.yaml"

kfp.compiler.Compiler().compile(hello_world_pipeline, PIPELINE_SPEC_FILE)

job = aiplatform.PipelineJob(
    display_name=os.environ["PIPELINE_DISPLAY_NAME"],
    template_path=PIPELINE_SPEC_FILE,
    pipeline_root=os.environ["GCS_PIPELINE_ROOT"],
    parameter_values=PIPELINE_PARAMETERS,
    project=os.environ["PROJECT_ID"],
    location=os.environ["REGION"],
)

job.submit()
