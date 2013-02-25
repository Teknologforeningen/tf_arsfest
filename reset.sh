#!/bin/bash
rm tf_arsfest/sqlite.db 
python manage.py  syncdb
rm tf_arsfest/migrations/000*
python manage.py schemamigration tf_arsfest --initial
python manage.py migrate tf_arsfest
