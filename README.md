# Transcribe recordings without having to pause and play it manually

Are you tired of transcribing recordings because you have to pause, minimize, copy, maximize, play, minimize, copy,...? Here is a nice solution:
A simple python script to watch a video or a recorded audio in VLC and pause and play it automatically. Perfect for students who have virtual lectures and have to copy the video/audio content. You can set the time of playing and the time you need to copy while is paused.

## Pre-Requirements
The explanation is done for Linux Systems. The script requiered at least python 2. You can know your version executing the command `python --version`. Despite the explanation is for Linux distributions, you can use the script if you have python, VLC and playerctl installed in your system (go directly to [step 4](#item1) ).

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




