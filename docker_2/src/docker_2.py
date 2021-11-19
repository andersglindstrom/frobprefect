
import prefect
from prefect import task, Flow
from prefect.run_configs import DockerRun
from prefect.storage import Module

@task
def say_hello():
    logger = prefect.context.get("logger")
    logger.info("Hello, docker 2!")

with Flow("docker_2_flow") as flow:
    flow.storage = Module("docker_2")
    flow.run_config = DockerRun(image="prefect_docker_2_image")
    say_hello()

if __name__ == "__main__":
    flow.register(project_name="docker_2_project", labels=["docker_flows"])
