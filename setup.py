#!/usr/bin/env python

from distutils.core import setup
import py2exe
import sys

sys.argv.append('py2exe')

opts = dict( ascii=True,excludes=['pyreadline', 'difflib', 'doctest',
                                 'optparse', 'pickle', 'calendar', 'pbd',
                                  'unittest', 'inspect','traceback'], 
                       dll_excludes=['w9xpopen.exe'],
                       compressed=None, 
                       bundle_files = 1,
                       optimize = 2                        
                       )

#Generate a single exe. 
setup(    
    options = {'py2exe': opts},
    console = [{'script': "punbup.py",'dest_base': 'unbup'}],        
    zipfile = None,
)
