from prometheus_client import CollectorRegistry, Gauge, push_to_gateway
import time
import socket
import subprocess
from pathlib import Path

home = str(Path.home())
push = '192.168.1.111:9091'

# host IP
#IP = socket.gethostbyname(socket.gethostname()) 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("gmail.com",80))
IP = s.getsockname()[0]
s.close()


#print(res)

while True:

# crontab
    cmd_cron = subprocess.run(['md5sum', '-c', home+'/scripts/security_check/cron_checksum.md5'], stdout=subprocess.DEVNULL)

    # receive sddout or stderr
    if cmd_cron.returncode == 0:
        res_cron = 0
    else:
        res_cron = 1

    registry = CollectorRegistry()

    g = Gauge('security_metrics_crontab', 'Description metric', registry=registry)
    g.set(res_cron)
    push_to_gateway(push, job=IP, registry=registry)

# sshd_conf
    cmd_sshd = subprocess.run(['md5sum', '-c', home+'/scripts/security_check/sshd_checksum.md5'], stdout=subprocess.DEVNULL)

    if cmd_sshd.returncode == 0:
        res_sshd = 0
    else:
        res_sshd = 1

    g2 = Gauge('security_metrics_sshd', 'Description metric', registry=registry)
    g2.set(res_sshd)
    push_to_gateway(push, job=IP, registry=registry)

# authorized_keys
    cmd_ssh = subprocess.run(['md5sum', '-c', home+'/scripts/security_check/ssh_checksum.md5'], stdout=subprocess.DEVNULL)

    if cmd_ssh.returncode == 0:
        res_ssh = 0
    else:
        res_ssh = 1

    g3 = Gauge('security_metrics_ssh', 'Description metric', registry=registry)
    g3.set(res_ssh)
    push_to_gateway(push, job=IP, registry=registry)

# passwd
    cmd_passwd = subprocess.run(['md5sum', '-c', home+'/scripts/security_check/passwd_checksum.md5'], stdout=subprocess.DEVNULL)

    if cmd_passwd.returncode == 0:
        res_passwd = 0
    else:
        res_passwd = 1

    g4 = Gauge('security_metrics_passwd', 'Description metric', registry=registry)
    g4.set(res_passwd)
    push_to_gateway(push, job=IP, registry=registry)


    time.sleep(10)









c
