AI code for Person_Detection
Hello Micheal, I prepare a small project for you which is to detect human at real time. The main aim of the project is to detect face of a human at real time whenver the person is driving a car or a boat. We have used two model. HAAR CASCADE CLASSIFIER and SSDMOBILENET. To train and check the inference of a model, w just train it using some images and get the accurate results. Here i am explaining how to test and run it by yourself.

Python Installation for UBUNTU:
1.Open the terminal through search box via Ctrl+Alt+T or searching for “Terminal” from app launcher. When it opens, run command to add the PPA:
**$sudo add-apt-repository ppa:jonathonf/python-3.6**

2. Then check updates and install Python 3.6 via commands:

**$sudo apt-get update**
**$sudo apt-get install python3.6

Now you have three Python versions, use python command for version 2.7, python3 for version 3.5, and/or python3.6 for version 3.6.1.
3. To make python3 use the new installed python 3.6 instead of the default 3.5 release, run following 2 commands

**$sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.5 1
$sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 2

Finally switch between the two python versions for python3 via command:

**$sudo update-alternatives --config python3

After selecting version 3.6:

**$python3 -V

4.Use the following command to install pip for Python 3:
**$sudo apt install python3-pip


Install Important Libraries:
Now, we have successfully installed python on our system, next thing we do is to install the pre-requisite libraries. The libraries required for testing are follows:

OpenCv:
**$pip3 install opencv-python

NumPy:
**$pip3 install numpy


Imageio:
**$pip3 install imageio

Pytorch:
**$pip3 install --no-cache-dir torch-scatter
$pip3 install --no-cache-dir https://download.pytorch.org/whl/cpu/torch-1.1.0-cp36-cp36m-linux_x86_64.whl
$pip3 install --no-cache-dir https://download.pytorch.org/whl/cpu/torchvision-0.3.0-cp36-cp36m-linux_x86_64.whl

Running the demo:
Now, we have successfully installed python, pip, required libraries. Base has been setted up, now we are good to go to get the demo run, just unzip code_face or clone the repo using;
**$git clone repo link** 
 Just go the directory,
**$cd code_face
$python3 face_and_eyes.py

Here’s the result:


This is the demo for HAARCASCADE,

For SSD:,

**$cd ..
**$cd __pycache__
**$python3 code.py
