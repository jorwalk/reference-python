# Run Tensorflow in Docker
Download the latest python3 with jupyter notebook image
```shell
$ docker pull tensorflow/tensorflow:nightly-py3-jupyter
```
Run the image
```shell
$ docker run -it --rm -v $(realpath ~/notebooks):/tf/notebooks -p 8888:8888 tensorflow/tensorflow:nightly-py3-jupyter
```