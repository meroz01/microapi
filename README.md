# microapi

Creates basic endpoint for testing connectionin your applications. For now there is only one endpoint.

How to use:
-----------

All parameters are optional and have default values.

```bash
  $ python3.6 microapi.py -p 9090 -e api/hello -d '{"hello": "data"}' -c 200
```

Install module globaly.
-----------------------

Enter project and:

```bash
  $ python3.6 setup.py sdist
  $ pip3 install dist/microapi-0.1.tar.gz
```

and then use it like:

```bash
  $ python3.6 -m microapi
```

or with parameters:

```bash
  $ python3.6 -m microapi -d '{"data": "hello world}'
```

Parameters (use -h parameter to list parameters):
  * `-p` - port for locahost, default is `8080`
  * `-e` - api endpoint, default is `''`
  * `-d` - response text, default is `'{}'`
  * `-c` - response code, default `200`

Tested with python3.6 on macOS.
