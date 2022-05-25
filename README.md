# Portland Solidarity In Action

#### By **Marisa Edgar**

#### A Community Media App which connects community organizations with community members in need and vice versa.


## Technologies Used

- Python
- Django
- Bulma
- HTML
- Pillow
- WhiteNoise

## Description

Portland Solidarity In Action (PSIA) is a new kind of media interface wherein the functionality for users is limited so that information from activists and community organizations can more easily share their events and programs. I am calling it a Community Media App. Stylistically like Instagram, the app focuses on presenting upcoming events to users, although messaging from user to user, user to org, and org to org will ultimately be possible.

## Setup/Installation Requirements

- Clone this repo to a project directory using the command _Git Clone https://github.com/marisa-edgar/psia_python_ in your command line interface.
- Check your version of Python using _Python --version_, and if none, or a deprecated version is installed, Install Version 3.10 of Python on your device using the Python installers on their website. *https://www.python.org*
- Install Pip for managing Python Packages using either Brew, or NPM. Follow this link for more information on Pip: *https://pip.pypa.io/en/stable/cli/pip_install/*
- Using the command line navigate to the root directory of the project and open it in your preferred code editor.
- Create a new Virtual Environment for the Python Project using the command _Python -m venv venv_. Then activate the environment with the command _venv/bin/activate_. You will know it is working correctly because (venv) will be beside your project pathway.
- Install Django 4.0.4 (or current version) to the virtual environment with the command _Python -m pip install Django==4.0.4_.
- Install Pillow with the command _Python -m pip install pillow_
- Install WhiteNoise with the command _Python -m pip install whitenoise_.
- Run the commands _Python manage.py collectstatic && Python manage.py makemigrations && Python manage.py migrate_.
- Run the program using _Python manage.py runserver_

## Known Bugs

- User Authentication not Fully Functional.
- Image link on Profile page broken.

## License

Licensed under the [MIT License](LICENSE).
Copyright (c) 2022 Marisa Edgar
