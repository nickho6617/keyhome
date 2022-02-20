# Django 4 boilerplate

Boilerplate django project for hobby projects

This is a boilerplate project for setting up quickly, its to my own preferences using
Django,
Postgres,
Django All Auth
debug_toolbar
docker
docker-compose

Some todos if you using this:
Packages versions are not pinned
You will need to setup an .env file for your secret keys and settings config.
Docker user has not been switched to non root

There is a make file inlcuded for brevity you can clone,
make build run docker-compose build
make up will run the web and postgres containers

There is an accounts app for allauth and custom user model and a pages app for static html which has the cdn version of bootstrap 5.
