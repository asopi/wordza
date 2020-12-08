# wordza - the vocabulary tool

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
2. [Technologies](#technologies)
3. [Installation](#installation)
4. [Collaboration](#collaboration)

### Introduction

Derived from the initial situation that students in foreign language modules often lack certain vocabulary, wordza will be developed.
It is a learning application which focuses especially on the translation of individually created vocabulary lists.

## Features
* Accounts: 
* Dashboard: 
* Vocabularies: 
* Learn sets: 

## Technologies

A list of technologies used within the project:
* [Django](https://www.djangoproject.com): Version 3.1.2 
* [Python](https://www.python.org): Version 3.8.5
* [Bootstrap](https://getbootstrap.com): Version 4.5.3
* [Google Translate API](https://cloud.google.com/translate/): Version 1234

## Installation

A little intro about the installation of wordza.

First clone the repository from Github and switch to the new directory:

$ git clone https://github.com/asopi/wordza.git

$ cd wordza 

Activate the virtualenv for your project.

Install project dependencies:

$ pip install -r requirements.txt

Then simply apply the migrations:

$ python manage.py migrate

Create superuser (optional):

$ python manage.py createsuperuser

You can now run the development server:

$ python manage.py runserver

## Collaboration

Give instructions on how to collaborate with your project.
> Docu: Versionierung
> Beispiele