Run the code like this:

*python face_detect.py abba.png haarcascade_frontalface_default.xml*

If you want to understand how the code works, the details are here:

https://realpython.com/blog/python/face-recognition-with-python/

Update: Now supports OpenCV3. This change has been made by furetosan ( https://github.com/furetosan) and tested on Linux.

To run the OpenCV3 version, run `facedetect_cv3.py`

Replace faces in single image:

```
python face_replace.py abba.png replacement.png haarcascade_frontalface_default.xml
```

Convert video to images (frames) + audio and vice versa:

```
bin/strip video.mp4 video/frames video/audio.aac
bin/combine video/out video/audio.acc out.mp4
```

Todo:

* Replace faces in directory
