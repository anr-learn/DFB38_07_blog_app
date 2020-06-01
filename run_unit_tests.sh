#!/bin/bash

help()
{
	echo ' '
	echo 'Use:  1. run_unit_tests.sh  '
	echo 'Use:  2. run_unit_tests.sh   <TESTNAME>'
	#echo 'Use:  3. run_unit_tests.sh   <TESTNAME>'
	echo 'where'
	echo 'case 1: run all unit tests'
	echo 'case 2: run the specific test'
	#echo 'case 3: run tests matching a pattern'
	echo ' '
	echo 'EXAMPLES:'
	echo 'Case 1: Run all tests:'
	echo '  run_unit_tests.sh'
	echo 'Case 2:  Run "test_01() in class HomePageViewTest in mb_posts.app.tests/'
	echo '  run_unit_tests.sh  mb_posts_app.tests.HomePageViewTest.test_01'
	echo ' '
	exit 1
}


if [ "$1" = "-h" ] ; then
	echo 'found h'
	help
	exit 1
fi
if [ "$1" = "--help" ] ; then
	echo 'found help'
	help
	exit 1
fi

echo \
"python3 manage.py test  $*"
 python3 manage.py test  $*

### end ###
