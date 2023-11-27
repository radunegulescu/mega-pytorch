# MEGA for Video Object Detection

This repo is a faculty project for the Deep Learning for Video Signal Processing course. It's purpose is offering a practical guidance for running video object detection using 2 approaches: base and MEGA. It is derived from the official github [repository](https://github.com/Scalsol/mega.pytorch) of the ["Memory Enhanced Global-Local Aggregation for Video Object Detection"](https://arxiv.org/abs/2003.12063), accepted by CVPR 2020. The purpose of this repo, depicted in the demo, is to run video object detection, using these 2 approaches on particular videos and image folders. This practical implementaion is done by: By [Smeu Stefan](https://github.com/MrNiceGuy090), [Negulescu Radu-Andrei](https://github.com/radunegulescu).

## Pretrained models

Pretrained models to download in order to run the demo:

Model | Backbone | AP50 | AP (fast) | AP (med) | AP (slow) | Link
:---: | :---: | :---: | :---: | :---: | :---: |:---:
base | ResNet-101 | 76.7 | 52.3 | 74.1 | 84.9 | [Google](https://drive.google.com/file/d/1W17f9GC60rHU47lUeOEfU--Ra-LTw3Tq/view?usp=sharing)
**MEGA** | ResNet-101 | 82.9 | 62.7| 81.6 | 89.4 | [Google](https://drive.google.com/file/d/1ZnAdFafF1vW9Lnpw-RPF1AD_csw61lBY/view?usp=sharing)

## Prerequisites

Please follow [INSTALL.md](INSTALL.md) for installation instructions, in order to be able to run the demo.

### Demo Usage
Please follow [demo/README.md](demo/README.md) to see how to visualize the images or video.
