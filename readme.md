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

* `#local_1/readme.md`
* `docker_1`
* `docker_2`
