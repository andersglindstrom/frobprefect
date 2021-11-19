
import prefect
from prefect import task, Flow
from prefect.run_configs import DockerRun
from prefect.storage import Docker

@task
def say_hello():
    logger = prefect.context.get("logger")
    logger.info("Hello, docker_1!")

with Flow("docker_1_flow") as flow:
    # We are registering the flow from _outside_ the docker container
    # so we use `prefect.storage.Docker`. If you don't use this storage type
    # it won't work.
    flow.storage = Docker()
    flow.run_config = DockerRun(image="docker_1_image")
    say_hello()

if __name__ == "__main__":
    flow.register(project_name="docker_1_project", labels=["docker_flows"])
