
import prefect
from prefect import task, Flow

@task
def say_hello():
    logger = prefect.context.get("logger")
    logger.info("Hello, server!")

with Flow("local_1_flow") as flow:
    say_hello()

# Register the flow under the "tutorial" project
flow.register(project_name="local_1_project")
