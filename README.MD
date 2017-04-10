# TEST CASE / FOR DVEBUKVY

This project is scaffolded by Ivan Semernyakov <direct@beatum-group.ru>

## Architecture

Tested on:

* Ubuntu 14.04
* PostgreSQL 9.6.1

## Usage

Read article if needed: https://www.rosehosting.com/blog/install-elasticsearch-on-ubuntu-14-04/

#### Clone project:
```
$ mkdir testproject && cd $_
$ git clone https://github.com/beatum/djangorest_and_elasticserch.git
$ cd djangorest_and_elasticserch
```

#### Initialize ```virtualenv``` if needed:
```
$ virtualenv {path}
```

#### Activate ```virtualenv```:
```
$ source {virtualenv_path}/bin/activate
```

#### Install ```pip``` dependencies using ```./requirements.txt``` they are not already installed:
```
$ pip install -r requirements.txt
```

#### Verify ```pip``` dependencies installed correctly under ```virtualenv```:
```
$ which django-admin.py
```

#### Configure PostgreSQL if needed:
```
$ sudo su postgres
$ createuser -P username
$ createdb --owner username dbname
$ exit
```

Check up settings.py !

#### Apply initial migration:
```
$ ./manage.py migrate
```

#### Create admin user:
```
$ ./manage.py createsuperuser
```

#### Create new article with command:
```
$ ./manage.py create_article 1000
```

#### Rebuild index
```
$ ./manage.py rebuild_index
```

#### Collect Static
```
$ ./manage.py collectstatic
```


#### Test dev environment.
```
$ ./manage.py runserver
```

Now you can go to the localhost:8000 and you should see "Hello, World!" - page.

Search and test the API...

### That's all! Good luck!

## License

This software is released under the [MIT License](http://opensource.org/licenses/MIT).

