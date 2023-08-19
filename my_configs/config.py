# The new config inherits a base config to highlight the necessary modification
_base_ = ['/mmdetection/configs/faster_rcnn/faster-rcnn_r50_fpn_1x_coco.py']

# change the number of classes of the model
model = dict(
    roi_head=dict(
        bbox_head=dict(
            num_classes=1)
    )
)

# Modify dataset related settings
dataset_type = 'CocoDataset'
classes = ('Suzanne2',)

# pipelines
backend_args = None
train_pipeline = [
    dict(type='LoadImageFromFile', backend_args=backend_args),
    dict(type='LoadAnnotations', with_bbox=True),
    dict(type='Resize', scale=(640, 360), keep_ratio=True),
    dict(type='RandomFlip', prob=0.5),
    dict(type='PackDetInputs')
]
test_pipeline = [
    dict(type='LoadImageFromFile', backend_args=backend_args),
    dict(type='Resize', scale=(640, 360), keep_ratio=True),
    # If you don't have a gt annotation, delete the pipeline
    dict(type='LoadAnnotations', with_bbox=True),
    dict(
        type='PackDetInputs',
        meta_keys=('img_id', 'img_path', 'ori_shape', 'img_shape',
                   'scale_factor'))
]

train_dataloader = dict(
    batch_size=4,
    num_workers=2,
    dataset=dict(
        type=dataset_type,
        # explicitly add your class names to the field `metainfo`
        metainfo=dict(classes=classes),
        ann_file='/mmdetection/data/train/annotations/instances_default.json',
        data_prefix=dict(img='/mmdetection/data/train/images/'),
        pipeline=train_pipeline
        )
    )

val_dataloader = dict(
    batch_size=1,
    num_workers=2,
    dataset=dict(
        type=dataset_type,
        test_mode=True,
        # explicitly add your class names to the field `metainfo`
        metainfo=dict(classes=classes),
        ann_file='/mmdetection/data/test/annotations/instances_default.json',
        data_prefix=dict(img='/mmdetection/data/test/images/'),
        pipeline=test_pipeline
        )
    )

test_dataloader = val_dataloader

val_evaluator = dict(ann_file='/mmdetection/data/test/annotations/instances_default.json')
test_evaluator = val_evaluator

# We can use the pre-trained model to obtain higher performance
load_from = 'https://download.openmmlab.com/mmdetection/v2.0/faster_rcnn/faster_rcnn_r50_fpn_1x_coco/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth'

# scheduler and optimizer
param_scheduler = [
    dict(
        type='LinearLR', start_factor=0.001, by_epoch=False, begin=0, end=500)
]
optim_wrapper = dict(optimizer=dict(type='SGD', lr=0.00001, momentum=0.9, weight_decay=0.0001))

# max_epochs for training
train_cfg = dict(max_epochs=30)

# log config
default_hooks = dict(
                    logger=dict(interval=100),
                    checkpoint=dict(type='CheckpointHook', interval=10) # Save checkpoints periodically every interval
                    )

# wwork_dir where model weights and tensorboard logs are saved
work_dir = '/mmdetection/workdir'

# use tensorboard logging
_base_.visualizer.vis_backends = [
    dict(type='TensorboardVisBackend')]
