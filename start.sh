#!/bin/bash
export DOCKER_HOST="tcp://172.16.16.139:2375"
docker run --rm --network proxy_pool_automation_proxy_network dorahero2727/proxy_scrapy:v1 crawl proxy # && \
# docker run --rm --network proxy_pool_automation_proxy_network dorahero2727/proxy_checker:v1 > /home/red/proxy_pool/log.txt 
