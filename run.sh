#!/usr/bin/bash

# PORT
sed -i "s/Listen 80/Listen $PORT/" /etc/apache2/ports.conf
/etc/init.d/apache2 start
mkdir -p /var/wwww/html/
touch /var/wwww/html/log.txt
python3 -m main
