FROM python:3.6
COPY ./proxy_scraper /proxy_scraper
WORKDIR /proxy_scraper
RUN pip install -r requirements.txt
ENTRYPOINT [ "scrapy" ]
CMD []
