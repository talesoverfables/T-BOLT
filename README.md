# T-BOLT : Traffic Bottleneck Out-tracing Logical Tech-Assistant!
<br>Imagine a police officer wearing an AR headset or using a smartphone or tablet with AR capabilities. As the officer walks or drives through the city, the webapp displays real-time information about traffic congestion, parking issues, encroachment of roads and footpaths, and poor road conditions. The AR experience is overlaid on the real world, allowing the officer to see the actual environment with additional valuable information.</br>
## Project Highlights
- Augmented Reality Visual Cues of every bottleneck.
- WebApp with multiple webpages that indicate - Civilian Reports of bottlenecks, Accidents bottlenecks, alerts.
- Integration with Maps for easier nagivation by Police Personnel.
- Pre-trained AI model for traffic and road condition detection.
<br></br>

## Installation
1. Clone this repository to your local machine using:

```bash
git clone https://github.com/talesoverfables/T-BOLT.git
```
2. Navigate to the project directory:

```bash
cd T-BOLT
```
3. Install the required dependencies from `requirements.txt` using pip:
```
pip install -r requirements.txt
```
4. Clone this repository using `git clone` and deploy using the command:
```bash
streamlit run Homepage.py
```

## Architechture
<img width="500" alt="50" src="https://github.com/talesoverfables/T-BOLT/blob/main/TBOLT-%20Architechture.png">

## Homepage
<img width="900" alt="101" src="https://github.com/talesoverfables/T-BOLT/blob/main/Homepage-101.png">

## Annotation
Annotated images using cvat.
![image](https://github.com/talesoverfables/T-BOLT/assets/166482014/78c025c3-08d8-493c-97f8-23c98214faeb)


## Traning
## YOLOv9 Bottleneck Detection with Traffic Custom Data
This repository contains code for training and testing YOLOv9 object detection models with custom data.

## Requirements
Python 3.7+
PyTorch 1.7.0+
CUDA 11.0+
OpenCV
scikit-image
tqdm
scipy
numpy

## Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/WongKinYiu/yolov9.gitcdyolov9
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Mount Google Drive and copy the custom data to the Colab environment:
   ```bash
   from google.colab import drive
   drive.mount("/content/gdrive")
   !scp "/content/gdrive/My Drive/bag/data.zip" "/content/data.zip"
   !unzip "/content/data.zip" -d "/content/"
   ```
4. Set the preferred encoding to UTF-8:
   ```bash
   import locale
   def getpreferredencoding(do_setlocale = True):
     return "UTF-8"
   locale.getpreferredencoding = getpreferredencoding
   ```
5. Clone the YOLOv9 repository and install the required packages:
   ```bash
   !git clone https://github.com/WongKinYiu/yolov9.git
   %cd yolov9
  !pip install -r requirements.txt -q
  ```
6. Set the home directory and check if CUDA is available:
   ```bash
   import os
   HOME = os.getcwd()
   print(HOME)
   import torch
   print(torch.cuda.is_available())
```
7.Create a directory for the weights and download the pre-trained weights:
   ```bash
   !mkdir -p {HOME}/weights
   !wget -P {HOME}/weights -qhttps://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9c.pt
   !wget -P {HOME}/weights -q https://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9-e.pt
```
8. Train the model:
   ```bash
    !python train_dual.py --workers 8 --device 0 --batch 8 --data '/content/gdrive/My Drive/bag/data.yaml' --img 320 --cfg models/detect/yolov9-e.yaml --weights 
   '{HOME}/weights/yolov9-e.pt' --name yolov9-e-finetuning --hyp hyp.scratch-high.yaml --min-items 0 --epochs 100 --close-mosaic 15
   ```
9. Copy the video file to the Colab environment:
    ```bash
    !scp "/content/gdrive/MyDrive/bag/video.mp4"  '/content/video.mp4'
    ```
10. Detect bottlenecks in the video:
    ```bash
    !python detect_dual.py --source '/content/video.mp4' --img 640 --device 0 --weights '/content/yolov9/runs/train/yolov9-e-finetuning/weights/best.pt' --name 
    yolov9_ppe_640_detect --vid-stride 2
    ```
11. Copy the detected video to Google Drive:
    ```bash
    import shutil
    shutil.copy("/content/yolov9/runs/detect/yolov9_ppe_640_detect2/video.mp4", "/content/gdrive/MyDrive")
    ```

## Training data
![WhatsApp Image 2024-04-13 at 14 31 01_29a396ea](https://github.com/talesoverfables/T-BOLT/assets/166482014/f2528488-5219-431e-80a5-cfe83321564b)
![WhatsApp Image 2024-04-13 at 14 35 13_36a958a2](https://github.com/talesoverfables/T-BOLT/assets/166482014/dd1ca622-7495-4d04-8d15-2a72960b4a73)



## Validation data
![WhatsApp Image 2024-04-13 at 21 26 23_df466136](https://github.com/talesoverfables/T-BOLT/assets/166482014/c981b40b-3f68-4447-8ff3-ddf3b77154f3)




## Results

https://github.com/talesoverfables/T-BOLT/assets/166482014/b6e7526b-f381-46fd-aff0-549fef85edd4




    

    
## More information about the project
Refer to [Our project Pitch](https://docs.google.com/presentation/d/1SfAv4E1dG_Os59Px8zseLoBFlciG5gAL7fWOfxQ8Lw8/edit#slide=id.g2cbb5c5073d_0_16)

## About us
We are Team Omega Cyborgs, four highly motivated and technologically-driven first-year engineering students who like solving problems using tech and its branches.
#SheCanCode
