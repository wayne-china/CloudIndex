#!/bin/bash


ps -ef |grep nginx |awk '{ print  $2 }' | sudo xargs kill -9 |sudo /usr/local/nginx/nginx
