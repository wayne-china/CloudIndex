#!/bin/bash


ps -ef |grep python  |awk '{ print  $2 }' | sudo xargs kill -9 |sudo python ./application.py --port=8000|sudo python ./application.py --port=8001|sudo python ./application.py --port=8002|sudo python ./application.py --port=8003;
