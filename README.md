# mmdet
This code uses containerized MMDetection to train a Faster-RCNN object detection model on CVAT data. Training can be visualized with Tensorboard.

# Installation
## CVAT
...

## Docker
Build an image with `sudo docker build -t mmdet:latest .`

Run the image with:
```
docker run --gpus all \
  -v "/path/to/mmdet/my_configs:/mmdetection/my_configs:ro" \
  -v "/path/to/mmdet/data:/mmdetection/data:ro" \
  -v "/path/to/mmdet/workdir:/mmdetection/workdir" \
  mmdet:latest
```


# Used Frameworks
- [MMDetection](https://github.com/open-mmlab/mmdetection)
- [CVAT](https://github.com/opencv/cvat)
- [TensorBoard](https://www.tensorflow.org/tensorboard)