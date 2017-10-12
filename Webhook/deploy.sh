#!/bin/bash

WEB_PATH=$1
WEB_USER='root'
WEB_USERGROUP='root'

echo "Start deployment" >> /var/log/deploy.log
cd $WEB_PATH
echo "pulling source code..."
git reset --hard origin/master >> /var/log/deploy.log
git clean -f
git pull
git checkout master
echo "changing permissions..." >> /var/log/deploy.log
chown -R $WEB_USER:$WEB_USERGROUP $WEB_PATH
echo "Finished." >> /var/log/deploy.log