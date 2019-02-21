## Building and running
Image build can be done like so:
```python
$ docker build . -t flask_image_prod
```

It creates an image named flask_image that can be run with this command:

```python
$ docker run -d -p 80:80 flask_image_prod
```

