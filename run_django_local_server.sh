#

if [ "$PIPENV_ACTIVE" != "1" ] ; then
	echo '*ERROR* You forgot to run:'
	echo '            pipenv shell'
	exit
fi


python manage.py runserver

###
