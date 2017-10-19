FROM python:3.6-alpine

# app workdir
WORKDIR /app

# copy app dependencies
COPY requirements.txt docker/*.sh ./
COPY docker/newrelic.ini /newrelic.ini

# install dependecies
RUN apk add --update bash git build-base \
    && pip install -r ./requirements.txt --upgrade \
    && pip install gunicorn --upgrade \
    && pip install newrelic --upgrade \
    && apk del --purge git build-base \
    && rm -rf /root/.cache/pip/* \
    && rm -rf /var/cache/apk/*

# build app source code
COPY . ./

# Default runtime configs
EXPOSE 8080
ENTRYPOINT ["./start.sh"]
CMD ["run"]

