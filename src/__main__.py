# __main__.py
# Entry point of the while

import definitions
import utility
import subprocess as sp
print("Hello world!")
definitions.init()
if not utility.openNotebook():
    msg = "Do you want to install required packages?"
    if utility.getConsent(msg):
        if utility.installRequirements():
            utility.openNotebook(verbose=False)
    else:
        sp.run("exit 0", shell=True)
