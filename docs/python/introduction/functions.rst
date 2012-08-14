Python Funktionen & co
######################


Flow control statements
-----------------------

-  *if*
-  *for*
-  *while*

for
~~~

::

    # -*- coding: utf-8 -*-

    numbers = range(10)
    print numbers
    for number in numbers:
        # Prüfen ob in tuple vorhanden
        if number in (3, 4, 7, 9):
            # "Break"
            # Zurückspringen ohne "else" ausführen
            break
        else:
            # "Continue"
            # startet nächste Iteration
            # (unnötig hier, da letztes Statement..)
            continue
    else:
        # "Else"
        # optional, wird nur ausgeführt wenn der 
        # loop nicht "ge-break-t" wurde
        pass # Do nothing

while
~~~~~

::

    i = 0
    while i < 10:
        print i
        i += 1
        
        
        
        
        
        
        
Funktionen
----------

Lambda
~~~~~~

::

    my_function = lambda x, y: x + y
    my_function(2,2)
    # 4

def
~~~

::

    def my_function(x,y):
        return x + y

Defaults & named parameter
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    def my_function(x=1,y=1):
        return x / y

return
~~~~~~

::

    def my_function(x=1,y=1):
        return x / y, y /x
        
        
        
        
Argumente
---------

**\*args** & **\*\*kwargs**


\*args
~~~~~~

::

    def multy_add(farg, *args):
        print "formal arg:", farg
        sum = farg
        for arg in args:
            sum += arg
            print "another arg:", arg
        return sum

\*\*kwargs
~~~~~~~~~~

::

    def kw_function(farg, **kwargs):
        print "formal arg:", farg
        for key in kwargs:
            print "another keyword arg: %s: %s" % (key, kwargs[key])