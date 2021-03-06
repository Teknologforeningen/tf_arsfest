Development
==========

Ubuntu
-------

Install pip and python-dev:
```
sudo apt-get install python-pip python-dev
```

Install virtualenv:
```
sudo pip install virtualenv
```

Clone the repository:
```
git clone https://github.com/Teknologforeningen/tf_arsfest.git && cd tf_arsfest/
```

Set up virtualenv:
```
virtualenv --no-site-packages venv
```

Activate virtualenv:

You will need to run this every time you open a terminal to run the service in order to use the isolated virtual environment.

```
source venv/bin/activate
```

Install dependencies:
```
pip install -r requirements.txt
```

Copy local settings:
```
cp tf_arsfest/local_settings_example.py tf_arsfest/local_settings.py
```

Sync db:
```
python manage.py syncdb
```

Migrate db:
```
python manage.py migrate
```

Deploying
----------

To deploy the service edit the fabfile.py with your information and run:
```
fab webserver deploy
```

Credits
=========
This project uses the Twitter Bootstrap framework:
http://twitter.github.com/bootstrap/
