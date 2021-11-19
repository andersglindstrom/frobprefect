Virtual environment
-------------------

See [this page](../readme.md).

Run Server
----------

In a new terminal:

```
$ cd frobprefect
$ source venv/frobprefect/bin/activate
$ prefect server start
```

Note that we do _not_ pass the `--expose` option to the server.

Wait for ASCII art displaying "Prefect Server" to appear.

Confirm that server is running using the UI at http://localhost:8080

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
[2021-11-19 20:29:30,628] INFO - agent | Completed deployment of flow run 141b1696-539f-4156-a2a8-62d0378de8e9
Traceback (most recent call last):
  File "/usr/local/lib/python3.7/site-packages/urllib3/connection.py", line 175, in _new_conn
    (self._dns_host, self.port), self.timeout, **extra_kw
  File "/usr/local/lib/python3.7/site-packages/urllib3/util/connection.py", line 96, in create_connection
    raise err
  File "/usr/local/lib/python3.7/site-packages/urllib3/util/connection.py", line 86, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [Errno 111] Connection refused

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/local/lib/python3.7/site-packages/urllib3/connectionpool.py", line 706, in urlopen
    chunked=chunked,
  File "/usr/local/lib/python3.7/site-packages/urllib3/connectionpool.py", line 394, in _make_request
    conn.request(method, url, **httplib_request_kw)
  File "/usr/local/lib/python3.7/site-packages/urllib3/connection.py", line 239, in request
    super(HTTPConnection, self).request(method, url, body=body, headers=headers)
  File "/usr/local/lib/python3.7/http/client.py", line 1281, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "/usr/local/lib/python3.7/http/client.py", line 1327, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "/usr/local/lib/python3.7/http/client.py", line 1276, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "/usr/local/lib/python3.7/http/client.py", line 1036, in _send_output
    self.send(msg)
  File "/usr/local/lib/python3.7/http/client.py", line 976, in send
    self.connect()
  File "/usr/local/lib/python3.7/site-packages/urllib3/connection.py", line 205, in connect
    conn = self._new_conn()
  File "/usr/local/lib/python3.7/site-packages/urllib3/connection.py", line 187, in _new_conn
    self, "Failed to establish a new connection: %s" % e
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x7f3af7cb45d0>: Failed to establish a new connection: [Errno 111] Connection refused

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/local/lib/python3.7/site-packages/requests/adapters.py", line 449, in send
    timeout=timeout
  File "/usr/local/lib/python3.7/site-packages/urllib3/connectionpool.py", line 756, in urlopen
    method, url, error=e, _pool=self, _stacktrace=sys.exc_info()[2]
  File "/usr/local/lib/python3.7/site-packages/urllib3/util/retry.py", line 574, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='host.docker.internal', port=4200): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7f3af7cb45d0>: Failed to establish a new connection: [Errno 111] Connection refused'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/local/bin/prefect", line 8, in <module>
    sys.exit(cli())
  File "/usr/local/lib/python3.7/site-packages/click/core.py", line 1128, in __call__
    return self.main(*args, **kwargs)
  File "/usr/local/lib/python3.7/site-packages/click/core.py", line 1053, in main
    rv = self.invoke(ctx)
  File "/usr/local/lib/python3.7/site-packages/click/core.py", line 1659, in invoke
    return _process_result(sub_ctx.command.invoke(sub_ctx))
  File "/usr/local/lib/python3.7/site-packages/click/core.py", line 1659, in invoke
    return _process_result(sub_ctx.command.invoke(sub_ctx))
  File "/usr/local/lib/python3.7/site-packages/click/core.py", line 1395, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/usr/local/lib/python3.7/site-packages/click/core.py", line 754, in invoke
    return __callback(*args, **kwargs)
  File "/usr/local/lib/python3.7/site-packages/prefect/cli/execute.py", line 53, in flow_run
    result = client.graphql(query)
  File "/usr/local/lib/python3.7/site-packages/prefect/client/client.py", line 554, in graphql
    retry_on_api_error=retry_on_api_error,
  File "/usr/local/lib/python3.7/site-packages/prefect/client/client.py", line 458, in post
    retry_on_api_error=retry_on_api_error,
  File "/usr/local/lib/python3.7/site-packages/prefect/client/client.py", line 738, in _request
    session=session, method=method, url=url, params=params, headers=headers
  File "/usr/local/lib/python3.7/site-packages/prefect/client/client.py", line 606, in _send_request
    timeout=prefect.context.config.cloud.request_timeout,
  File "/usr/local/lib/python3.7/site-packages/requests/sessions.py", line 590, in post
    return self.request('POST', url, data=data, json=json, **kwargs)
  File "/usr/local/lib/python3.7/site-packages/requests/sessions.py", line 542, in request
    resp = self.send(prep, **send_kwargs)
  File "/usr/local/lib/python3.7/site-packages/requests/sessions.py", line 655, in send
    r = adapter.send(request, **kwargs)
  File "/usr/local/lib/python3.7/site-packages/requests/adapters.py", line 516, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='host.docker.internal', port=4200): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7f3af7cb45d0>: Failed to establish a new connection: [Errno 111] Connection refused'))
```
