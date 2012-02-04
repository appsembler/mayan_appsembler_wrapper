Appsembler wrapper for Mayan
============================

This project is an example of how to create a wrapper for deploying Mayan using Appsembler.

The project consists of:

 * stackato.yml
 * wsgi.py
 * requirements.pip (these are install automatically by pip)
 * appsembler_settings.py (necessary overrides)
 * mayan (this is checked out as a git submodule - see below)

Copy appsembler_settings file
-----------------------------

Copy the appsembler_settings.py file into the ``mayan`` directory::

    $ cp appsembler_settings.py mayan

Copy the manage.py file into the ``mayan`` directory::

    $ cp manage.py mayan
    
This will be done automatically by our web-based deploy process, but when using the command line, it needs to be done manually.

Cloning this repo
-----------------

Since this project uses Git submodules, you should clone it using ``--recursive``::

    $ git clone --recursive git://github.com/appsembler/mayan_appsembler.git
 
If you need to update the code from this repository, you simple run these commands::

    $ git submodule init
    $ git submodule update

Deploying to Appsembler
-----------------------

You can deploy this app to Appsembler with just a few commands. First download the Stackato command line tool from http://community.activestate.com/stackato/download

Then you can deploy it the first time with::

    $ stackato target http://api.somedomain.com
    $ stackato login --email name@domain.com --password *****
    $ stackato push

The next time you need to deploy, you use the update command::

    $ stackato update
