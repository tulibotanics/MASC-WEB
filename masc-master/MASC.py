#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.4),
    on November 27, 2024, at 10:04
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
        originPath='C:\\Uni\\Master\\Internship\\PsychoPyStuff\\MASC\\Builder\\MASC_fr\\MASC.py',
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
            winType='pyglet', allowGUI=False, allowStencil=False,
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
    if deviceManager.getDevice('key_resp_4') is None:
        # initialise key_resp_4
        key_resp_4 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_4',
        )
    if deviceManager.getDevice('key_resp') is None:
        # initialise key_resp
        key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp',
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
    
    # --- Initialize components for Routine "Instruction" ---
    WelcomeParticipant = visual.TextStim(win=win, name='WelcomeParticipant',
        text='Vous allez visionner un film d‘une durée de 15 minutes. Regardez attentivement ce film et essayez de comprendre ce que chaque personnage pense ou ressent.\n\n Appuyez sur une touche pour continuer.',
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
        text='Appuyez sur une touche pour continuer.',
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
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    Answer_A = visual.TextStim(win=win, name='Answer_A',
        text='',
        font='Arial',
        pos=(-0.3, 0), draggable=False, height=0.05, wrapWidth=0.5, ori=0.0, 
        color=[1.0000, 0.0000, 0.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    Answer_B = visual.TextStim(win=win, name='Answer_B',
        text='',
        font='Arial',
        pos=(-0.1, 0), draggable=False, height=0.05, wrapWidth=0.5, ori=0.0, 
        color=[-0.0000, 1.0000, 0.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    Answer_C = visual.TextStim(win=win, name='Answer_C',
        text='',
        font='Arial',
        pos=(0.1, 0), draggable=False, height=0.05, wrapWidth=0.5, ori=0.0, 
        color=[-0.0000, 0.0000, 1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    Answer_D = visual.TextStim(win=win, name='Answer_D',
        text='',
        font='Arial',
        pos=(0.3, 0), draggable=False, height=0.05, wrapWidth=0.5, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    key_resp = keyboard.Keyboard(deviceName='key_resp')
    
    # --- Initialize components for Routine "ConfidenceSlider" ---
    slider = visual.Slider(win=win, name='slider',
        startValue=5, size=(1.0, 0.1), pos=(0, 0), units=win.units,
        labels=["Pas confiant", "Très confiant "], ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9), granularity=1.0,
        style='rating', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='white', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.019,
        flip=False, ori=0.0, depth=0, readOnly=False)
    text_4 = visual.TextStim(win=win, name='text_4',
        text='Utilisez les touches fléchées pour naviguer et appuyez sur la touche Entrée pour valider votre sélection.',
        font='Arial',
        pos=(0, -0.3), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
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
    trials = data.TrialHandler2(
        name='trials',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('MASC_Characters.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            globals()[paramName] = thisTrial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrial in trials:
        currentLoop = trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
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
        if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
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
        trials.addData('key_resp_3.keys',key_resp_3.keys)
        if key_resp_3.keys != None:  # we had a response
            trials.addData('key_resp_3.rt', key_resp_3.rt)
            trials.addData('key_resp_3.duration', key_resp_3.duration)
        # the Routine "Characters" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # set up handler to look after randomisation of conditions etc
    VideoQuestionSlider = data.TrialHandler2(
        name='VideoQuestionSlider',
        nReps=43.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('MASC_Cleaned_SingleRowPerQuestion_Corrected.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(VideoQuestionSlider)  # add the loop to the experiment
    thisVideoQuestionSlider = VideoQuestionSlider.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisVideoQuestionSlider.rgb)
    if thisVideoQuestionSlider != None:
        for paramName in thisVideoQuestionSlider:
            globals()[paramName] = thisVideoQuestionSlider[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisVideoQuestionSlider in VideoQuestionSlider:
        currentLoop = VideoQuestionSlider
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisVideoQuestionSlider.rgb)
        if thisVideoQuestionSlider != None:
            for paramName in thisVideoQuestionSlider:
                globals()[paramName] = thisVideoQuestionSlider[paramName]
        
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
        if isinstance(VideoQuestionSlider, data.TrialHandler2) and thisVideoQuestionSlider.thisN != VideoQuestionSlider.thisTrial.thisN:
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
            if Clip.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Clip.tStartRefresh + 15-frameTolerance or Clip.isFinished:
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
            if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
        VideoQuestionSlider.addData('key_resp_4.keys',key_resp_4.keys)
        if key_resp_4.keys != None:  # we had a response
            VideoQuestionSlider.addData('key_resp_4.rt', key_resp_4.rt)
            VideoQuestionSlider.addData('key_resp_4.duration', key_resp_4.duration)
        # the Routine "PlayVideo" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "AskQuestion" ---
        # create an object to store info about Routine AskQuestion
        AskQuestion = data.Routine(
            name='AskQuestion',
            components=[Questions, Answer_A, Answer_B, Answer_C, Answer_D, key_resp],
        )
        AskQuestion.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        Questions.setText(Question)
        Answer_A.setText(Answer_1)
        Answer_B.setText(Answer_2)
        Answer_C.setText(Answer_3)
        Answer_D.setText(Answer_4)
        # create starting attributes for key_resp
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
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
        if isinstance(VideoQuestionSlider, data.TrialHandler2) and thisVideoQuestionSlider.thisN != VideoQuestionSlider.thisTrial.thisN:
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
            
            # *key_resp* updates
            waitOnFlip = False
            
            # if key_resp is starting this frame...
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp.started')
                # update status
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['1','2','3','4'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    key_resp.duration = _key_resp_allKeys[-1].duration
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
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
        VideoQuestionSlider.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            VideoQuestionSlider.addData('key_resp.rt', key_resp.rt)
            VideoQuestionSlider.addData('key_resp.duration', key_resp.duration)
        # the Routine "AskQuestion" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "ConfidenceSlider" ---
        # create an object to store info about Routine ConfidenceSlider
        ConfidenceSlider = data.Routine(
            name='ConfidenceSlider',
            components=[slider, text_4],
        )
        ConfidenceSlider.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        slider.reset()
        # Run 'Begin Routine' code from code
        # Python
        
        if slider.getRating() is None:
            slider.markerPos = int((slider.ticks[0] + slider.ticks[-1]) / 2)
        
        
        
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
        if isinstance(VideoQuestionSlider, data.TrialHandler2) and thisVideoQuestionSlider.thisN != VideoQuestionSlider.thisTrial.thisN:
            continueRoutine = False
        ConfidenceSlider.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *slider* updates
            
            # if slider is starting this frame...
            if slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                slider.frameNStart = frameN  # exact frame index
                slider.tStart = t  # local t and not account for scr refresh
                slider.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slider, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider.started')
                # update status
                slider.status = STARTED
                slider.setAutoDraw(True)
            
            # if slider is active this frame...
            if slider.status == STARTED:
                # update params
                slider.setFillColor('Red', log=False)
            
            # Check slider for response to end Routine
            if slider.getRating() is not None and slider.status == STARTED:
                continueRoutine = False
            # Run 'Each Frame' code from code
            # Detect arrow keys and move slider marker
            keys = event.getKeys(['left', 'right', 'return'])
            
            if 'left' in keys and slider.markerPos > slider.ticks[0]:
                slider.markerPos -= 1
            elif 'right' in keys and slider.markerPos < slider.ticks[-1]:
                slider.markerPos += 1
            elif 'return' in keys:
                # Save the slider rating and end the routine
                thisExp.addData('slider.response', slider.markerPos)  # Save the rating
                continueRoutine = False  # End the routine
            
            
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
        VideoQuestionSlider.addData('slider.response', slider.getRating())
        VideoQuestionSlider.addData('slider.rt', slider.getRT())
        # the Routine "ConfidenceSlider" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 43.0 repeats of 'VideoQuestionSlider'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
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
