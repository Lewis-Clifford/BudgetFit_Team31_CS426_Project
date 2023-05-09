#!/bin/bash

sudo apt update
sudo apt autoremove
sudo apt autoclean
sudo apt install mysql-client-core-8.0
sudo apt install mysql-server

sudo mysqld_safe --skip-grant-tables --skip-networking &
mysql -u root
# FLUSH PRIVILEGES;
# ALTER USER 'root'@'localhost' IDENTIFIED BY '__password__';
# exit;

sudo systemctl start mysql
sudo systemctl status mysql.service
sudo journalctl -xeu mysql.service

sudo systemctl start mysql
echo $?
sudo /etc/init.d/mysql stop
sudo service mysql stop
sudo killall -KILL mysql mysqld_safe mysqld
sudo /etc/init.d/mysql start
sudo service mysql start
mysqladmin -u root password '__password__'
sudo mysql -u root -p
sudo service mysql stop
sudo su
mysqld_safe --skip-grant-tables &
sudo mkdir -p /var/run/mysqld
sudo chown mysql:mysql /var/run/mysqld
mysql
exit

mysql
sudo mysql -u $(whoami)

sudo su
mysql -u root -p
service mysql stop
mysqld_safe --skip-grant-tables &
# USE MYSQL;
# SELECT * FROM user;
# TRUNCATE TABLE user;
# FLUSH PRIVILEGES;
# CREATE USER 'root'@'localhost' IDENTIFIED BY '__password__';
# GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' WITH GRANT OPTION;
# SELECT host, user FROM user;
# QUIT;
ps ax | grep "mysqld_safe"
kill -KILL $pid
# repeated this a few times
# beware if discord interferes with this
/etc/init.d/mysql start
service mysql start
mysql -u root -p
# CREATE DATABASE test;
# DROP DATABASE test;
# exit
exit
