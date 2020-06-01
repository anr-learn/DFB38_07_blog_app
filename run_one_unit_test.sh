#!/bin/bash
#
# Run one (or more) unit tests, one at a time

for tst in $* ; do
	echo ' '
	echo 'Run unit test ' $tst
    python3 manage.py  test  blog05_app.tests.BlogTests.$tst
done

### end ###
