
Server
------

```
$ prefect server start
```

Wait for ASCII art displaying "Prefect Server" to appear.

Confirm that server is running using the UI at http://localhost:8080

Create flow
-------------------------

In a new terminal, do the following:

Set backend to `server` (rather than the default value of `cloud`)

```
$ prefect backend server
```

Create project `local_1_project`

```
$ prefect create project local_1_project
```

Register flow with server

```
$ python hello.py
```
Output should look something like this:
```
[200~Flow URL: http://localhost:8080/default/flow/ea21ec6a-7c1c-4201-80e2-692617efca36
 └── ID: 137a0fb3-c60f-47b0-8e68-0e6e44111548
 └── Project: local_1_project
 └── Labels: ['PC172']
```
The label here is the local hostname. It will be different for you.

Local Agent
-----------

Run a local agent

```
$ prefect agent local start
```
Output should be something like this:
```
[2021-11-18 20:19:38,847] INFO - agent | Starting LocalAgent with labels ['PC172']
[2021-11-18 20:19:38,847] INFO - agent | Agent documentation can be found at https://docs.prefect.io/orchestration/
[2021-11-18 20:19:38,847] INFO - agent | Waiting for flow runs...
```
Note the label is the same as the flow label in previous step.

Run Flow
--------

Go to UI and run
