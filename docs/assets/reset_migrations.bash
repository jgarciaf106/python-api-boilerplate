rm -R -f ./migrations &&
pipenv run init &&
psql -U gitpod -c 'DROP DATABASE inventory;' || true &&
psql -U gitpod -c 'CREATE DATABASE inventory;' &&
psql -U gitpod -c 'CREATE EXTENSION unaccent;' -d inventory &&
pipenv run migrate &&
pipenv run upgrade