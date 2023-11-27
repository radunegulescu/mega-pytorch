# MEGA for Video Object Detection

By [Smeu Stefan](https://github.com/MrNiceGuy090), [Negulescu Radu-Andrei](https://github.com/radunegulescu).

This repo is an unofficial implementation of ["Memory Enhanced Global-Local Aggregation for Video Object Detection"](https://arxiv.org/abs/2003.12063), accepted by CVPR 2020. This repository contains a PyTorch implementation of the approach MEGA based on [maskrcnn_benchmark](https://github.com/facebookresearch/maskrcnn-benchmark), as well as some training scripts to reproduce the results on ImageNet VID reported in the paper. 
The purpose of this repo is to run video object detection, using 2 approaches, depicted in the paper: base and MEGA. They can be applied on particular videos and image folders.

## Pretrained models

Pretrained models to download in order to run the demo:

Model | Backbone | AP50 | AP (fast) | AP (med) | AP (slow) | Link
:---: | :---: | :---: | :---: | :---: | :---: |:---:
base | ResNet-101 | 76.7 | 52.3 | 74.1 | 84.9 | [Google](https://drive.google.com/file/d/1W17f9GC60rHU47lUeOEfU--Ra-LTw3Tq/view?usp=sharing)
**MEGA** | ResNet-101 | 82.9 | 62.7| 81.6 | 89.4 | [Google](https://drive.google.com/file/d/1ZnAdFafF1vW9Lnpw-RPF1AD_csw61lBY/view?usp=sharing)

## Installation

Please follow [INSTALL.md](INSTALL.md) for installation instructions.

## Data preparation

Please download the image folder from [here](https://github.com/radunegulescu/mega-pytorch/tree/master/image_folder) and the videos from [here](https://github.com/radunegulescu/mega-pytorch/tree/master/videos_folder), in order to run the demo on the image folder and videos.

### Demo Usage
Please follow [demo/README.md](demo/README.md) to see how to visualize the images or video.
