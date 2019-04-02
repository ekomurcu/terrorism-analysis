# utility.py
import subprocess as sp  # subprocess.run() requires Python 3.5 or higher.
import definitions


def installRequirements(verbose=True):
    response = sp.run(
                "sh " + str(definitions.DIR_SCRIPT/"installRequirements.sh"),
                shell=True)
    return checkResponse(
            response,
            "requirements.txt installation",
            verbose=verbose)


def openNotebook(verbose=True):
    response = sp.run(
                "sh " + str(definitions.DIR_SCRIPT / "openJupyter.sh"),
                shell=True)
    return checkResponse(
            response,
            command_name='Jupyter',
            verbose=verbose)


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


def checkResponse(response, command_name='', verbose=False):
    '''
    Input:
        response is a subprocess.CompletedProcess type
        command_name is a string and used to call command by its name
    '''
    if response.returncode is 0:
        if verbose:
            print(command_name, "run correctly.")
        return True
    elif response.returncode is 1:
        print("ERROR CODE: 1")
        if verbose:
            print(command_name, "encountered an error with a generic code.")
            print("Read above messages if any in the terminal screen to",
                  "get more info.")
        return False
    elif response.returncode is 126:
        print("ERROR CODE: 126")
        if verbose:
            print("Command invoked. Probably a permission error.")
        return False
    elif response.returncode is 127:
        print("ERROR CODE: 127")
        if verbose:
            print(command_name, "is not installed on this system or could not",
                  "found in your PATH.")
        return False
    else:
        print("Unrecognized error.")
        if verbose:
            print("Something else happened.")
        return False
