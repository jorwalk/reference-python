# FastAPI
## Getting Started
Now create a new virtual environment called `myvenv` by running:

```
$ python3 -m venv venv

```

Because we used `python3` here our virtual environment knows that when we type `python` for a command we mean Python 3 not Python 2. In order to activate this virtual environment, so we can use it, we must also run the following command:

```
$ source venv/bin/activate
```

Note that while the environment is active, you will see its name in parentheses. Software packages we install now will only be available within this virtual environment. You can use the command `pip freeze` to see all installed software within a virtual environment.

To stop using a virtual environment, either close the Terminal window or enter `deactivate`:

```
(venv) $ deactivate

```
Generate a requirements file and then install from it in another environment.
```
$ venv/bin/pip freeze > requirements.txt
$ venv/bin/pip install -r requirements.txt
```

## Run it
Run the server with:
```
$ uvicorn main:app --reload
```

## Check it
Open your browser at http://127.0.0.1:8000/items/5?q=somequery.

You will see the JSON response as:
```
{"item_id":5,"q":"somequery."}
```

## Documentation

You will see the automatic interactive API documentation (provided by Swagger UI):
- http://localhost:8000/docs

You will see the alternative automatic documentation (provided by ReDoc):
- http://localhost:8000/redoc


## Test and code coverage

```
sh test.sh
```
```
file:///Users/jordanwalker/Code/reference-python/fastapi/htmlcov/index.html
```

## Test load
If the Locust file is located under a subdirectory and/or named different than locustfile.py, specify it using -f:

```
$ locust -f test-load/locust.py --host=http://127.0.0.1:8000
```
### Open up Locust’s web interface

Once you’ve started Locust using one of the above command lines, you should open up a browser and point it to http://127.0.0.1:8089 (if you are running Locust locally). Then you should be greeted with something like this:

