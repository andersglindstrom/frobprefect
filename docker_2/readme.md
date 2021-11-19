Virtual environment
-------------------

See [this page](../readme.md).

Run Server
----------

In a new terminal:

```
$ cd frobprefect
$ source venv/frobprefect/bin/activate
$ prefect server start --expose
```

Wait for ASCII art displaying "Prefect Server" to appear.

Confirm that server is running using the UI at http://localhost:8080

Note that, ideally, we would not pass the `--expose` option to the server but
it doesn't work without it. See this bug report for details:
https://github.com/PrefectHQ/prefect/issues/4963.

Build Docker image
------------------

In a new terminal, do the following:

```
$ cd frobprefect
$ source venv/frobprefect/bin/activate
$ cd docker_2
$ docker build -t prefect_docker_2_image:latest .
```

Register flow with Prefect server
---------------------------------

In the same terminal as previous step, create a project with the following
command:

```
$ prefect create project docker_2_project
```

Next, register the flow with the server:

```
$ docker run --network prefect-server --rm prefect_docker_2_image python -m flows.docker_2
```

Start the docker agent
----------------------

In the same terminal as the previous step, start a Prefect docker agent:

```
$ prefect agent docker start -l docker_flows --show-flow-logs --network prefect-server
```

Check in UI that agent has been registered

Run the flow
------------

In a new terminal, do the following:

```
$ cd frobprefect
$ source venv/frobprefect/bin/activate
$ prefect run --project docker_2_project -n docker_2_flow
```

The agent's output should eventually contain something like the following:

```
[2021-11-19 19:56:17+0000] INFO - prefect.CloudFlowRunner | Beginning Flow run for 'docker_2_flow'
[2021-11-19 19:56:17+0000] INFO - prefect.CloudTaskRunner | Task 'say_hello': Starting task run...
[2021-11-19 19:56:17+0000] INFO - prefect.say_hello | Hello, docker 2!
[2021-11-19 19:56:17+0000] INFO - prefect.CloudTaskRunner | Task 'say_hello': Finished task run for task with final state: 'Success'
[2021-11-19 19:56:17+0000] INFO - prefect.CloudFlowRunner | Flow run SUCCESS: all reference tasks succeeded
```
