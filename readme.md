Set Up
------

Prefect depends on Docker. Make sure you have it installed on your machine.

Next, create and activate a virtual environment, then install dependencies:

```
$ virtualenv -p38 venv/frobprefect
$ source venv/frobprefect/bin/activate
$ pip install -r requirements.txt
```

Note that the virtualenv is put in `venv/frobprefect` so that `basename
$VIRTUAL_ENV` (yielding `frobprefect`) can be used in your bash prompt.

Do the examples in the following order. Each one has its own `readme.md`

* [local_1](./local_1/readme.md)
* [docker_1](./docker_1/readme.md)
* [docker_2](./docker_2/readme.md)

I have had troubles with Docker networking with Prefect. Here's a description:

* [docker_local_host_problem](./docker_2/readme_docker_host_network_problem.md)
