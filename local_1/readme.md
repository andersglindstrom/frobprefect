Virtual environment
-------------------

See [this page](../readme.md).

Start Prefect Server
--------------------

```
$ prefect server start
```

Wait for ASCII art displaying "Prefect Server" to appear.

Confirm that server is running using the UI at http://localhost:8080

Set backend to `server`
----------------------

In a new terminal, do the following:

```
$ cd frobprefect
$ source venv/frobprefect/bin/activate
```

Set backend to `server` (rather than the default value of `cloud`)

```
$ prefect backend server
```

Create project `local_1_project`
--------------------------------

In the same terminal as previous step:

```
$ prefect create project local_1_project
```

Check in UI (http://localhost:8080) that project has been created. Projects
appear in the dashboard at the far right in a drop down.

Register flow with server
-------------------------

In the same terminal as previously:

```
$ cd local_1
$ python local_1.py
```
Output should look something like this:
```
[200~Flow URL: http://localhost:8080/default/flow/ea21ec6a-7c1c-4201-80e2-692617efca36
 └── ID: 137a0fb3-c60f-47b0-8e68-0e6e44111548
 └── Project: local_1_project
 └── Labels: ['PC172']
```
The label here is the local hostname. It will be different for you.

Check UI for new flow

Run a local agent
-----------------

In the same terminal as previously:

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

In a new terminal:

```
$ cd frobprefect
$ source venv/frobprefect/bin/activate
$ prefect run --project local_1_project -n local_1_flow
```
Output should be something like this:
```
Looking up flow metadata... Done
Creating run for flow 'local_1_flow'... Done
└── Name: authentic-grouse
└── UUID: 19660990-4a4c-470b-890d-5b257a068341
└── Labels: ['parami']
└── Parameters: {}
└── Context: {}
└── URL: http://localhost:8080/default/flow-run/19660990-4a4c-470b-890d-5b257a068341
```

Check UI for flow run success. To find the flow run:
* Select the `local_1_project` in the dashboard
* Click `Flows` tab in the dashboard
* Click `Run` in the flow panel
* Click the most recent flow run
  * Note: my ad blocker (uBlock) blocked following links to
    flow runs so I had to turn it off for `localhost`
* Click the 'Logs' tab in the flow run panel

It should have the following entry somewhere:
```
08:40:03
INFO            Hello, server!
say_hello
```
