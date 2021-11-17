Server
------

```
$ prefect server start --expose
```

UI
--

* UI at http://localhost:8080

Create Project "docker\_test"
-----------------------------

In UI under "Project"

Set Prefect Backend
-------------------

$ prefect backend server

Register Flow
-------------

```
$ python src/hello_docker.py
```

Run Agent
---------

```
$ prefect agent docker start --log-level DEBUG -l docker_flows --show-flow-logs
```

Check in UI that agent has been registered

Run Flow in UI
--------------
