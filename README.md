# Test for Stackt

### For local deploy
```
virtualenv venv
. venv/bin/activate
pip3 install -r backend/requirements/req_base.txt
python3 backend/manage.py migrate --settings=settings.local
```
#### Linting
```
flake8 backend --exclude=migrations
```

#### Run tests
```
python3 backend/manage.py test apps.core.tests.OrderTestCase --settings=settings.local
```
#### Run local server
```
python3 manage.py runserver --settings=settings.local
```
### Run production deploy
```
docker-compose -f docker-compose-deploy.yaml build
docker-compose -f docker-compose-deploy.yaml up
```
### Special rules for coding
* Please use black just for your file where you made edit.
* Don't use for migrations  
```
black some_file.py
```
