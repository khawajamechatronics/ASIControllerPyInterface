# BorealBike

## Getting the sources

This project uses git repository, thus before building the project ,do the following step

* **Clone the main project:** 

```shell 
git clone https://github.com/borealbikes-dev/ASIControllerPyInterface
```

## Supported operating systems

The server part can be build and executed on the following operating systems:

 * Linux
 * Windows
 

## Installation

Python versions 2.7 and higher are supported (including 3.x). Tested with Python 2.7, 3.2, 3.3 and 3.4. This module is pure Python.

**Installing the dependencies**

At the command line call:

```shell
sudo apt-get install python-pip python-dev build-essential 

sudo pip install --upgrade pip

```

**Installing serial-USB conventer driver:**

if you are using serial-Usb conventer, Just connect the device and it will be available. The commands lsusb and dmesg | tail (directly after plugging in the device) are your friends here.

Serial COM Ports are addressed as /dev/tty* (hardware serial COM ports) while USB serials (like the FTDI chip) appear as /dev/ttyUSB* when they are connected.

Personally I like moserial which is available in the repository. Install it like so:

```shell
sudo apt install moserial
```

**Installing minimal modbus**

Minimak modbus is a python library, could be installed by calling 

```shell
sudo pip install minimalmodbus
```

## Compiling 

MinimalModbus is an easy-to-use Python module for talking to instruments (slaves) from a computer (master) using the Modbus protocol, and is intended to be running on the master. Example code includes drivers for Eurotherm and Omega process controllers. The only dependence is the pySerial module (also pure Python).

Tested with Python 2.7, 3.2, 3.3 and 3.4.

change into cloned repository:

```shell
cd ASIControllerPyInterface
```

if you are using linux system call 

```shell
python2.7 linux.py
```

## Usage

check [here](https://minimalmodbus.readthedocs.io/en/master/usage.html#)
