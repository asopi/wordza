# wordza - the vocabulary tool

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Technologies](#technologies)
4. [Installation](#installation)
5. [Collaboration](#collaboration)
6. [Code Style Guide](#codestyleguide)

### Introduction

Derived from the initial situation that students in foreign language modules often lack certain vocabulary, wordza will be developed.
It is a learning application which focuses especially on the translation of individually created vocabulary lists.

## Features
* Accounts: User registration and login
* Dashboard: Overview of learn sets and progress
* Vocabularies: User is able to generate vocabulary lists 
* Learn sets: User is able to combine several vocabulary lists and learn them with flipping cards

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

How the team collaborated throughout the project:

* Versioning:
The source code is managed in a public git repository on GitHub. 
This repository contains the django project and ensures that all developers have the same state of the source code. 
* Approach:
Each team member has a local copy of the remote GitHub repository. 
The Repository includes two main branches called master and develop, the master is used to hold a stable state of the application whereas the develop branch is needed for development and testing purposes. 
For every feature or bugfix, a new branch will be checked out from the develop branch. All changes are recorded with meaningful commit messages, following the principle of "commit early, commit often".
* Pull Request:
The pull request workflow ensures that each change is subject to a code review by another team member. 
This ensures a consistently high quality.

##Code Style Guide

PEP8:
Compliance with these guidelines is automatically checked in the development environment and during the deployment process using Pylint.
