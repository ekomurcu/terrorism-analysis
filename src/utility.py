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


def getConsent(message='', trial=1):
    passes = {'Y': True, 'N': False}
    reply_original = input(message + "\t[Y/N]: ")
    reply = reply_original.capitalize().strip()

    if reply in passes.keys():
        return passes[reply]
    elif trial < 3:
        print("Unrecognized reply:", reply_original)
        return getConsent(message, trial=trial+1)
    else:
        return False
