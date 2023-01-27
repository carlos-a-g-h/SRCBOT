#!/usr/bin/bash

# PORT
sed -i "s/Listen 80/Listen $PORT/" /etc/apache2/ports.conf
/etc/init.d/apache2 start
python3 wait.py
while true
do
	sleep 1
	python3 -m main
done
