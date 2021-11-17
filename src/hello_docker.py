
import prefect
from prefect import task, Flow
from prefect.run_configs import DockerRun
from prefect.storage import Docker

@task
def say_hello():
    logger = prefect.context.get("logger")
    logger.info("Hello, docker!")

with Flow("docker-hello-flow") as flow:
    flow.storage = Docker()
    flow.run_config = DockerRun(image="prefect_docker_test:latest")
    say_hello()

# Register the flow under the "docker_example" project
flow.register(project_name="docker_test", labels=["docker_flows"])
