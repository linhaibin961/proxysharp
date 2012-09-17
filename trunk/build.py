from distutils.core import setup
import py2exe
 
setup(  
    version = "",
    description = "",
    name = r"output",
    options = {
        "py2exe": {
            "compressed": 1,
            "optimize": 2,
            "ascii": 0,
            "bundle_files": 1,
            "includes" : ["sip"]
        }
    },
    zipfile = None,
    # targets to build
    windows = [
        {
            "script": r"main.py",
            "icon_resources": [(1, r"appengine.ico")]
        }
    ],
)

import shutil
shutil.rmtree('build')