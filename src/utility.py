# utility.py
import subprocess as sp  # subprocess.run() requires Python 3.5 or higher.
import definitions


def installRequirements(verbose=True):
    response = sp.run(
                "sh " + str(definitions.DIR_SCRIPT/"installRequirements.sh"),
                shell=True)


def openNotebook(verbose=True):
    response = sp.run(
                "sh " + str(definitions.DIR_SCRIPT / "openJupyter.sh"),
                shell=True)
