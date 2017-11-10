#!/bin/sh

set -e

# clean
RESULT_DIR=$(pwd)"/test-results"
rm -rf ${RESULT_DIR}
mkdir -p ${RESULT_DIR}

result_name=xunit.xml
coverage_name=xcoverage.xml

# test
nosetests --verbosity=3 \
--cover-package=scarlett --cover-erase \
--with-xcoverage --with-xunit \
--xunit-file=${RESULT_DIR}/${result_name} \
--xcoverage-file=${RESULT_DIR}/${coverage_name} \
tests
