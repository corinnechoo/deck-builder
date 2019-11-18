# Deck Builder Backend App

This is a card selection app for the game Hearthstone. It generates 30 cards picked randomly from the Rastakhan’s Rumble expansion pack given one of the following player class - Druid, Hunter, Mage, Paladin, Priest, Rogue, Shaman, Warlock, Warrior, Neutral, and no more than 2 cards are repeated. 

The assumption that the field 'name' is used to differentiate whether cards are the same is made based on preliminary analysis, since this field does not contain null values. In addition, since the data does not contain null values for the fields dbfId, name, playerClass, cardId, cardSet and cardType, it is assumed that all cards must have these fields. 

The database populated with all fields given in the raw dataset, though in the future we may only want to store important columns.

The X-Mashape-Key required for retrieving the raw data is stored in a .env file as HEARTHSTONE_KEY.


## Running Tests Locally
```
$ DJANGO_SETTINGS_MODULE="deck.settings_test" python manage.py test deck 
```

## Running Locally

```
$ heroku git:clone -a damp-lowlands-95607
$ cd damp-lowlands-95607

$ pipenv shell
$ pip install -r requirements.txt

$ createdb damp-lowlands-95607

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local:run python manage.py migrate
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku
```
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```