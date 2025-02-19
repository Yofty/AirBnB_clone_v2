#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y install nginx
echo -e "\e[1;32m Packages updated\e[0m"
echo

sudo ufw allow 'Nginx HTTP'
echo -e "\e[1;32m Allow incomming NGINX HTTP connections\e[0m"
echo

sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
echo -e "\e[1;32m directories created"
echo

echo "<h1>Welcome to www.yoftynet.tech</h1>" > /datat/web_static/release/test/index.html
echo -e "\e[1;32m Test string added\e[0m"
echo

if [ -d "/data/web_static/current"];
then
	echo "path /data/web_static/current exists"
	sudo rm -rf /data/web_static/current;
fi;
echo -e "\e[1;32m prevent overwrite\e[0m"
echo


sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data

sudo sed -i '38i\\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}n' /etc/nginx/sites-enabled/default

sudo ln -sf '/etc/nginx/sites-available/default' '/etc/nginx/sites-enabled/default'
echo -e "\e[1;32m Symbolic link created\e[0m"
echo

sudo service nginx restart
echo -e "\e[1;32m restart NGINX\e[0m"
