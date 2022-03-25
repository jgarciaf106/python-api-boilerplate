rm -R -f ./migrations &&
pipenv run init &&
sudo -u postgres psql postgres -c 'DROP DATABASE IF EXISTS example;' || true &&
sudo -u postgres psql postgres -c  'CREATE DATABASE example;' &&
sudo -u postgres psql postgres -c  'CREATE EXTENSION unaccent;' -d example
pipenv run migrate &&
pipenv run upgrade &&
pipenv run start