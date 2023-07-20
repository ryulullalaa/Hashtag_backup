#!/bin/bash

# GitHub 저장소 클론
git clone https://github.com/ryulullalaa/Hashtag_backup.git

# 필요한 패키지 업데이트 및 설치
sudo apt update
sudo apt install -y nginx php-fpm mysql-server php-mysql

# MySQL 설정
sudo mysql_secure_installation

# PHP-FPM 설정
sudo sed -i 's/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/' /etc/php/*/fpm/php.ini

# Nginx 설정
sudo rm /etc/nginx/sites-available/default
sudo cp nginx-php-mysql/nginx.conf /etc/nginx/sites-available/default

# 서비스 재시작
sudo service nginx restart
sudo service php*-fpm restart
