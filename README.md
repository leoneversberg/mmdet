# mmdet
This code uses containerized MMDetection to train a Faster-RCNN object detection model on CVAT data. Training can be visualized with Tensorboard.

# Installation & Setup
## CVAT
You can create an account for the free online version [app.cvat.ai](https://app.cvat.ai/) or [run your own server](https://opencv.github.io/cvat/docs/administration/basics/installation/).



## Docker Image
Build an image with `sudo docker build -t mmdet:latest .`

# Training
Run the image with:
```
docker run --gpus all \
  -v "/path/to/mmdet/my_configs:/mmdetection/my_configs:ro" \
  -v "/path/to/mmdet/data:/mmdetection/data:ro" \
  -v "/path/to/mmdet/workdir:/mmdetection/workdir" \
  mmdet:latest
```


# Used Frameworks
- [MMDetection](https://github.com/open-mmlab/mmdetection) for model training
- [CVAT](https://github.com/opencv/cvat) for annotating and exporting training/testing data
- [TensorBoard](https://www.tensorflow.org/tensorboard) for training visualization
- [blender-gen](https://github.com/ignc-research/blender-gen) to create synthetic object detection data
