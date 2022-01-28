#!/bin/bash

mkdir -p ~/scripts/security_check
cp secure_metrics.py ~/scripts/security_check/ 
cp secure_metrics.sh ~/scripts/security_check/
sudo cp secure_metrics.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl start secure_metrics.service
sudo systemctl enable secure_metrics.service
sudo systemctl status secure_metrics.service
