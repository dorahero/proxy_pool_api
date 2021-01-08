FROM python:3.6
COPY . /proxy_checker
WORKDIR /proxy_checker
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "checker.py" ]
