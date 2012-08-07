The Shell
#########

.. seealso::

   Course  `Learn UNIX in 10 minutes. Version 1.3  <http://freeengineer.org/learnUNIXin10minutes.html>`_.
        

        
Basics
******


Directories
-----------

File and directory paths in UNIX use the forward slash "/" 
to separate directory names in a path.

Examples
""""""""

Change to your home folder. Same as ``cd ~/`` or ``cd /Users/<yourusername>/``

::

    cd

::

    cd ~/code/

::

    cd ~/Desktop
  
etc


Listing
-------

``man ls`` to show all options :)

Examples
""""""""

::

    # list current directory | ls: "list"
    ls

::

    # long format | ls: "list long"
    ls -l

::

    # show hidden files | ls: "list long and show all"
    ls -la

::

    # list specific folder
    ls -l ~/code/



Viewing files
-------------


Examples
""""""""


::
    
    # dump file content
    cat file.txt

::

    # progressive dump, "spachebar" = down, "q" = quit
    more file.txt

    
::

    # like dump, additional up/down with cursor
    less file.txt

    
::

    # shows the last few lines of a file
    tail file.txt
    
    # usefull to watch logfiles.. -f for "follow"
    tail -f /var/log/system.log
    tail -f /var/log/apache2/access.log



OS X specific
-------------


Examples
""""""""


::
    
    # open current directory in finder
    open .
    
    # open specifyed directory in finder
    open ~/code/wdd311
    
    # open any file with default application
    open documentation.pdf
    open archive.zip
    
etc


.. note::

   You always can drag-n-drop files and folders from the finder to the console!


  