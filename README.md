* Face Detection & Replacement *

Original face detection https://realpython.com/blog/python/face-recognition-with-python/
Face replacement idea http://stackoverflow.com/questions/14063070/overlay-a-smaller-image-on-a-larger-image-python-opencv
Original video-image conversion https://github.com/matthewfranglen/face-replace-python

Dependencies
* Python 2 (>= 2.7)
* OpenCV 2 (and OpenCV 3 for face detection)
* FFMPEG (for video-image conversion)

** Face detection **

Detect faces in single image. Usage:
```
python face_detect.py [image] [xml config]
```
Example:
```
python face_detect.py abba.png haarcascade_frontalface_default.xml
```

** Face Replacement **

Replace faces in single image. Usage:
```
python face_replace.py [image] [replacement image] [xml config]
```
Example:
```
python face_replace.py abba.png replacement.png haarcascade_frontalface_default.xml
```
The output file will be in `[image name].merged.[image ext]`

Replace faces in multiple images in a directory. Usage:
```
python face_replace_multi.py [xml config] [replacement image] [input dir containing images] [output dir]
```
Example:
```
python face_replace_multi.py haarcascade_frontalface_default.xml replacement.png video/frame/ video/merged/
```

** Video-Image Conversion **

Convert video to images (frames) + audio. Usage:
```
bin/strip [video input] [images output dir] [audio ouput file path]
```
Example:
```
bin/strip video.mp4 video/frame video/audio.aac
```

Convert images + audio to video. Usage:
```
bin/combine [images input dir] [audio input file path] [output video]
```
Example:
```
bin/combine video/merged video/audio.acc out.mp4
```
