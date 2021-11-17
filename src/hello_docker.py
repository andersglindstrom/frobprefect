
import prefect
from prefect import task, Flow
from prefect.run_configs import DockerRun
from prefect.storage import Docker

@task
def say_hello():
    logger = prefect.context.get("logger")
    logger.info("Hello, docker!")

with Flow("hello_docker_flow") as flow:
    flow.storage = Docker()
    flow.run_config = DockerRun(image="hello_docker_image")
    say_hello()

if __name__ == "__main__":
    flow.register(project_name="hello_docker_project", labels=["docker_flows"])
