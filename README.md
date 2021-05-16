# Transcribe recordings without having to pause and play it manually

>Also available in [spanish]() / También disponible en [castellano]().

Are you tired of transcribing recordings because you have to pause, minimize, copy, maximize, play, minimize, copy,...? Here is a nice solution:
A simple python script to watch a video or a recorded audio in VLC and pause and play it automatically. Perfect for students who have virtual lectures and have to copy the video/audio content. You can set the time of playing and the time you need to copy while is paused.

## Pre-Requirements
The explanation is done for Linux Systems. The script requiered at least python 2. You can know your version executing the command `python --version`. If you have `python`, `VLC` and `playerctl` installed in your system, go directly to [step 4](#item1).

## Installation
### 1.- First of all, make sure your system is update:
You can execute the following commands:
```
sudo apt update
```
and
```
sudo apt upgrade
```
### 2.- Install [pip](https://pypi.org/project/pip/) (recommended):
Use the command:
```
sudo apt-get install python-pip
```
or for Python 3:
```
sudo apt-get install python3-pip
```
### 3.- Installing playerctl and vlc
You need to install [playerctl](https://github.com/altdesktop/playerctl):
```
sudo apt-get install playerctl
```
and [VLC](https://www.videolan.org/):
```
sudo apt-get install vlc
```
<a name="item1"></a>
### 4.- Python Script
You can download `paustart.py` from this repository. Make sure to enter the video/audio path and to set the pause and play times that fit with you.

* To get the path of the video/audio you can execute the command `pwd` and copy it to the `line 18`, also, if your video/audio file's name is different to `video.mp4` you will have to replace it in `line 19`.
* If you want to set the pause duration, change `line 23`.
* If you want to set the playing duration, change `line 25`.

Once everything is set up, you can execute the script using the command:
```
python paustart.py
```
and do a transcription efficiently in time, not having to pause and play it manually every time :)



