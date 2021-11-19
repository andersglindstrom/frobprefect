In this example, we use a Docker agent to run the flow. However, the flow
itself is not packaged in a Docker image. Rather, we use `prefect.storage.Docker`
for the flow. We register the flow in a similar way to the `local_1` example;
that is, by simply executing the python module. The docker storage will build
a new image based on the `prefecthq/prefect` with the addition of some
representation of the flow, I guess as a serialized object.

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

```
cd frobprefect
source venv/frobprefect/bin/activate
```

Set backend to `server` (rather than the default value of `cloud`)

```
$ prefect backend server
```

Create project `docker_1_project`

```
$ prefect create project docker_1_project
```
Check in UI for new project.

Register flow with server

```
$ python docker_1/docker_1.py
```
You will see an image being built and finally something like this:
```
Successfully built bcc2591af334
Successfully tagged docker-1-flow:2021-11-18t22-30-09-072770-00-00
Flow URL: http://localhost:8080/default/flow/0f3879fb-993b-431e-b901-d2069db35353
 └── ID: 09226602-1392-4324-b875-f6e8e4c91037
 └── Project: docker_1_project
 └── Labels: ['docker_flows']
```
Note that the label `docker_flows` has been added to the flow.

Check that the flow has been registered by using the UI. In the `Overview`
tab of the flow information there is a `Labels` section. It will have the
label `docker_flows` there. There will be a red warning icon. If you hover
over the icon it will say 'Agent Problem - you have no live agents'. We
will start the agent in the next step.

The docker storage will build a new image based on the `prefecthq/prefect` with
the addition of some representation of the flow, I guess as a serialized
object. You can see the images thusly:

```
$ docker image ls
docker-1-flow           2021-11-18t23-43-21-708813-00-00   4aa4c6ce4489   17 minutes ago      621MB
```

The docker agent will use that image to create the container if and when
necessary.

Start the docker agent
----------------------

In the same terminal as the previous step, do the following:

```
$ prefect agent docker start -l docker_flows --show-flow-logs --network prefect-server
```

Note the `--show-flow-logs` option so that we can see any flow run logs in
the console rather than looking in the UI.

Also note the `-l docker_flows` label. This is necessary to pick up the flow
registered in the previous step.

Run Flow
--------

In a new terminal, do the following:

```
$ prefect run --project docker_1_project -n docker_1_flow
```

The agent logging (in the terminal that has the agent running in it), should
have a line that looks something like this:
```
[2021-11-18 22:33:58+0000] INFO - prefect.CloudFlowRunner | Beginning Flow run for 'docker_1_flow'
[2021-11-18 22:33:58+0000] INFO - prefect.CloudTaskRunner | Task 'say_hello': Starting task run...
[2021-11-18 22:33:58+0000] INFO - prefect.say_hello | Hello, docker_1!
[2021-11-18 22:33:58+0000] INFO - prefect.CloudTaskRunner | Task 'say_hello': Finished task run for task with final state: 'Success'
[2021-11-18 22:33:58+0000] INFO - prefect.CloudFlowRunner | Flow run SUCCESS: all reference tasks succeeded
```
The `Hello, docker_1!` is the output from the flow. See `docker_1.py` in this directory.
