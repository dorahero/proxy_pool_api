#!/bin/bash
docker run --rm --network mongo_proxy_network dorahero2727/proxy_scrapy:v1 crawl proxy && \
docker run --rm --network mongo_proxy_network dorahero2727/proxy_checker:v1 
