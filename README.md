# Python-IPLocation
This code repository allows the tracking of IP addresses with UDP and SKYPE 
protocols using the Tshark packet parser on MacOS platform with Python.

## Installation
Firstly, WireShark package parser must be downloaded, as the program runs through the Tshark package parser.
If you haven't downloaded the brew package management system, you can download it from https://brew.sh

```shell
# Install Wireshark with brew
$ brew install --cask wireshark
```

**Be sure to use the same version of the code as the version of the docs you're reading.**
You probably want the latest tagged version, but the default Git version is the master branch.

```shell
# clone the repository
$ git clone https://github.com/furkankyildirim/Python-IPLocation
$ cd Python-IPLocation
# checkout the correct version
$ git tag
```

Create a virtualenv and activate it:
```shell
$ python3 -m venv venv --without-pip
$ source venv/bin/activate
```

Install pip3 requirements
```shell
$ pip3 install -r requirements.txt
```

## Run
```shell
$ source venv/bin/activate
$ python3 main.py
```
When the program starts, it reflects the IP address, coordinates and open address
of the other user to the console in video chat services such as Omegle.
