#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.4),
    on December 13, 2024, at 16:42
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.2.4'
expName = 'MASC'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1707, 1067]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Uni\\Master\\Internship\\PsychoPyStuff\\MASC\\Builder\\MASC_fr\\MASC_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=True,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ptb'
        )
    if deviceManager.getDevice('key_resp_2') is None:
        # initialise key_resp_2
        key_resp_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_2',
        )
    if deviceManager.getDevice('key_resp_3') is None:
        # initialise key_resp_3
        key_resp_3 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_3',
        )
    if deviceManager.getDevice('key_resp_5') is None:
        # initialise key_resp_5
        key_resp_5 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_5',
        )
    if deviceManager.getDevice('key_resp_4') is None:
        # initialise key_resp_4
        key_resp_4 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_4',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='PsychToolbox',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='PsychToolbox'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "Ethics" ---
    text_10 = visual.TextStim(win=win, name='text_10',
        text="La participation à cette étude est entièrement volontaire, et un consentement éclairé est obtenu avant le début de celle-ci. Les participants sont assurés de l'anonymat et de la confidentialité, toutes les données étant stockées de manière sécurisée et utilisées uniquement à des fins de recherche. L'étude présente un risque minimal pour les participants, qui peuvent se retirer à tout moment sans conséquence. L'approbation éthique de cette étude a été obtenue auprès de Centre Hospitalaire Universitaire Vaudoise.",
        font='Arial',
        pos=(0, 0.2), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    EthicsSlider = visual.Slider(win=win, name='EthicsSlider',
        startValue=None, size=(1.0, 0.1), pos=(0, -0.08), units=win.units,
        labels=["Oui", "Non"], ticks=(1, 2), granularity=1.0,
        style='rating', styleTweaks=('triangleMarker',), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=-1, readOnly=False)
    InstructionEthicsSlider = visual.TextStim(win=win, name='InstructionEthicsSlider',
        text='Utilisez les touches fléchées pour naviguer et appuyez sur la touche Entrée pour valider votre sélection.',
        font='Arial',
        pos=(0, -0.40), draggable=False, height=0.025, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "AgeRange" ---
    AgeQuestion = visual.TextStim(win=win, name='AgeQuestion',
        text='À quelle tranche d’âge vous identifiez-vous ?',
        font='Arial',
        pos=(0, 0.25), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    Age_slider = visual.Slider(win=win, name='Age_slider',
        startValue=1, size=(1.0, 0.1), pos=(0, 0), units=win.units,
        labels=["18-29","30-39","40-49", "50-59", "60-69", "70-79", "80+"], ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
        style='rating', styleTweaks=('triangleMarker',), opacity=None,
        labelColor='White', markerColor='Red', lineColor='Gray', colorSpace='rgb',
        font='Open Sans', labelHeight=0.03,
        flip=False, ori=0.0, depth=-2, readOnly=False)
    InstructionAgeSlider = visual.TextStim(win=win, name='InstructionAgeSlider',
        text='Utilisez les touches fléchées pour naviguer et appuyez sur la touche Entrée pour valider votre sélection.',
        font='Arial',
        pos=(0, -0.40), draggable=False, height=0.025, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "Gender" ---
    GenderQuestion = visual.TextStim(win=win, name='GenderQuestion',
        text='À quel sexe vous identifiez-vous ?',
        font='Arial',
        pos=(0, 0.25), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    Gender_slider = visual.Slider(win=win, name='Gender_slider',
        startValue=1, size=(1.0, 0.1), pos=(0, 0), units=win.units,
        labels=["Femme","Homme","Autre", "Je préfère ne pas le dire"], ticks=(1, 2, 3, 4), granularity=1.0,
        style='rating', styleTweaks=('triangleMarker',), opacity=None,
        labelColor='White', markerColor='Red', lineColor='Gray', colorSpace='rgb',
        font='Open Sans', labelHeight=0.03,
        flip=False, ori=0.0, depth=-2, readOnly=False)
    InstructionGenderSlider = visual.TextStim(win=win, name='InstructionGenderSlider',
        text='Utilisez les touches fléchées pour naviguer et appuyez sur la touche Entrée pour valider votre sélection.',
        font='Arial',
        pos=(0, -0.40), draggable=False, height=0.025, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "CountryOfResidence" ---
    text_7 = visual.TextStim(win=win, name='text_7',
        text='Quel est votre pays de résidence ?',
        font='Arial',
        pos=(0, 0.25), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    textbox = visual.TextBox2(
         win, text='Enter text', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='textbox',
         depth=-1, autoLog=True,
    )
    
    # --- Initialize components for Routine "Instruction" ---
    WelcomeParticipant = visual.TextStim(win=win, name='WelcomeParticipant',
        text='Vous allez visionner un film d‘une durée de 15 minutes. Regardez attentivement ce film et essayez de comprendre ce que chaque personnage pense ou ressent.\n\n Appuyez sur la touche espace pour continuer.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_2 = keyboard.Keyboard(deviceName='key_resp_2')
    
    # --- Initialize components for Routine "Characters" ---
    text_2 = visual.TextStim(win=win, name='text_2',
        text='',
        font='Arial',
        pos=(0, 0.35), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    text_3 = visual.TextStim(win=win, name='text_3',
        text='Appuyez sur la touche espace pour continuer.',
        font='Arial',
        pos=(0, -0.4), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    Character = visual.ImageStim(
        win=win,
        name='Character', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.629, 0.418),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    key_resp_3 = keyboard.Keyboard(deviceName='key_resp_3')
    
    # --- Initialize components for Routine "Instruction2" ---
    text_5 = visual.TextStim(win=win, name='text_5',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_5 = keyboard.Keyboard(deviceName='key_resp_5')
    text_6 = visual.TextStim(win=win, name='text_6',
        text='',
        font='Arial',
        pos=(0, -0.4), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "PlayVideo" ---
    Clip = visual.MovieStim(
        win, name='Clip',
        filename=None, movieLib='ffpyplayer',
        loop=False, volume=1.0, noAudio=False,
        pos=(0, 0), size=(0.64, 0.48), units=win.units,
        ori=0.0, anchor='center',opacity=None, contrast=1.0,
        depth=0
    )
    key_resp_4 = keyboard.Keyboard(deviceName='key_resp_4')
    
    # --- Initialize components for Routine "AskQuestion" ---
    Questions = visual.TextStim(win=win, name='Questions',
        text='',
        font='Arial',
        pos=(0, 0.35), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    Answer_A = visual.TextStim(win=win, name='Answer_A',
        text='',
        font='Arial',
        pos=(-0.5, -0.1), draggable=False, height=0.04, wrapWidth=0.3, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    Answer_B = visual.TextStim(win=win, name='Answer_B',
        text='',
        font='Arial',
        pos=(-0.16, -0.1), draggable=False, height=0.04, wrapWidth=0.3, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    Answer_C = visual.TextStim(win=win, name='Answer_C',
        text='',
        font='Arial',
        pos=(0.16, -0.1), draggable=False, height=0.04, wrapWidth=0.3, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    Answer_D = visual.TextStim(win=win, name='Answer_D',
        text='',
        font='Arial',
        pos=(0.5, -0.1), draggable=False, height=0.04, wrapWidth=0.2, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    slider_2 = visual.Slider(win=win, name='slider_2',
        startValue=1, size=(1.0, 0.1), pos=(0, 0.1), units=win.units,
        labels=None, ticks=(1, 2, 3, 4), granularity=1.0,
        style='rating', styleTweaks=('triangleMarker',), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='Gray', colorSpace='rgb',
        font='Open Sans', labelHeight=0.01,
        flip=False, ori=0.0, depth=-5, readOnly=False)
    InstructionSlider = visual.TextStim(win=win, name='InstructionSlider',
        text='Utilisez les touches fléchées pour naviguer et appuyez sur la touche Entrée pour valider votre sélection.',
        font='Arial',
        pos=(0, -0.40), draggable=False, height=0.025, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-7.0);
    
    # --- Initialize components for Routine "ConfidenceSlider" ---
    confidence_slider = visual.Slider(win=win, name='confidence_slider',
        startValue=5, size=(1.0, 0.1), pos=(0, 0), units=win.units,
        labels=["Pas confiant", "Ni confiant, ni pas confiant", "Très confiant"], ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9), granularity=1.0,
        style='rating', styleTweaks=('triangleMarker',), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.019,
        flip=False, ori=0.0, depth=-1, readOnly=False)
    text_4 = visual.TextStim(win=win, name='text_4',
        text='Utilisez les touches fléchées pour naviguer et appuyez sur la touche Entrée pour valider votre sélection.',
        font='Arial',
        pos=(0, -0.3), draggable=False, height=0.025, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    text_8 = visual.TextStim(win=win, name='text_8',
        text='A quel point êtes vous sur de votre réponse?',
        font='Arial',
        pos=(0, 0.35), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "ThankYou" ---
    Thanks = visual.TextStim(win=win, name='Thanks',
        text="Vous avez terminé l'experience. Merci de votre participation.",
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "Ethics" ---
    # create an object to store info about Routine Ethics
    Ethics = data.Routine(
        name='Ethics',
        components=[text_10, EthicsSlider, InstructionEthicsSlider],
    )
    Ethics.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    EthicsSlider.reset()
    # Run 'Begin Routine' code from EthicsSliderController
    # Initialize variables
    slider_position = 0  # Starting position of the slider
    EthicsSlider.markerPos = slider_position  # Set initial slider position
    
    # store start times for Ethics
    Ethics.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Ethics.tStart = globalClock.getTime(format='float')
    Ethics.status = STARTED
    thisExp.addData('Ethics.started', Ethics.tStart)
    Ethics.maxDuration = None
    # keep track of which components have finished
    EthicsComponents = Ethics.components
    for thisComponent in Ethics.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Ethics" ---
    Ethics.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_10* updates
        
        # if text_10 is starting this frame...
        if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_10.frameNStart = frameN  # exact frame index
            text_10.tStart = t  # local t and not account for scr refresh
            text_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_10.started')
            # update status
            text_10.status = STARTED
            text_10.setAutoDraw(True)
        
        # if text_10 is active this frame...
        if text_10.status == STARTED:
            # update params
            pass
        
        # *EthicsSlider* updates
        
        # if EthicsSlider is starting this frame...
        if EthicsSlider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            EthicsSlider.frameNStart = frameN  # exact frame index
            EthicsSlider.tStart = t  # local t and not account for scr refresh
            EthicsSlider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(EthicsSlider, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'EthicsSlider.started')
            # update status
            EthicsSlider.status = STARTED
            EthicsSlider.setAutoDraw(True)
        
        # if EthicsSlider is active this frame...
        if EthicsSlider.status == STARTED:
            # update params
            pass
        
        # Check EthicsSlider for response to end Routine
        if EthicsSlider.getRating() is not None and EthicsSlider.status == STARTED:
            continueRoutine = False
        # Run 'Each Frame' code from EthicsSliderController
        # Capture key presses
        keys = event.getKeys()
        
        for key in keys:
            if key == 'left':  # Move marker left
                if slider_position > 1:
                    slider_position -= 1
                    EthicsSlider.markerPos = slider_position
            elif key == 'right':  # Move marker right
                if slider_position < len(EthicsSlider.labels):
                    slider_position += 1
                    EthicsSlider.markerPos = slider_position
            elif key == 'return':  # Confirm choice
                if slider_position == 2:  # Check if "No" (second tick) is selected
                    thisExp.abort()  # End the experiment
                    core.quit()
                else:
                    continueRoutine = False  # End the routine
        
        
        # *InstructionEthicsSlider* updates
        
        # if InstructionEthicsSlider is starting this frame...
        if InstructionEthicsSlider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstructionEthicsSlider.frameNStart = frameN  # exact frame index
            InstructionEthicsSlider.tStart = t  # local t and not account for scr refresh
            InstructionEthicsSlider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstructionEthicsSlider, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'InstructionEthicsSlider.started')
            # update status
            InstructionEthicsSlider.status = STARTED
            InstructionEthicsSlider.setAutoDraw(True)
        
        # if InstructionEthicsSlider is active this frame...
        if InstructionEthicsSlider.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Ethics.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Ethics.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Ethics" ---
    for thisComponent in Ethics.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Ethics
    Ethics.tStop = globalClock.getTime(format='float')
    Ethics.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Ethics.stopped', Ethics.tStop)
    thisExp.addData('EthicsSlider.response', EthicsSlider.getRating())
    thisExp.addData('EthicsSlider.rt', EthicsSlider.getRT())
    thisExp.addData('EthicsSlider.history', EthicsSlider.getHistory())
    thisExp.nextEntry()
    # the Routine "Ethics" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "AgeRange" ---
    # create an object to store info about Routine AgeRange
    AgeRange = data.Routine(
        name='AgeRange',
        components=[AgeQuestion, Age_slider, InstructionAgeSlider],
    )
    AgeRange.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    Age_slider.reset()
    # store start times for AgeRange
    AgeRange.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    AgeRange.tStart = globalClock.getTime(format='float')
    AgeRange.status = STARTED
    thisExp.addData('AgeRange.started', AgeRange.tStart)
    AgeRange.maxDuration = None
    # keep track of which components have finished
    AgeRangeComponents = AgeRange.components
    for thisComponent in AgeRange.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "AgeRange" ---
    AgeRange.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from AgeRange_slider_controller
        # Detect arrow keys and move the slider marker
        keys = event.getKeys(['left', 'right', 'return'])
        
        if 'left' in keys and Age_slider.markerPos > Age_slider.ticks[0]:
            Age_slider.markerPos -= 1  # Move left
        elif 'right' in keys and Age_slider.markerPos < Age_slider.ticks[-1]:
            Age_slider.markerPos += 1  # Move right
        elif 'return' in keys:
            # Confirm the selection and end the routine
            continueRoutine = False
        
        
        # *AgeQuestion* updates
        
        # if AgeQuestion is starting this frame...
        if AgeQuestion.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            AgeQuestion.frameNStart = frameN  # exact frame index
            AgeQuestion.tStart = t  # local t and not account for scr refresh
            AgeQuestion.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AgeQuestion, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'AgeQuestion.started')
            # update status
            AgeQuestion.status = STARTED
            AgeQuestion.setAutoDraw(True)
        
        # if AgeQuestion is active this frame...
        if AgeQuestion.status == STARTED:
            # update params
            pass
        
        # *Age_slider* updates
        
        # if Age_slider is starting this frame...
        if Age_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Age_slider.frameNStart = frameN  # exact frame index
            Age_slider.tStart = t  # local t and not account for scr refresh
            Age_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Age_slider, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Age_slider.started')
            # update status
            Age_slider.status = STARTED
            Age_slider.setAutoDraw(True)
        
        # if Age_slider is active this frame...
        if Age_slider.status == STARTED:
            # update params
            pass
        
        # *InstructionAgeSlider* updates
        
        # if InstructionAgeSlider is starting this frame...
        if InstructionAgeSlider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstructionAgeSlider.frameNStart = frameN  # exact frame index
            InstructionAgeSlider.tStart = t  # local t and not account for scr refresh
            InstructionAgeSlider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstructionAgeSlider, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'InstructionAgeSlider.started')
            # update status
            InstructionAgeSlider.status = STARTED
            InstructionAgeSlider.setAutoDraw(True)
        
        # if InstructionAgeSlider is active this frame...
        if InstructionAgeSlider.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            AgeRange.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AgeRange.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "AgeRange" ---
    for thisComponent in AgeRange.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for AgeRange
    AgeRange.tStop = globalClock.getTime(format='float')
    AgeRange.tStopRefresh = tThisFlipGlobal
    thisExp.addData('AgeRange.stopped', AgeRange.tStop)
    thisExp.addData('Age_slider.response', Age_slider.getRating())
    thisExp.addData('Age_slider.history', Age_slider.getHistory())
    # Run 'End Routine' code from CollectAgeData
    thisExp.addData('Age_slider_position', Age_slider.getRating())
    thisExp.addData('Age_slider.response', Age_slider.getRT())
    thisExp.addData('AgeRange.started', Age_slider.tStart)
    thisExp.addData('AgeRange.stopped', Age_slider.tStop)
    
    thisExp.nextEntry()
    # the Routine "AgeRange" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Gender" ---
    # create an object to store info about Routine Gender
    Gender = data.Routine(
        name='Gender',
        components=[GenderQuestion, Gender_slider, InstructionGenderSlider],
    )
    Gender.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    Gender_slider.reset()
    # store start times for Gender
    Gender.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Gender.tStart = globalClock.getTime(format='float')
    Gender.status = STARTED
    thisExp.addData('Gender.started', Gender.tStart)
    Gender.maxDuration = None
    # keep track of which components have finished
    GenderComponents = Gender.components
    for thisComponent in Gender.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Gender" ---
    Gender.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from Gender_slider_controller
        # Detect arrow keys and move the slider marker
        keys = event.getKeys(['left', 'right', 'return'])
        
        if 'left' in keys and Gender_slider.markerPos > Gender_slider.ticks[0]:
            Gender_slider.markerPos -= 1  # Move left
        elif 'right' in keys and Gender_slider.markerPos < Gender_slider.ticks[-1]:
            Gender_slider.markerPos += 1  # Move right
        elif 'return' in keys:
            # Confirm the selection and end the routine
            continueRoutine = False
        
        
        # *GenderQuestion* updates
        
        # if GenderQuestion is starting this frame...
        if GenderQuestion.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            GenderQuestion.frameNStart = frameN  # exact frame index
            GenderQuestion.tStart = t  # local t and not account for scr refresh
            GenderQuestion.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(GenderQuestion, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'GenderQuestion.started')
            # update status
            GenderQuestion.status = STARTED
            GenderQuestion.setAutoDraw(True)
        
        # if GenderQuestion is active this frame...
        if GenderQuestion.status == STARTED:
            # update params
            pass
        
        # *Gender_slider* updates
        
        # if Gender_slider is starting this frame...
        if Gender_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Gender_slider.frameNStart = frameN  # exact frame index
            Gender_slider.tStart = t  # local t and not account for scr refresh
            Gender_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Gender_slider, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Gender_slider.started')
            # update status
            Gender_slider.status = STARTED
            Gender_slider.setAutoDraw(True)
        
        # if Gender_slider is active this frame...
        if Gender_slider.status == STARTED:
            # update params
            pass
        
        # *InstructionGenderSlider* updates
        
        # if InstructionGenderSlider is starting this frame...
        if InstructionGenderSlider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstructionGenderSlider.frameNStart = frameN  # exact frame index
            InstructionGenderSlider.tStart = t  # local t and not account for scr refresh
            InstructionGenderSlider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstructionGenderSlider, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'InstructionGenderSlider.started')
            # update status
            InstructionGenderSlider.status = STARTED
            InstructionGenderSlider.setAutoDraw(True)
        
        # if InstructionGenderSlider is active this frame...
        if InstructionGenderSlider.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Gender.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Gender.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Gender" ---
    for thisComponent in Gender.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Gender
    Gender.tStop = globalClock.getTime(format='float')
    Gender.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Gender.stopped', Gender.tStop)
    # Run 'End Routine' code from Gender_slider_controller
    # Get the slider's selected position
    Gender_slider_position = Gender_slider.markerPos
    
    # Log the slider position in the data file
    thisExp.addData('Gender_slider_position', Gender_slider_position)
    
    thisExp.addData('Gender_slider.response', Gender_slider.getRating())
    thisExp.addData('Gender_slider.rt', Gender_slider.getRT())
    # Run 'End Routine' code from CollectGenderData
    thisExp.addData('Gender_slider_position', Gender_slider.getRating())
    thisExp.addData('Gender_slider.response', Gender_slider.getRT())
    thisExp.addData('Gender.started', Gender_slider.tStart)
    thisExp.addData('Gender.stopped', Gender_slider.tStop)
    
    thisExp.nextEntry()
    # the Routine "Gender" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "CountryOfResidence" ---
    # create an object to store info about Routine CountryOfResidence
    CountryOfResidence = data.Routine(
        name='CountryOfResidence',
        components=[text_7, textbox],
    )
    CountryOfResidence.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    textbox.reset()
    # Run 'Begin Routine' code from Type_Controller
    #BeginRoutine
    
    text_entered = ''  # Stores the user input
    typing_enabled = False  # Whether typing is allowed
    instruction_text = "Appuyez sur 'T' pour commencer a taper et sur 'Entree ' pour soumettre."  # Instruction message
    textbox.setText(instruction_text)  # Set the initial instruction text
    
    # store start times for CountryOfResidence
    CountryOfResidence.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    CountryOfResidence.tStart = globalClock.getTime(format='float')
    CountryOfResidence.status = STARTED
    thisExp.addData('CountryOfResidence.started', CountryOfResidence.tStart)
    CountryOfResidence.maxDuration = None
    # keep track of which components have finished
    CountryOfResidenceComponents = CountryOfResidence.components
    for thisComponent in CountryOfResidence.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "CountryOfResidence" ---
    CountryOfResidence.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_7* updates
        
        # if text_7 is starting this frame...
        if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_7.frameNStart = frameN  # exact frame index
            text_7.tStart = t  # local t and not account for scr refresh
            text_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_7.started')
            # update status
            text_7.status = STARTED
            text_7.setAutoDraw(True)
        
        # if text_7 is active this frame...
        if text_7.status == STARTED:
            # update params
            pass
        
        # *textbox* updates
        
        # if textbox is starting this frame...
        if textbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textbox.frameNStart = frameN  # exact frame index
            textbox.tStart = t  # local t and not account for scr refresh
            textbox.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textbox, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textbox.started')
            # update status
            textbox.status = STARTED
            textbox.setAutoDraw(True)
        
        # if textbox is active this frame...
        if textbox.status == STARTED:
            # update params
            pass
        # Run 'Each Frame' code from Type_Controller
        #EachFrame
        
        # Get currently pressed keys
        keys = event.getKeys()
        
        # Debugging: Print the pressed keys
        if keys:
            print(f"Keys pressed: {keys}")
        
        # Check if typing is enabled
        if typing_enabled:
            for key in keys:
                if key == 'return':  # If Enter is pressed
                    print(f"Input submitted: '{text_entered}'")  # Debug: Log the submitted input
                    thisExp.addData('Country', text_entered)  # Save the entered text to the experiment data
                    continueRoutine = False  # End the routine
                    typing_enabled = False  # Disable typing
                elif key == 'backspace':  # If Backspace is pressed
                    if len(text_entered) > 0:  # Only delete if there is text
                        text_entered = text_entered[:-1]  # Remove the last character
                        print(f"Backspace pressed. Updated text: '{text_entered}'")  # Debug log
                elif key == 'period':  # Handle '.' character
                    text_entered += '.'  # Append a dot
                    print(f"Period pressed. Updated text: '{text_entered}'")  # Debug log
                elif len(key) == 1:  # If it's a single character (e.g., numbers or letters)
                    text_entered += key  # Add the key to the text
                    print(f"Key '{key}' added. Updated text: '{text_entered}'")  # Debug log
        
            # Update the textbox with the latest text
            textbox.setText(text_entered)
        
        elif 't' in keys:  # Enable typing when 'T' is pressed
            typing_enabled = True  # Enable typing
            text_entered = ''  # Clear previous input
            textbox.setText('')  # Clear the textbox
            print("Typing enabled. Textbox cleared.")  # Debug log
        
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            CountryOfResidence.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in CountryOfResidence.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "CountryOfResidence" ---
    for thisComponent in CountryOfResidence.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for CountryOfResidence
    CountryOfResidence.tStop = globalClock.getTime(format='float')
    CountryOfResidence.tStopRefresh = tThisFlipGlobal
    thisExp.addData('CountryOfResidence.stopped', CountryOfResidence.tStop)
    # Run 'End Routine' code from Type_Controller
    # EndRoutine
    
    # Save the entered text
    thisExp.addData('Country', text_entered)
    
    
    
    thisExp.nextEntry()
    # the Routine "CountryOfResidence" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instruction" ---
    # create an object to store info about Routine Instruction
    Instruction = data.Routine(
        name='Instruction',
        components=[WelcomeParticipant, key_resp_2],
    )
    Instruction.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_2
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # store start times for Instruction
    Instruction.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Instruction.tStart = globalClock.getTime(format='float')
    Instruction.status = STARTED
    thisExp.addData('Instruction.started', Instruction.tStart)
    Instruction.maxDuration = None
    # keep track of which components have finished
    InstructionComponents = Instruction.components
    for thisComponent in Instruction.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Instruction" ---
    Instruction.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *WelcomeParticipant* updates
        
        # if WelcomeParticipant is starting this frame...
        if WelcomeParticipant.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            WelcomeParticipant.frameNStart = frameN  # exact frame index
            WelcomeParticipant.tStart = t  # local t and not account for scr refresh
            WelcomeParticipant.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(WelcomeParticipant, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'WelcomeParticipant.started')
            # update status
            WelcomeParticipant.status = STARTED
            WelcomeParticipant.setAutoDraw(True)
        
        # if WelcomeParticipant is active this frame...
        if WelcomeParticipant.status == STARTED:
            # update params
            pass
        
        # *key_resp_2* updates
        waitOnFlip = False
        
        # if key_resp_2 is starting this frame...
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_2.started')
            # update status
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                key_resp_2.duration = _key_resp_2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Instruction.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instruction.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instruction" ---
    for thisComponent in Instruction.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Instruction
    Instruction.tStop = globalClock.getTime(format='float')
    Instruction.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Instruction.stopped', Instruction.tStop)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    thisExp.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        thisExp.addData('key_resp_2.rt', key_resp_2.rt)
        thisExp.addData('key_resp_2.duration', key_resp_2.duration)
    thisExp.nextEntry()
    # the Routine "Instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    CharactersLoop = data.TrialHandler2(
        name='CharactersLoop',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('MASC_Characters.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(CharactersLoop)  # add the loop to the experiment
    thisCharactersLoop = CharactersLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisCharactersLoop.rgb)
    if thisCharactersLoop != None:
        for paramName in thisCharactersLoop:
            globals()[paramName] = thisCharactersLoop[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisCharactersLoop in CharactersLoop:
        currentLoop = CharactersLoop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisCharactersLoop.rgb)
        if thisCharactersLoop != None:
            for paramName in thisCharactersLoop:
                globals()[paramName] = thisCharactersLoop[paramName]
        
        # --- Prepare to start Routine "Characters" ---
        # create an object to store info about Routine Characters
        Characters = data.Routine(
            name='Characters',
            components=[text_2, text_3, Character, key_resp_3],
        )
        Characters.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        text_2.setText('Nous vous proposons maintenant de rencontrer chacun des personnages. \n')
        Character.setImage(FileName)
        # create starting attributes for key_resp_3
        key_resp_3.keys = []
        key_resp_3.rt = []
        _key_resp_3_allKeys = []
        # store start times for Characters
        Characters.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Characters.tStart = globalClock.getTime(format='float')
        Characters.status = STARTED
        thisExp.addData('Characters.started', Characters.tStart)
        Characters.maxDuration = None
        # keep track of which components have finished
        CharactersComponents = Characters.components
        for thisComponent in Characters.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Characters" ---
        # if trial has changed, end Routine now
        if isinstance(CharactersLoop, data.TrialHandler2) and thisCharactersLoop.thisN != CharactersLoop.thisTrial.thisN:
            continueRoutine = False
        Characters.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_2* updates
            
            # if text_2 is starting this frame...
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_2.started')
                # update status
                text_2.status = STARTED
                text_2.setAutoDraw(True)
            
            # if text_2 is active this frame...
            if text_2.status == STARTED:
                # update params
                pass
            
            # *text_3* updates
            
            # if text_3 is starting this frame...
            if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_3.frameNStart = frameN  # exact frame index
                text_3.tStart = t  # local t and not account for scr refresh
                text_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_3.started')
                # update status
                text_3.status = STARTED
                text_3.setAutoDraw(True)
            
            # if text_3 is active this frame...
            if text_3.status == STARTED:
                # update params
                pass
            
            # *Character* updates
            
            # if Character is starting this frame...
            if Character.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Character.frameNStart = frameN  # exact frame index
                Character.tStart = t  # local t and not account for scr refresh
                Character.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Character, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Character.started')
                # update status
                Character.status = STARTED
                Character.setAutoDraw(True)
            
            # if Character is active this frame...
            if Character.status == STARTED:
                # update params
                pass
            
            # *key_resp_3* updates
            waitOnFlip = False
            
            # if key_resp_3 is starting this frame...
            if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_3.frameNStart = frameN  # exact frame index
                key_resp_3.tStart = t  # local t and not account for scr refresh
                key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_3.started')
                # update status
                key_resp_3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_3.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_3.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_3_allKeys.extend(theseKeys)
                if len(_key_resp_3_allKeys):
                    key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                    key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                    key_resp_3.duration = _key_resp_3_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Characters.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Characters.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Characters" ---
        for thisComponent in Characters.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Characters
        Characters.tStop = globalClock.getTime(format='float')
        Characters.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Characters.stopped', Characters.tStop)
        # check responses
        if key_resp_3.keys in ['', [], None]:  # No response was made
            key_resp_3.keys = None
        CharactersLoop.addData('key_resp_3.keys',key_resp_3.keys)
        if key_resp_3.keys != None:  # we had a response
            CharactersLoop.addData('key_resp_3.rt', key_resp_3.rt)
            CharactersLoop.addData('key_resp_3.duration', key_resp_3.duration)
        # the Routine "Characters" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'CharactersLoop'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # set up handler to look after randomisation of conditions etc
    InstructionsLoop = data.TrialHandler2(
        name='InstructionsLoop',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('MASC_Instructions.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(InstructionsLoop)  # add the loop to the experiment
    thisInstructionsLoop = InstructionsLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisInstructionsLoop.rgb)
    if thisInstructionsLoop != None:
        for paramName in thisInstructionsLoop:
            globals()[paramName] = thisInstructionsLoop[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisInstructionsLoop in InstructionsLoop:
        currentLoop = InstructionsLoop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisInstructionsLoop.rgb)
        if thisInstructionsLoop != None:
            for paramName in thisInstructionsLoop:
                globals()[paramName] = thisInstructionsLoop[paramName]
        
        # --- Prepare to start Routine "Instruction2" ---
        # create an object to store info about Routine Instruction2
        Instruction2 = data.Routine(
            name='Instruction2',
            components=[text_5, key_resp_5, text_6],
        )
        Instruction2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        text_5.setText(Text
        )
        # create starting attributes for key_resp_5
        key_resp_5.keys = []
        key_resp_5.rt = []
        _key_resp_5_allKeys = []
        text_6.setText('Appuyez sur la touche espace pour continuer.')
        # store start times for Instruction2
        Instruction2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Instruction2.tStart = globalClock.getTime(format='float')
        Instruction2.status = STARTED
        thisExp.addData('Instruction2.started', Instruction2.tStart)
        Instruction2.maxDuration = None
        # keep track of which components have finished
        Instruction2Components = Instruction2.components
        for thisComponent in Instruction2.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Instruction2" ---
        # if trial has changed, end Routine now
        if isinstance(InstructionsLoop, data.TrialHandler2) and thisInstructionsLoop.thisN != InstructionsLoop.thisTrial.thisN:
            continueRoutine = False
        Instruction2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_5* updates
            
            # if text_5 is starting this frame...
            if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_5.frameNStart = frameN  # exact frame index
                text_5.tStart = t  # local t and not account for scr refresh
                text_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_5.started')
                # update status
                text_5.status = STARTED
                text_5.setAutoDraw(True)
            
            # if text_5 is active this frame...
            if text_5.status == STARTED:
                # update params
                pass
            
            # *key_resp_5* updates
            waitOnFlip = False
            
            # if key_resp_5 is starting this frame...
            if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_5.frameNStart = frameN  # exact frame index
                key_resp_5.tStart = t  # local t and not account for scr refresh
                key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_5.started')
                # update status
                key_resp_5.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_5.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_5.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_5_allKeys.extend(theseKeys)
                if len(_key_resp_5_allKeys):
                    key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                    key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                    key_resp_5.duration = _key_resp_5_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *text_6* updates
            
            # if text_6 is starting this frame...
            if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_6.frameNStart = frameN  # exact frame index
                text_6.tStart = t  # local t and not account for scr refresh
                text_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_6.started')
                # update status
                text_6.status = STARTED
                text_6.setAutoDraw(True)
            
            # if text_6 is active this frame...
            if text_6.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Instruction2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Instruction2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Instruction2" ---
        for thisComponent in Instruction2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Instruction2
        Instruction2.tStop = globalClock.getTime(format='float')
        Instruction2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Instruction2.stopped', Instruction2.tStop)
        # check responses
        if key_resp_5.keys in ['', [], None]:  # No response was made
            key_resp_5.keys = None
        InstructionsLoop.addData('key_resp_5.keys',key_resp_5.keys)
        if key_resp_5.keys != None:  # we had a response
            InstructionsLoop.addData('key_resp_5.rt', key_resp_5.rt)
            InstructionsLoop.addData('key_resp_5.duration', key_resp_5.duration)
        # the Routine "Instruction2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'InstructionsLoop'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # set up handler to look after randomisation of conditions etc
    VideoQuestionSliderLoop = data.TrialHandler2(
        name='VideoQuestionSliderLoop',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('MASC_Cleaned_SingleRowPerQuestion_Corrected (1).xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(VideoQuestionSliderLoop)  # add the loop to the experiment
    thisVideoQuestionSliderLoop = VideoQuestionSliderLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisVideoQuestionSliderLoop.rgb)
    if thisVideoQuestionSliderLoop != None:
        for paramName in thisVideoQuestionSliderLoop:
            globals()[paramName] = thisVideoQuestionSliderLoop[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisVideoQuestionSliderLoop in VideoQuestionSliderLoop:
        currentLoop = VideoQuestionSliderLoop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisVideoQuestionSliderLoop.rgb)
        if thisVideoQuestionSliderLoop != None:
            for paramName in thisVideoQuestionSliderLoop:
                globals()[paramName] = thisVideoQuestionSliderLoop[paramName]
        
        # --- Prepare to start Routine "PlayVideo" ---
        # create an object to store info about Routine PlayVideo
        PlayVideo = data.Routine(
            name='PlayVideo',
            components=[Clip, key_resp_4],
        )
        PlayVideo.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        Clip.setMovie(ClipName)
        # create starting attributes for key_resp_4
        key_resp_4.keys = []
        key_resp_4.rt = []
        _key_resp_4_allKeys = []
        # Run 'Begin Routine' code from CollectDataVideo
        # Record the start time of the clip
        t0 = globalClock.getTime()
        thisExp.addData('t0', t0)
        
        # Log the clip name
        thisExp.addData('ClipName', ClipName)  # Replace `currentClip` with the variable storing the clip name
        
        # store start times for PlayVideo
        PlayVideo.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        PlayVideo.tStart = globalClock.getTime(format='float')
        PlayVideo.status = STARTED
        thisExp.addData('PlayVideo.started', PlayVideo.tStart)
        PlayVideo.maxDuration = None
        # keep track of which components have finished
        PlayVideoComponents = PlayVideo.components
        for thisComponent in PlayVideo.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "PlayVideo" ---
        # if trial has changed, end Routine now
        if isinstance(VideoQuestionSliderLoop, data.TrialHandler2) and thisVideoQuestionSliderLoop.thisN != VideoQuestionSliderLoop.thisTrial.thisN:
            continueRoutine = False
        PlayVideo.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Clip* updates
            
            # if Clip is starting this frame...
            if Clip.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Clip.frameNStart = frameN  # exact frame index
                Clip.tStart = t  # local t and not account for scr refresh
                Clip.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Clip, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Clip.started')
                # update status
                Clip.status = STARTED
                Clip.setAutoDraw(True)
                Clip.play()
            
            # if Clip is stopping this frame...
            if Clip.status == STARTED:
                if bool(False) or Clip.isFinished:
                    # keep track of stop time/frame for later
                    Clip.tStop = t  # not accounting for scr refresh
                    Clip.tStopRefresh = tThisFlipGlobal  # on global time
                    Clip.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Clip.stopped')
                    # update status
                    Clip.status = FINISHED
                    Clip.setAutoDraw(False)
                    Clip.stop()
            if Clip.isFinished:  # force-end the Routine
                continueRoutine = False
            
            # *key_resp_4* updates
            waitOnFlip = False
            
            # if key_resp_4 is starting this frame...
            if key_resp_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_4.frameNStart = frameN  # exact frame index
                key_resp_4.tStart = t  # local t and not account for scr refresh
                key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_4.started')
                # update status
                key_resp_4.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_4.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_4.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_4_allKeys.extend(theseKeys)
                if len(_key_resp_4_allKeys):
                    key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                    key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                    key_resp_4.duration = _key_resp_4_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[Clip]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                PlayVideo.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PlayVideo.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "PlayVideo" ---
        for thisComponent in PlayVideo.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for PlayVideo
        PlayVideo.tStop = globalClock.getTime(format='float')
        PlayVideo.tStopRefresh = tThisFlipGlobal
        thisExp.addData('PlayVideo.stopped', PlayVideo.tStop)
        Clip.stop()  # ensure movie has stopped at end of Routine
        # check responses
        if key_resp_4.keys in ['', [], None]:  # No response was made
            key_resp_4.keys = None
        VideoQuestionSliderLoop.addData('key_resp_4.keys',key_resp_4.keys)
        if key_resp_4.keys != None:  # we had a response
            VideoQuestionSliderLoop.addData('key_resp_4.rt', key_resp_4.rt)
            VideoQuestionSliderLoop.addData('key_resp_4.duration', key_resp_4.duration)
        # Run 'End Routine' code from CollectDataVideo
        # Record the end time of the clip
        t1 = globalClock.getTime()
        thisExp.addData('t1', t1)
        
        # the Routine "PlayVideo" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "AskQuestion" ---
        # create an object to store info about Routine AskQuestion
        AskQuestion = data.Routine(
            name='AskQuestion',
            components=[Questions, Answer_A, Answer_B, Answer_C, Answer_D, slider_2, InstructionSlider],
        )
        AskQuestion.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        Questions.setText(Question)
        Answer_A.setText(Answer_1)
        Answer_B.setText(Answer_2)
        Answer_C.setText(Answer_3)
        Answer_D.setText(Answer_4)
        slider_2.reset()
        # Run 'Begin Routine' code from SliderStuff
        # Dynamically fetch the labels from the conditions file
        #slider_labels = [Answer_1, Answer_2, Answer_3, Answer_4]
        
        # Assign labels to the slider
        #slider_2.reset()
        #slider_2.labels = slider_labels
        
        # Flip the triangle horizontally
        #slider_2.marker.setOri(180)  # Flip the triangle
        
        # Clear any lingering keypresses from the previous routine
        event.clearEvents()
        
        # Run 'Begin Routine' code from QuestionDataCollectTime
        # Record the time when the question is displayed
        t2 = globalClock.getTime()
        thisExp.addData('t2', t2)
        
        # store start times for AskQuestion
        AskQuestion.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        AskQuestion.tStart = globalClock.getTime(format='float')
        AskQuestion.status = STARTED
        thisExp.addData('AskQuestion.started', AskQuestion.tStart)
        AskQuestion.maxDuration = None
        # keep track of which components have finished
        AskQuestionComponents = AskQuestion.components
        for thisComponent in AskQuestion.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "AskQuestion" ---
        # if trial has changed, end Routine now
        if isinstance(VideoQuestionSliderLoop, data.TrialHandler2) and thisVideoQuestionSliderLoop.thisN != VideoQuestionSliderLoop.thisTrial.thisN:
            continueRoutine = False
        AskQuestion.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Questions* updates
            
            # if Questions is starting this frame...
            if Questions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Questions.frameNStart = frameN  # exact frame index
                Questions.tStart = t  # local t and not account for scr refresh
                Questions.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Questions, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Questions.started')
                # update status
                Questions.status = STARTED
                Questions.setAutoDraw(True)
            
            # if Questions is active this frame...
            if Questions.status == STARTED:
                # update params
                pass
            
            # *Answer_A* updates
            
            # if Answer_A is starting this frame...
            if Answer_A.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Answer_A.frameNStart = frameN  # exact frame index
                Answer_A.tStart = t  # local t and not account for scr refresh
                Answer_A.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Answer_A, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Answer_A.started')
                # update status
                Answer_A.status = STARTED
                Answer_A.setAutoDraw(True)
            
            # if Answer_A is active this frame...
            if Answer_A.status == STARTED:
                # update params
                pass
            
            # *Answer_B* updates
            
            # if Answer_B is starting this frame...
            if Answer_B.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Answer_B.frameNStart = frameN  # exact frame index
                Answer_B.tStart = t  # local t and not account for scr refresh
                Answer_B.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Answer_B, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Answer_B.started')
                # update status
                Answer_B.status = STARTED
                Answer_B.setAutoDraw(True)
            
            # if Answer_B is active this frame...
            if Answer_B.status == STARTED:
                # update params
                pass
            
            # *Answer_C* updates
            
            # if Answer_C is starting this frame...
            if Answer_C.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Answer_C.frameNStart = frameN  # exact frame index
                Answer_C.tStart = t  # local t and not account for scr refresh
                Answer_C.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Answer_C, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Answer_C.started')
                # update status
                Answer_C.status = STARTED
                Answer_C.setAutoDraw(True)
            
            # if Answer_C is active this frame...
            if Answer_C.status == STARTED:
                # update params
                pass
            
            # *Answer_D* updates
            
            # if Answer_D is starting this frame...
            if Answer_D.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Answer_D.frameNStart = frameN  # exact frame index
                Answer_D.tStart = t  # local t and not account for scr refresh
                Answer_D.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Answer_D, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Answer_D.started')
                # update status
                Answer_D.status = STARTED
                Answer_D.setAutoDraw(True)
            
            # if Answer_D is active this frame...
            if Answer_D.status == STARTED:
                # update params
                pass
            
            # *slider_2* updates
            
            # if slider_2 is starting this frame...
            if slider_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                slider_2.frameNStart = frameN  # exact frame index
                slider_2.tStart = t  # local t and not account for scr refresh
                slider_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slider_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider_2.started')
                # update status
                slider_2.status = STARTED
                slider_2.setAutoDraw(True)
            
            # if slider_2 is active this frame...
            if slider_2.status == STARTED:
                # update params
                pass
            
            # Check slider_2 for response to end Routine
            if slider_2.getRating() is not None and slider_2.status == STARTED:
                continueRoutine = False
            # Run 'Each Frame' code from SliderStuff
            #EachFrame
            # Detect arrow keys and move the slider marker
            keys = event.getKeys(['left', 'right', 'return'])
            
            if 'left' in keys and slider_2.markerPos > slider_2.ticks[0]:
                slider_2.markerPos -= 1  # Move left
            elif 'right' in keys and slider_2.markerPos < slider_2.ticks[-1]:
                slider_2.markerPos += 1  # Move right
            elif 'return' in keys:
                # Confirm the selection and end the routine
                continueRoutine = False
            
            
            # *InstructionSlider* updates
            
            # if InstructionSlider is starting this frame...
            if InstructionSlider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                InstructionSlider.frameNStart = frameN  # exact frame index
                InstructionSlider.tStart = t  # local t and not account for scr refresh
                InstructionSlider.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(InstructionSlider, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'InstructionSlider.started')
                # update status
                InstructionSlider.status = STARTED
                InstructionSlider.setAutoDraw(True)
            
            # if InstructionSlider is active this frame...
            if InstructionSlider.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                AskQuestion.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in AskQuestion.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "AskQuestion" ---
        for thisComponent in AskQuestion.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for AskQuestion
        AskQuestion.tStop = globalClock.getTime(format='float')
        AskQuestion.tStopRefresh = tThisFlipGlobal
        thisExp.addData('AskQuestion.stopped', AskQuestion.tStop)
        VideoQuestionSliderLoop.addData('slider_2.response', slider_2.getRating())
        VideoQuestionSliderLoop.addData('slider_2.rt', slider_2.getRT())
        # Run 'End Routine' code from SliderStuff
        # Get the slider's selected position
        slider_position = slider_2.markerPos
        
        # Map the slider position to the corresponding answer
        if slider_position == 1:
            chosen_answer = Answer_1
        elif slider_position == 2:
            chosen_answer = Answer_2
        elif slider_position == 3:
            chosen_answer = Answer_3
        elif slider_position == 4:
            chosen_answer = Answer_4
        else:
            chosen_answer = "No selection"
        
        # Print the result to the console for debugging
        print(f"Slider Position: {slider_position}, Chosen Answer: {chosen_answer}")
        
        # Log the chosen answer in the data file
        thisExp.addData('ChosenAnswer', chosen_answer)
        
        # Log correctness
        if chosen_answer == Target:  # Replace `Target` with the correct answer column from your conditions file
            thisExp.addData('Correct', 1)
            thisExp.addData('Score', 1)
        else:
            thisExp.addData('Correct', 0)
            thisExp.addData('Score', -1)
        
        
        
        # Run 'End Routine' code from QuestionDataCollectTime
        # Ensure slider has a valid response
        if slider_2.getRating() is None:
            thisExp.addData('slider_2.response', 'No Response')
            thisExp.addData('slider_2.rt', 'No Response')
        else:
            thisExp.addData('slider_2.response', slider_2.getRating())
            thisExp.addData('slider_2.rt', slider_2.getRT())
        
        # the Routine "AskQuestion" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "ConfidenceSlider" ---
        # create an object to store info about Routine ConfidenceSlider
        ConfidenceSlider = data.Routine(
            name='ConfidenceSlider',
            components=[confidence_slider, text_4, text_8],
        )
        ConfidenceSlider.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from Confidence_Slider_Controller
        # Initialize logging variables for confidence slider
        confidence_slider.reset()  # Reset slider state
        confidence_slider.markerPos = 5  # Neutral starting position (middle)
        t_confidence_start = globalClock.getTime()  # Log the time when slider is displayed
        print(f"Begin Routine: Confidence slider initialized with markerPos={confidence_slider.markerPos}")
        
        confidence_slider.reset()
        # store start times for ConfidenceSlider
        ConfidenceSlider.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        ConfidenceSlider.tStart = globalClock.getTime(format='float')
        ConfidenceSlider.status = STARTED
        thisExp.addData('ConfidenceSlider.started', ConfidenceSlider.tStart)
        ConfidenceSlider.maxDuration = None
        # keep track of which components have finished
        ConfidenceSliderComponents = ConfidenceSlider.components
        for thisComponent in ConfidenceSlider.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "ConfidenceSlider" ---
        # if trial has changed, end Routine now
        if isinstance(VideoQuestionSliderLoop, data.TrialHandler2) and thisVideoQuestionSliderLoop.thisN != VideoQuestionSliderLoop.thisTrial.thisN:
            continueRoutine = False
        ConfidenceSlider.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from Confidence_Slider_Controller
            # Detect arrow keys and move the slider marker
            keys = event.getKeys(['left', 'right', 'return'])
            
            if 'left' in keys and confidence_slider.markerPos > confidence_slider.ticks[0]:
                confidence_slider.markerPos -= 1  # Move left
                print(f"Each Frame: Marker moved left to {confidence_slider.markerPos}")
            elif 'right' in keys and confidence_slider.markerPos < confidence_slider.ticks[-1]:
                confidence_slider.markerPos += 1  # Move right
                print(f"Each Frame: Marker moved right to {confidence_slider.markerPos}")
            elif 'return' in keys:
                # Confirm the selection and end the routine
                print(f"Each Frame: 'Return' pressed. Final position: {confidence_slider.markerPos}")
                continueRoutine = False  # End the routine
            
            
            # *confidence_slider* updates
            
            # if confidence_slider is starting this frame...
            if confidence_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                confidence_slider.frameNStart = frameN  # exact frame index
                confidence_slider.tStart = t  # local t and not account for scr refresh
                confidence_slider.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(confidence_slider, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'confidence_slider.started')
                # update status
                confidence_slider.status = STARTED
                confidence_slider.setAutoDraw(True)
            
            # if confidence_slider is active this frame...
            if confidence_slider.status == STARTED:
                # update params
                pass
            
            # *text_4* updates
            
            # if text_4 is starting this frame...
            if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_4.frameNStart = frameN  # exact frame index
                text_4.tStart = t  # local t and not account for scr refresh
                text_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_4.started')
                # update status
                text_4.status = STARTED
                text_4.setAutoDraw(True)
            
            # if text_4 is active this frame...
            if text_4.status == STARTED:
                # update params
                pass
            
            # *text_8* updates
            
            # if text_8 is starting this frame...
            if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_8.frameNStart = frameN  # exact frame index
                text_8.tStart = t  # local t and not account for scr refresh
                text_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_8.started')
                # update status
                text_8.status = STARTED
                text_8.setAutoDraw(True)
            
            # if text_8 is active this frame...
            if text_8.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                ConfidenceSlider.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ConfidenceSlider.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ConfidenceSlider" ---
        for thisComponent in ConfidenceSlider.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for ConfidenceSlider
        ConfidenceSlider.tStop = globalClock.getTime(format='float')
        ConfidenceSlider.tStopRefresh = tThisFlipGlobal
        thisExp.addData('ConfidenceSlider.stopped', ConfidenceSlider.tStop)
        # Run 'End Routine' code from Confidence_Slider_Controller
        # Record the confidence slider's final position
        confidence_position = confidence_slider.markerPos
        
        # Add confidence data to the experiment output
        if confidence_position is not None:
            t_confidence_end = globalClock.getTime()  # Log end time
            confidence_rt = t_confidence_end - t_confidence_start  # Calculate response time
            print(f"End Routine: Confidence position={confidence_position}, RT={confidence_rt}")
            thisExp.addData('ConfidencePosition', confidence_position)
            thisExp.addData('ConfidenceRT', confidence_rt)
        else:
            print("No confidence rating recorded.")
            thisExp.addData('ConfidencePosition', "No selection")
            thisExp.addData('ConfidenceRT', "No response")
        
        VideoQuestionSliderLoop.addData('confidence_slider.response', confidence_slider.getRating())
        VideoQuestionSliderLoop.addData('confidence_slider.rt', confidence_slider.getRT())
        VideoQuestionSliderLoop.addData('confidence_slider.history', confidence_slider.getHistory())
        # the Routine "ConfidenceSlider" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'VideoQuestionSliderLoop'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "ThankYou" ---
    # create an object to store info about Routine ThankYou
    ThankYou = data.Routine(
        name='ThankYou',
        components=[Thanks],
    )
    ThankYou.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for ThankYou
    ThankYou.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    ThankYou.tStart = globalClock.getTime(format='float')
    ThankYou.status = STARTED
    thisExp.addData('ThankYou.started', ThankYou.tStart)
    ThankYou.maxDuration = None
    # keep track of which components have finished
    ThankYouComponents = ThankYou.components
    for thisComponent in ThankYou.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ThankYou" ---
    ThankYou.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 15.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Thanks* updates
        
        # if Thanks is starting this frame...
        if Thanks.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Thanks.frameNStart = frameN  # exact frame index
            Thanks.tStart = t  # local t and not account for scr refresh
            Thanks.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Thanks, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Thanks.started')
            # update status
            Thanks.status = STARTED
            Thanks.setAutoDraw(True)
        
        # if Thanks is active this frame...
        if Thanks.status == STARTED:
            # update params
            pass
        
        # if Thanks is stopping this frame...
        if Thanks.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Thanks.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                Thanks.tStop = t  # not accounting for scr refresh
                Thanks.tStopRefresh = tThisFlipGlobal  # on global time
                Thanks.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Thanks.stopped')
                # update status
                Thanks.status = FINISHED
                Thanks.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            ThankYou.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ThankYou.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ThankYou" ---
    for thisComponent in ThankYou.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for ThankYou
    ThankYou.tStop = globalClock.getTime(format='float')
    ThankYou.tStopRefresh = tThisFlipGlobal
    thisExp.addData('ThankYou.stopped', ThankYou.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if ThankYou.maxDurationReached:
        routineTimer.addTime(-ThankYou.maxDuration)
    elif ThankYou.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-15.000000)
    thisExp.nextEntry()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
