#!/bin/bash

# Author: John Carter
# Created: 2021/07/04 17:57:02
# Last modified: 2021/07/19 20:30:16

GRN=$'\e[1;32m'
END=$'\e[0m'

echo "[${GRN}INFO${END}] Copying data...."
cd website
git pull
cd ..
cp -r website/ /home/john/

echo "[${GRN}INFO${END}] Restarting service...."
systemctl restart website.service
systemctl status website.service