#!/bin/bash

mkdir -p ~/scripts/security_check
cd ~/scripts/security_check
sudo md5sum /etc/crontab > cron_checksum.md5
sudo md5sum /etc/ssh/sshd_config > sshd_checksum.md5
sudo md5sum ~/.ssh/authorized_keys > ssh_checksum.md5
sudo md5sum /etc/passwd > passwd_checksum.md5



