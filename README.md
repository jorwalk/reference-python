# Python Reference Scripts

Reference frameworks, files, and folders written in Python

## Flask
- [Building and Documenting Python REST APIs With Flask and Connexion](flask-connexion/)


## Best Practice - Virtual Environments

You should always use a virtual environment for your Python projects. A virtual environment is a way to create an isolated space so you can, for example, run Python 2.7 for one project and Python 3.7 for another on the same computer. We can use the built-in [venv](https://docs.python.org/3/library/venv.html) module for this.

It's a best practice to keep all your virtualenvs in one place, for example `.virtualenvs/` in your home directory. Let's create that directory:

```
$ mkdir ~/.virtualenvs

```

Now create a new virtual environment called `myvenv` by running:

```
$ python3 -m venv ~/.virtualenvs/myvenv

```

Because we used `python3` here our virtual environment knows that when we type `python` for a command we mean Python 3 not Python 2. In order to activate this virtual environment, so we can use it, we must also run the following command:

```
$ source ~/.virtualenvs/myvenv/bin/activate
(myvenv) $
```

Note that while the environment is active, you will see its name in parentheses. Software packages we install now will only be available within this virtual environment. You can use the command `pip freeze` to see all installed software within a virtual environment.

To stop using a virtual environment, either close the Terminal window or enter `deactivate`:

```
(myvenv) $ deactivate

```
Generate a requirements file and then install from it in another environment.
```shell
$ myvenv/bin/pip freeze > requirements.txt
$ myvenv/bin/pip install -r requirements.txt
```
See outdated packages
```
python3 -m pip list --outdated --format=columns
```

Freeze requirements
```
python3 -m venv/bin/pip freeze > requirements.txt
```