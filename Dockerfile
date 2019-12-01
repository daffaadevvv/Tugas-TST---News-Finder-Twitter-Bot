FROM python:3

COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN pip3 install -r requirements.txt
RUN pip3 install feedparser
RUN pip3 install python-twitter

COPY . /

ENTRYPOINT [ "python3" ]

CMD [ "app/app.py" ]