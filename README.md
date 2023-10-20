# estudos sobre RAPIDS
 esse repositório se dedica especificamente a uso da plataforma rapids

# Placa de Video RTX

Para saber qual placa de video está abilitada para uso da plataforma, ela precisa ser diretamente da nvidia
os comandos para saber qual a sua placa de video e qual cuda baixar são:

Para versão do cuda 11.2 pois estou usando a RTX 3050 em ambiente windows
[LINK CUDA](https://developer.download.nvidia.com/compute/cuda/11.2.0/local_installers/cuda_11.2.0_460.89_win10.exe)

# Para ver se a instalação da placa de VIDEO
<br>
cmd > nvidia-smi
<br>
cmd > nvcc -V

# Instalação do RAPIDS em Ambiente Windows
### Crie um ambiente virtual


### via PIP

````cmd
pip install --extra-index-url=https://pypi.nvidia.com cudf-cu11 dask-cudf-cu11 cuml-cu11 cugraph-cu11 cuspatial-cu11 cuproj-cu11 cuxfilter-cu11 cucim
````

### via Docker com python 3.9
- lembre-se de mudar o final para o seu uso -cuda11.2-py3.9 se refere a ao cuda 11.2 com python 3.9
```
docker run --gpus all --pull always --rm -it --shm-size=1g --ulimit memlock=-1 --ulimit stack=67108864 nvcr.io/nvidia/rapidsai/base:23.08-cuda11.2-py3.9
```

### via conda
```
conda install -n base conda-libmamba-solver
conda create --solver=libmamba -n rapids-23.10 -c rapidsai -c conda-forge -c nvidia rapids=23.10 python=3.9 cuda-version=11.2  tensorflow dash jupyterlab
```
