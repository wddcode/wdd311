Quickstart Session
##################

.. seealso::

   Course  `slides <http://wdd.ohrstrom.ch/presentations/5/>`_  and
   `github project <https://github.com/wddcode/wdd311>`_.
        

        
easy_install & PIP
******************


Install PIP
===========

`pip` is a tool for installing and managing Python packages, such as
those found in the `Python Package Index <http://pypi.python.org/pypi>`_. It's a replacement for
`easy_install <http://peak.telecommunity.com/DevCenter/EasyInstall>`_.

::

    sudo easy_install PIP


Install virtualenv
==================

`virtualenv <http://www.virtualenv.org/>`_ is a tool to create isolated Python environments.

The basic problem being addressed is one of dependencies and versions, and indirectly permissions. 
Imagine you have an application that needs version 1 of LibFoo, but another application requires version 2. 
How can you use both these applications? If you install everything into ``/usr/lib/python2.7/site-packages`` 
(or whatever your platform’s standard location is), it’s easy to end up in a situation where you 
unintentionally upgrade an application that shouldn’t be upgraded.

::

    sudo pip install virtualenv
    
    
Using virtualenv
****************

Assuming your code lives in ``~/code/`` and environments should be in ``~/srv/``
(and the project/enviroment are named **wddtest**)

::
    
    # creating the env
    virtualenv ~/srv/wddtest

    # using the env
    source ~/srv/wddtest/bin/activate
    
    # test:
    which python
    
    # should output something like: /Users/ohrstrom/srv/wddtest/bin/python
    # (and not: /usr/bin/python)
    
    # deactivate virtualenv
    deactivate

