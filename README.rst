Appsembler wrapper for Mayan
============================

This project is an example of how to create a wrapper for deploying Mayan using Appsembler.

Cloning this repo
-----------------

Since this project uses Git submodules, you should clone it using ``--recursive``::

    $ git clone --recursive git://github.com/appsembler/mayan_appsembler.git
 
If you need to update the code from this repository, you simple run these commands::

    $ git submodule init
    $ git submodule update

The project consists of:

 * stackato.yml
 * wsgi.py
 * requirements.pip (these are install automatically by pip)
 * appsembler_settings.py (necessary overrides)
 * manage.py (loads appsembler_settings instead of settings)
 * mayan (this is checked out as a git submodule - see below)

Copy appsembler_settings file
-----------------------------

Copy the appsembler_settings.py file into the ``mayan`` directory::

    $ cp appsembler_settings.py mayan

Copy the manage.py file into the ``mayan`` directory::

    $ cp manage.py mayan

Copy the settings overriding file into the ``mayan`` directory::

    $ cp settings_local.py mayan 
    
This will be done automatically by our web-based deploy process, but when using the command line, it needs to be done manually.

Deploying to Appsembler
-----------------------

You can deploy this app to Appsembler with just a few commands. First download the Stackato command line tool from http://community.activestate.com/stackato/download

Edit the ``mysql-mayan`` entry in stackato.yml, and give your MysQL service a unique name::

    services:
        mysql: mysql-yourappname

From the ``mayan_appsembler`` directory, deploy with these commands::

    stackato target api.appsembler.com
    stackato login --email name@domain.com --password *****
    stackato push yourappname --url yourappname.appsembler.com -n

Substitute ``yourappname`` with whatever you want to call your Mayan app instance.
Substitute ``name@domain.com`` with your email address.

The next time you need to deploy, you use the update command::

    $ stackato update -n
