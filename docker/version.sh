#!/bin/bash

if [[ "$TRAVIS_PULL_REQUEST_BRANCH" == "" ]]; then
  if [[ "$TRAVIS_TAG" != "" ]]; then
    echo $TRAVIS_TAG; exit 0
  elif [[ "$TRAVIS_BRANCH" == "master" ]]; then
    echo $TRAVIS_BRANCH; exit 0
  elif [[ $TRAVIS_BRANCH =~ ^feature/ ]]; then
    echo ${TRAVIS_BRANCH#feature/}; exit 0
  fi
fi

echo "local"
