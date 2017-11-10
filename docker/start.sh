#!/bin/bash -e

export NEW_RELIC_CONFIG_FILE=/newrelic.ini

case $1 in
  "run")
    shift
    newrelic-admin run-program gunicorn app:app --bind ${HOST:-0.0.0.0}:${PORT:-8080} --worker-class sanic.worker.GunicornWorker -w 3 --access-logfile=- "$@"
    ;;
  "test")
    ./test.sh "$@"
    ;;
  *)
    echo "usage: $0 [run]"
    exit 1
    ;;
esac
