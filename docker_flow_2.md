Run Server
----------

In a new terminal:

```
$ prefect server start --expose
```

Wait for ASCII art displaying "Prefect Server" to appear.

Confirm that server is running using the UI at http://localhost:8080

Build Docker image
------------------

In a new terminal, do the following:

:; docker build -f Dockerfile src -t hello_docker_2_image:latest

Create flow from inside container
---------------------------------

In same terminal as previous step, run bash in a container using the
image from the previous step:

$ docker run --rm -it prefect_hello_docker_2 bash

You should now be running bash in the container as `root`.

Set backend to `server` (rather than the default value of `cloud`)

```
# prefect backend server
```

Set server endpoint to the host machine. Using `localhost` will not work.
In my case, my desktop machine is 10.1.2.9. Obviously, you'll have to use
the address of whatever machine you're using.

```
# export PREFECT__SERVER__HOST=http://10.1.2.9
```

Create project `hello\_docker\_2\_project`

```
# prefect create project hello_docker_2_project
```

Register flow with server

```
# python hello_docker_2.py
```

Start the docker agent
----------------------

Exit from the container of the previous step:

```
# exit
```

```
$ prefect agent docker start --log-level DEBUG -l docker_flows --show-flow-logs
```

Check in UI that agent has been registered

Run Flow in UI
--------------

In a new terminal, do the following:

```
$ prefect run --project hello_docker_2_project -n hello_docker_2_flow
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
