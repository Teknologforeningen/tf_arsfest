Development
==========

Ubuntu
-------

Install pip:
'''
sudo apt-get install python-pip
'''

Install virtualenv:
'''
sudo pip install virtualenv
'''

Clone the repository:
'''
git clone git@github.com:Teknologforeningen/tf_arsfest.git && cd tf_arsfest/
'''

Set up virtualenv:
'''
virtualenv --no-site-packages venv
'''

Activate virtualenv:
'''
source venv/bin/activate
'''

Install dependencies:
'''
pip install -r requirements.txt
'''

Copy local settings:
'''
cp tf_arsfest/local_settings_example.py tf_arsfest/local_settings.py
'''

Sync db:
'''
python manage.py syncdb
'''

Migrate db:
'''
python manage.py migrate
'''



Credits
=========
This project uses the Twitter Bootstrap framework:
http://twitter.github.com/bootstrap/
