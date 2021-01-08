#!/bin/bash
docker run --rm --network proxy_pool_automation_proxy_network dorahero2727/proxy_scrapy:v1 crawl proxy && \
docker run --rm --network proxy_pool_automation_proxy_network dorahero2727/proxy_checker:v1
