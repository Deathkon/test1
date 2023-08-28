

# Introduction

Havity project



# Usage

To use this template to start your own project:


# {{ Havty }}

# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone https://github.com/HavityLabs/Havity-site-.git
    $ cd Havity-site-
    
create environment:

    $ python -m venv venv

activate environment:

     $ venv\Scripts\activate
    
Install project dependencies:

    $ pip install -r requirements
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver
