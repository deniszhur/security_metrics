#!/bin/bash

# sudo apt-get update --fix-missing
sudo apt-get update -y 
sudo apt-get install -y python3-pip
pip install prometheus_client
pip install pathlib

