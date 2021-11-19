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

Build Docker image
------------------

In a new terminal, do the following:

```
$ cd frobprefect
$ source venv/frobprefect/bin/activate
$ cd docker_2
$ docker build -f Dockerfile -t prefect_docker_2:latest .
```

Create flow from inside container
---------------------------------

In same terminal as previous step, run bash in a container using the
image from the previous step:

$ docker run --network prefect-server --rm -it prefect_docker_2 bash

You should now be running bash in the container as `root`.

Create project `docker_2_project`

```
# prefect create project docker_2_project
```

Register flow with server

```
# python docker_2.py
```

Start the docker agent
----------------------

Exit from the container of the previous step:

```
# exit
```

Your now back in the host machine. Start the agent:

```
$ prefect agent docker start --log-level DEBUG -l docker_flows --show-flow-logs
```

Check in UI that agent has been registered

Run Flow in UI
--------------

In a new terminal, do the following:

```
$ cd frobprefect
$ source venv/frobprefect/bin/activate
$ prefect run --project docker_2_project -n docker_2_flow
