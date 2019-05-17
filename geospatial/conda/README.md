```
docker build -t condatest .
```

```
docker run -i -t -p 8888:8888 continuumio/miniconda /bin/bash -c "/opt/conda/bin/conda install jupyter -y --quiet && mkdir /opt/notebooks && /opt/conda/bin/jupyter notebook --notebook-dir=/opt/notebooks --ip='*' --port=8888 --no-browser" 
```

```
docker run -i -t -p 8888:8888 continuumio/miniconda3 /bin/bash -c "/opt/conda/bin/conda install jupyter -y --quiet && mkdir /opt/notebooks && /opt/conda/bin/jupyter notebook --notebook-dir=/opt/notebooks --ip=0.0.0.0 --port=8888 --no-browser --allow-root"
```

```
docker run -p 8888:8888 -v ~/notebooks:/home/jovyan jupyter/minimal-notebook
```

https://jakevdp.github.io/blog/2017/12/05/installing-python-packages-from-jupyter/