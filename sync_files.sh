#!/bin/bash

# Author: John Carter
# Created: 2021/07/04 17:57:02
# Last modified: 2021/07/06 09:21:06

GRN=$'\e[1;32m'
END=$'\e[0m'

echo "[${GRN}INFO${END}] Copying data...."
git pull
cp -r website/ /home/john/

echo "[${GRN}INFO${END}] Restarting service...."
systemctl restart website.service
systemctl status website.service