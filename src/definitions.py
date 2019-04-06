# definitions.py
'''
Contains project wide(global) variables
'''
from pathlib import Path
import os


def init():
    '''
    Creates project wide global variables to be reached within other files
    '''
    # DIR_SRC points to folder of source codes which is *PROJECT_DIRECTORY*/src
    # and can be reached from definitions.DIR_SRC after
    # running definitions.init() just once
    global DIR_SRC
    DIR_SRC = Path(__file__).parent

    # DIR_DATA points to where input data files are located
    global DIR_DATA
    DIR_DATA = Path('data')
    # DIR_HAPP and DIR_SUIC are directory to input data of respective data sets
    global DIR_HAPP
    DIR_HAPP = DIR_DATA / 'happiness'
    global DIR_SUIC
    DIR_SUIC = DIR_DATA / 'suicide'

    global DIR_SCRIPT
    DIR_SCRIPT = Path('sh')

    global FILE_REQS
    FILE_REQS = DIR_SRC.resolve().parent / "requirements.txt"

    if Path.cwd() is not DIR_SRC:
        # Changes active directory to project directory
        os.chdir(DIR_SRC)
