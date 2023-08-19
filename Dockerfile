ARG PYTORCH="1.13.1"
ARG CUDA="11.6"
ARG CUDNN="8"

FROM pytorch/pytorch:${PYTORCH}-cuda${CUDA}-cudnn${CUDNN}-runtime

# apt-get install packages
RUN apt-get update && apt-get install -y \
    ffmpeg \
    git \
    libglib2.0-0 \
    libsm6 \
    libxrender-dev \
    libxext6 \
    ninja-build \
    python3-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# install PyTorch and MMCV
WORKDIR /mmdetection
RUN pip3 install -U openmim && \
    mim install "mmengine==0.8.4" && \
    mim install "mmcv==2.0.1"

# install MMDetection v3.1.0
RUN git clone --depth 1 --branch v3.1.0 https://github.com/open-mmlab/mmdetection.git /mmdetection
RUN pip3 install -v -e .

# install additional requirements
COPY requirements.txt /mmdetection/
RUN pip3 install -r requirements.txt

# start training
CMD ["python3", "/mmdetection/tools/train.py", "/mmdetection/my_configs/config.py"]
