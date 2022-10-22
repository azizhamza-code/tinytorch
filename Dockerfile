FROM python:latest

WORKDIR /app

COPY ./requirements.txt /app
COPY ./requirements.extra.txt /app
COPY ./lib /app/libr

RUN pip install --upgrade pip
RUN pip install /app/libr/llvmlite-0.39.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
RUN pip install /app/libr/numba-0.56.3-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.whl

RUN   pip install -r requirements.txt
RUN  pip install -r requirements.extra.txt

COPY . /app





