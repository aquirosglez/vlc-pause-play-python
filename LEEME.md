# Transcribe grabaciones sin tener que estar pausando y reproduciendolo manualmente todo el tiempo.

>También disponible en [inglés](./README.md) / Also available in [English](./README.md).

¿Estás cansado de transcribir grabaciones porque tienes que estar pausándo, minimizando, copiando, maximizando, reproduciendo, volviendo a minimizar, seguir copiando,...? Aquí tienes una solución:
Un script de python para ver en VLC videos o audios grabados, pudiendolos pausar y reproducir automáticamente. Es perfecto para estudiantes que tienen clases virtuales y deben copiar el contenido que les expone el profesor, siendo imposible transcribirlo al tiempo de reproducción (incluso reduciendo la velocidad). Con este script podrás ajustar el tiempo de reproducción y el de pausa que necesitas para copiar.

## Pre-requisitos
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
    ```python
    path='PATH'
    proccess = subprocess.Popen(['vlc', path + 'video.mp4'])
    ```
* If you want to set the pause duration, change `line 23`. In this example it is 4 seconds.
    ```python
    time.sleep(4)
    ```
* If you want to set the playing duration, change `line 25`. In this example it is 3 seconds.
    ```python
    time.sleep(3)
    ```

Once everything is set up, you can execute the script using the command:
```
python paustart.py
```
and do a transcription efficiently in time, not having to pause and play it manually every time :)





