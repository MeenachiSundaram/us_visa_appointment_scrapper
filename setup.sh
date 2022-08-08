#!/bin/bash

repeat(){
	for i in {1..90}; do echo -n "$1"; done
    echo ""
}

echo_fn () {
    repeat =
    echo `date` - - $1
    repeat =
} 

echo_fn "Setting up supporting Directory and files"
WORK_DIR=`pwd`
mkdir -p ${WORK_DIR}/debugging
mkdir -p ${WORK_DIR}/archive
wget -q -O test.jpg https://unsplash.it/1920/1080/?random
mv test.jpg ${WORK_DIR}/archive

if [[ ! -f module/creds.py ]]
then
    echo_fn "'creds.py' does not exist creating now, replace the values in this file"
    cp module/creds.py.example module/creds.py
fi

echo_fn "Installing Chrome driver"
sudo apt-get install chromium-chromedriver

echo_fn "Installing Python Requirements"
pip install -r requirements.txt

echo_fn "Completed"