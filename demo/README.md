# Demo Usage

Currently the demo supports visualization for:
- Image Folder: A set of frames that were decoded from a given video.
- Video: Only tested `.mp4` and `.avi`, but other video format should be OK.

## Inference on a image folder

The command line should be like this:
```shell
    python demo/demo.py ${METHOD} ${CONFIG_FILE} ${CHECKPOINT_FILE} [--visualize-path ${IMAGE-FOLDER}] [--suffix ${IMAGE_SUFFIX}][--output-folder ${FOLDER}] [--output-video]
``` 
Example for image folder:
```shell
    python demo/demo.py base configs/vid_R_101_C4_1x.yaml R_101.pth --suffix ".JPEG"\
        --visualize-path image_folder \
        --output-folder visualization [--output-video]
```
This will generate visualization result using single frame baseline with ResNet-101 backbone. And the results, images with generated bboxes, are saved in folder `visualization`. 

Please note that:
1) If your want to use the MEGA method, please change METHOD `base` to `mega`.
2) Don't forget to modify CONFIG_FILE from `configs/vid_R_101_C4_1x.yaml` to `configs\MEGA\vid_R_101_C4_MEGA_1x.yaml` and CHECKPOINT_FILE from `R_101.pth` to `MEGA_R_101.pth`!
3) Add `--output-video` to generate video instead of set of images, the video is encoded at `25` fps by default.
4) If you want to visualize your own image folder, please make sure that the name of your images is like `XXXXXX.jpg`. `XXXXXX` is the frame number of current frame, e.g., `000000` is the first frame. `.jpg` could be replaced by other common image suffix like `.png`, which could be specified by `--suffix.`

## Inference on a video

The command line should be like this:
```shell
    python demo/demo.py ${METHOD} ${CONFIG_FILE} ${CHECKPOINT_FILE} --video [--visualize-path ${VIDEO-NAME}] [--output-folder ${FOLDER}] [--output-video]
``` 
Example:
```shell
    python demo/demo.py base configs/vid_R_101_C4_1x.yaml R_101.pth --video \
        --visualize-path videos_folder/custom_video.mp4 \
        --output-folder visualization [--output-video]
```
This will generate visualization result using single frame baseline with ResNet-101 backbone. And the results, images with generated bboxes, are saved in folder `visualization`. 

Please note that:
1) All you should know about has given above.
