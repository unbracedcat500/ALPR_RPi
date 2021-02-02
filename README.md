# ALPR_RPi Instructions 

## Follow th below Instructions to setup this project on your Raspberry Pi
### **Set the Environment**
```bash
    #make sure your username is  'pi'
    $ cd ~
    $mkdir Github
    $cd Github/
    $ git clone https://github.com/unbracedcat500/ALPR_RPi.git
    #yolov3.weights must be downloaded from https://pjreddie.com/media/files/yolov3.weights and saved in folder yolo-coco
  ```
### **Installation of Tensor Flow**
System requirements
* Python 3.5–3.8
  * Python 3.8 support requires TensorFlow 2.2 or later.
* Raspbian 9.0 or later

1. Install the Python development environment on your system

    Raspbian 10 comes with a python 3.7 pre-installed

2. Install required Packages

```bash
    $ cd ~
    $ sudo apt update
    $ sudo apt install python3-dev python3-pip python3-venv
    $ sudo apt install libatlas-base-dev         # required for numpy
# Create a virtual environment
    $ python3 -m venv --system-site-packages ./venv
# Activate the Virtual Environment
    $ source ./venv/bin/activate  # sh, bash, or zsh
  When the virtual environment is active, your shell prompt is prefixed with (venv).
# Upgrade pip
    (venv) $ pip install --upgrade pip
# Install the TensorFlow pip package
    (venv) $  pip install --upgrade tensorflow
```
### **Installation of OpenAlpr**
```bash
#Install prerequisites
    (venv) $ cd ~
    (venv) $ sudo apt install libopencv-dev libtesseract-dev git cmake build-essential libleptonica-dev

    (venv) $ sudo apt install liblog4cplus-dev libcurl3-dev

#If using the daemon, install beanstalkd
    (venv) $ sudo apt-get install beanstalkd

#Clone the latest code from GitHub
    (venv) $ git clone https://github.com/openalpr/openalpr.git

#Setup the build directory
    (venv) $ cd openalpr/src
    (venv) $ mkdir build
    (venv) $ cd build

#setup the compile environment
    (venv) $ cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr  -DCMAKE_INSTALL_SYSCONFDIR:PATH=/etc ..

#compile the library
    (venv) $ make

#Install the binaries/libraries to your local system (prefix is /usr)
    (venv) $ sudo make install

#Test the library
    (venv) $ wget http://plates.openalpr.com/h786poj.jpg -O lp.jpg
    (venv) $ alpr lp.jpg

#One necessary step
    (venv) cd openalpr/src/bindings/python/
    (venv) $ sudo python3 setup.py install

#Set Python path
    (venv) $ cd ~
    (venv) $ export PYTHONPATH=/home/pi/openalpr/src/bindings/python/openalpr
 
 #Below command should return the path if it is set properly   
    (venv)  $ echo $PYTHONPATH
```
### **Install OpenCV & PiCam**
```bash
    (venv) $ pip install opencv-python
    (venv) $ pip install picamera
    #make sure the camera module is  enabled. Check Raspberry pi configuration
```
### **Execute the program**
```bash
#Deactivate the virtual environment
    (venv) $ deactivate
    $ cd /home/pi/Github/ALPR_RPi/make_color/
    $ ./autovenv.sh
```
### **Run the program on startup**
```bash
    $ cd /etc/
    $ sudo nano rc.local
#Add the 2nd last line  above the  'exit0'  line
    ./home/pi/Github/ALPR_RPi/make_color/autovenv.sh &
#press ctrl X > y > Enter to save
