Run Server
----------

In a new terminal:

```
$ prefect server start --expose
```

Wait for ASCII art displaying "Prefect Server" to appear.

Confirm that server is running using the UI at http://localhost:8080

Create flow
------------

In a new terminal, do the following:

Set backend to `server` (rather than the default value of `cloud`)

```
$ prefect backend server
```

Create project `hello\_docker\_project`

```
$ prefect create project hello_docker_project
```

Register flow with server

```
$ python python/hello_docker.py
```

Start the docker agent
----------------------

In the same terminal as the previous step, do the following:

```
$ prefect agent docker start --log-level DEBUG -l docker_flows --show-flow-logs
```

Check in UI that agent has been registered

Run Flow
--------

In a new terminal, do the following:

```
$ prefect run --project hello_docker_project -n hello_docker_flow
```

The agent logging (in the terminal that has the agent running in it), should
have a line that looks something like this:
```
[2021-11-17 10:07:22+0000] INFO - prefect.CloudFlowRunner | Beginning Flow run for 'hello_docker_flow'
[2021-11-17 10:07:22+0000] INFO - prefect.CloudTaskRunner | Task 'say_hello': Starting task run...
[2021-11-17 10:07:22+0000] INFO - prefect.say_hello | Hello, docker!
[2021-11-17 10:07:22+0000] INFO - prefect.CloudTaskRunner | Task 'say_hello': Finished task run for task with final state: 'Success'
[2021-11-17 10:07:22+0000] INFO - prefect.CloudFlowRunner | Flow run SUCCESS: all reference tasks succeeded
```
