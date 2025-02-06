/************* 
 * Masc *
 *************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2024.2.4.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'MASC';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'session': '001',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); },flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);


const trials_2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_2LoopBegin(trials_2LoopScheduler));
flowScheduler.add(trials_2LoopScheduler);
flowScheduler.add(trials_2LoopEnd);


const trials_3LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_3LoopBegin(trials_3LoopScheduler));
flowScheduler.add(trials_3LoopScheduler);
flowScheduler.add(trials_3LoopEnd);


flowScheduler.add(CountryOfResidenceRoutineBegin());
flowScheduler.add(CountryOfResidenceRoutineEachFrame());
flowScheduler.add(CountryOfResidenceRoutineEnd());
flowScheduler.add(InstructionRoutineBegin());
flowScheduler.add(InstructionRoutineEachFrame());
flowScheduler.add(InstructionRoutineEnd());
const CharactersLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(CharactersLoopLoopBegin(CharactersLoopLoopScheduler));
flowScheduler.add(CharactersLoopLoopScheduler);
flowScheduler.add(CharactersLoopLoopEnd);


const InstructionsLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(InstructionsLoopLoopBegin(InstructionsLoopLoopScheduler));
flowScheduler.add(InstructionsLoopLoopScheduler);
flowScheduler.add(InstructionsLoopLoopEnd);


const VideoQuestionSliderLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(VideoQuestionSliderLoopLoopBegin(VideoQuestionSliderLoopLoopScheduler));
flowScheduler.add(VideoQuestionSliderLoopLoopScheduler);
flowScheduler.add(VideoQuestionSliderLoopLoopEnd);




flowScheduler.add(ThankYouRoutineBegin());
flowScheduler.add(ThankYouRoutineEachFrame());
flowScheduler.add(ThankYouRoutineEnd());
flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'MASC_Characters.xlsx', 'path': 'MASC_Characters.xlsx'},
    {'name': 'Anna.png', 'path': 'Anna.png'},
    {'name': 'Ben.png', 'path': 'Ben.png'},
    {'name': 'Marie.png', 'path': 'Marie.png'},
    {'name': 'Michael.png', 'path': 'Michael.png'},
    {'name': 'MASC_Instructions.xlsx', 'path': 'MASC_Instructions.xlsx'},
    {'name': 'MASC_Cleaned_SingleRowPerQuestion_Corrected (1).xlsx', 'path': 'MASC_Cleaned_SingleRowPerQuestion_Corrected (1).xlsx'},
    {'name': '01.mp4', 'path': '01.mp4'},
    {'name': '02.mp4', 'path': '02.mp4'},
    {'name': '03.mp4', 'path': '03.mp4'},
    {'name': '04.mp4', 'path': '04.mp4'},
    {'name': '05.mp4', 'path': '05.mp4'},
    {'name': '06-07.mp4', 'path': '06-07.mp4'},
    {'name': '08.mp4', 'path': '08.mp4'},
    {'name': '09.mp4', 'path': '09.mp4'},
    {'name': '10.mp4', 'path': '10.mp4'},
    {'name': '11.mp4', 'path': '11.mp4'},
    {'name': '12.mp4', 'path': '12.mp4'},
    {'name': '13.mp4', 'path': '13.mp4'},
    {'name': '14.mp4', 'path': '14.mp4'},
    {'name': '15.mp4', 'path': '15.mp4'},
    {'name': '16.mp4', 'path': '16.mp4'},
    {'name': '17.mp4', 'path': '17.mp4'},
    {'name': '18.mp4', 'path': '18.mp4'},
    {'name': '19.mp4', 'path': '19.mp4'},
    {'name': '20.mp4', 'path': '20.mp4'},
    {'name': '21.mp4', 'path': '21.mp4'},
    {'name': '22-23.mp4', 'path': '22-23.mp4'},
    {'name': '24.mp4', 'path': '24.mp4'},
    {'name': '25.mp4', 'path': '25.mp4'},
    {'name': '26.mp4', 'path': '26.mp4'},
    {'name': '27.mp4', 'path': '27.mp4'},
    {'name': '28.mp4', 'path': '28.mp4'},
    {'name': '29.mp4', 'path': '29.mp4'},
    {'name': '30.mp4', 'path': '30.mp4'},
    {'name': '31.mp4', 'path': '31.mp4'},
    {'name': '32.mp4', 'path': '32.mp4'},
    {'name': '33.mp4', 'path': '33.mp4'},
    {'name': '34.mp4', 'path': '34.mp4'},
    {'name': '35.mp4', 'path': '35.mp4'},
    {'name': '36-37.mp4', 'path': '36-37.mp4'},
    {'name': '38.mp4', 'path': '38.mp4'},
    {'name': '39.mp4', 'path': '39.mp4'},
    {'name': '40.mp4', 'path': '40.mp4'},
    {'name': '41.mp4', 'path': '41.mp4'},
    {'name': '42.mp4', 'path': '42.mp4'},
    {'name': '43.mp4', 'path': '43.mp4'},
    {'name': '44.mp4', 'path': '44.mp4'},
    {'name': '45.mp4', 'path': '45.mp4'},
    {'name': '46.mp4', 'path': '46.mp4'},
    {'name': 'default.png', 'path': 'https://pavlovia.org/assets/default/default.png'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.INFO);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2024.2.4';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var EthicsClock;
var text_10;
var EthicsSlider;
var InstructionEthicsSlider;
var AgeRangeClock;
var AgeQuestion;
var Age_slider;
var InstructionAgeSlider;
var GenderClock;
var GenderQuestion;
var Gender_slider;
var InstructionGenderSlider;
var CountryOfResidenceClock;
var text_7;
var textbox;
var InstructionClock;
var WelcomeParticipant;
var key_resp_2;
var CharactersClock;
var text_2;
var text_3;
var Character;
var key_resp_3;
var Instruction2Clock;
var text_5;
var key_resp_5;
var text_6;
var PlayVideoClock;
var ClipClock;
var Clip;
var key_resp_4;
var AskQuestionClock;
var Questions;
var Answer_A;
var Answer_B;
var Answer_C;
var Answer_D;
var slider_2;
var InstructionSlider;
var ConfidenceSliderClock;
var confidence_slider;
var text_4;
var text_8;
var ThankYouClock;
var Thanks;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "Ethics"
  EthicsClock = new util.Clock();
  text_10 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_10',
    text: "La participation à cette étude est entièrement volontaire, et un consentement éclairé est obtenu avant le début de celle-ci. Les participants sont assurés de l'anonymat et de la confidentialité, toutes les données étant stockées de manière sécurisée et utilisées uniquement à des fins de recherche. L'étude présente un risque minimal pour les participants, qui peuvent se retirer à tout moment sans conséquence. L'approbation éthique de cette étude a été obtenue auprès de Centre Hospitalaire Universitaire Vaudoise.",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.2], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  EthicsSlider = new visual.Slider({
    win: psychoJS.window, name: 'EthicsSlider',
    startValue: 1,
    size: [1.0, 0.1], pos: [0, (- 0.08)], ori: 0.0, units: psychoJS.window.units,
    labels: ["Oui", "Non"], fontSize: 0.05, ticks: [1, 2],
    granularity: 1.0, style: ["RATING", "TRIANGLE_MARKER"],
    color: new util.Color('LightGray'), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Open Sans', bold: true, italic: false, depth: -1, 
    flip: false,
  });
  
  InstructionEthicsSlider = new visual.TextStim({
    win: psychoJS.window,
    name: 'InstructionEthicsSlider',
    text: 'Utilisez les touches fléchées pour naviguer et appuyez sur la touche Entrée pour valider votre sélection.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], draggable: false, height: 0.025,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  // Initialize components for Routine "AgeRange"
  AgeRangeClock = new util.Clock();
  AgeQuestion = new visual.TextStim({
    win: psychoJS.window,
    name: 'AgeQuestion',
    text: 'À quelle tranche d’âge vous identifiez-vous ?',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.25], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  Age_slider = new visual.Slider({
    win: psychoJS.window, name: 'Age_slider',
    startValue: 1,
    size: [1.0, 0.1], pos: [0, 0], ori: 0.0, units: psychoJS.window.units,
    labels: ["18-29", "30-39", "40-49", "50-59", "60-69", "70-79", "80+"], fontSize: 0.03, ticks: [1, 2, 3, 4, 5, 6, 7],
    granularity: 1.0, style: ["RATING", "TRIANGLE_MARKER"],
    color: new util.Color('White'), markerColor: new util.Color('Red'), lineColor: new util.Color('Gray'), 
    opacity: undefined, fontFamily: 'Open Sans', bold: true, italic: false, depth: -2, 
    flip: false,
  });
  
  InstructionAgeSlider = new visual.TextStim({
    win: psychoJS.window,
    name: 'InstructionAgeSlider',
    text: 'Utilisez les touches fléchées pour naviguer et appuyez sur la touche Entrée pour valider votre sélection.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], draggable: false, height: 0.025,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  // Initialize components for Routine "Gender"
  GenderClock = new util.Clock();
  GenderQuestion = new visual.TextStim({
    win: psychoJS.window,
    name: 'GenderQuestion',
    text: 'À quel sexe vous identifiez-vous ?',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.25], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  Gender_slider = new visual.Slider({
    win: psychoJS.window, name: 'Gender_slider',
    startValue: 1,
    size: [1.0, 0.1], pos: [0, 0], ori: 0.0, units: psychoJS.window.units,
    labels: ["Femme", "Homme", "Autre", "Je pr\u00e9f\u00e8re ne pas le dire"], fontSize: 0.03, ticks: [1, 2, 3, 4],
    granularity: 1.0, style: ["RATING", "TRIANGLE_MARKER"],
    color: new util.Color('White'), markerColor: new util.Color('Red'), lineColor: new util.Color('Gray'), 
    opacity: undefined, fontFamily: 'Open Sans', bold: true, italic: false, depth: -2, 
    flip: false,
  });
  
  InstructionGenderSlider = new visual.TextStim({
    win: psychoJS.window,
    name: 'InstructionGenderSlider',
    text: 'Utilisez les touches fléchées pour naviguer et appuyez sur la touche Entrée pour valider votre sélection.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], draggable: false, height: 0.025,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  // Initialize components for Routine "CountryOfResidence"
  CountryOfResidenceClock = new util.Clock();
  text_7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_7',
    text: 'Quel est votre pays de résidence ?',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.25], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  textbox = new visual.TextBox({
    win: psychoJS.window,
    name: 'textbox',
    text: 'Enter text',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0], 
    draggable: false,
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [0.5, 0.5],  units: undefined, 
    ori: 0.0,
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  // Initialize components for Routine "Instruction"
  InstructionClock = new util.Clock();
  WelcomeParticipant = new visual.TextStim({
    win: psychoJS.window,
    name: 'WelcomeParticipant',
    text: 'Vous allez visionner un film d‘une durée de 15 minutes. Regardez attentivement ce film et essayez de comprendre ce que chaque personnage pense ou ressent.\n\n Appuyez sur la touche espace pour continuer.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Characters"
  CharactersClock = new util.Clock();
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.35], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: 'Appuyez sur la touche espace pour continuer.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  Character = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Character', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.629, 0.418],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Instruction2"
  Instruction2Clock = new util.Clock();
  text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_5',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_6',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  // Initialize components for Routine "PlayVideo"
  PlayVideoClock = new util.Clock();
  ClipClock = new util.Clock();
  Clip = new visual.MovieStim({
    win: psychoJS.window,
    name: 'Clip',
    units: psychoJS.window.units,
    movie: undefined,
    pos: [0, 0],
    anchor: 'center',
    size: [0.64, 0.48],
    ori: 0.0,
    opacity: undefined,
    loop: false,
    noAudio: false,
    depth: 0
    });
  key_resp_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "AskQuestion"
  AskQuestionClock = new util.Clock();
  Questions = new visual.TextStim({
    win: psychoJS.window,
    name: 'Questions',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.35], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  Answer_A = new visual.TextStim({
    win: psychoJS.window,
    name: 'Answer_A',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), (- 0.1)], draggable: false, height: 0.04,  wrapWidth: 0.3, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  Answer_B = new visual.TextStim({
    win: psychoJS.window,
    name: 'Answer_B',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.16), (- 0.1)], draggable: false, height: 0.04,  wrapWidth: 0.3, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  Answer_C = new visual.TextStim({
    win: psychoJS.window,
    name: 'Answer_C',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.16, (- 0.1)], draggable: false, height: 0.04,  wrapWidth: 0.3, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  Answer_D = new visual.TextStim({
    win: psychoJS.window,
    name: 'Answer_D',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.5, (- 0.1)], draggable: false, height: 0.04,  wrapWidth: 0.2, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  slider_2 = new visual.Slider({
    win: psychoJS.window, name: 'slider_2',
    startValue: 1,
    size: [1.0, 0.1], pos: [0, 0.1], ori: 0.0, units: psychoJS.window.units,
    labels: undefined, fontSize: 0.01, ticks: [1, 2, 3, 4],
    granularity: 1.0, style: ["RATING", "TRIANGLE_MARKER"],
    color: new util.Color('LightGray'), markerColor: new util.Color('Red'), lineColor: new util.Color('Gray'), 
    opacity: undefined, fontFamily: 'Open Sans', bold: true, italic: false, depth: -5, 
    flip: false,
  });
  
  InstructionSlider = new visual.TextStim({
    win: psychoJS.window,
    name: 'InstructionSlider',
    text: 'Utilisez les touches fléchées pour naviguer et appuyez sur la touche Entrée pour valider votre sélection.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], draggable: false, height: 0.025,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -7.0 
  });
  
  // Initialize components for Routine "ConfidenceSlider"
  ConfidenceSliderClock = new util.Clock();
  confidence_slider = new visual.Slider({
    win: psychoJS.window, name: 'confidence_slider',
    startValue: 5,
    size: [1.0, 0.1], pos: [0, 0], ori: 0.0, units: psychoJS.window.units,
    labels: ["Pas confiant", "Ni confiant, ni pas confiant", "Tr\u00e8s confiant"], fontSize: 0.019, ticks: [1, 2, 3, 4, 5, 6, 7, 8, 9],
    granularity: 1.0, style: ["RATING", "TRIANGLE_MARKER"],
    color: new util.Color('LightGray'), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Open Sans', bold: true, italic: false, depth: -1, 
    flip: false,
  });
  
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: 'Utilisez les touches fléchées pour naviguer et appuyez sur la touche Entrée pour valider votre sélection.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], draggable: false, height: 0.025,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  text_8 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_8',
    text: 'A quel point êtes vous sur de votre réponse?',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.35], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  // Initialize components for Routine "ThankYou"
  ThankYouClock = new util.Clock();
  Thanks = new visual.TextStim({
    win: psychoJS.window,
    name: 'Thanks',
    text: "Vous avez terminé l'experience. Merci de votre participation.",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial of trials) {
      snapshot = trials.getSnapshot();
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(EthicsRoutineBegin(snapshot));
      trialsLoopScheduler.add(EthicsRoutineEachFrame());
      trialsLoopScheduler.add(EthicsRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials_2;
function trials_2LoopBegin(trials_2LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_2 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'trials_2'
    });
    psychoJS.experiment.addLoop(trials_2); // add the loop to the experiment
    currentLoop = trials_2;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_2 of trials_2) {
      snapshot = trials_2.getSnapshot();
      trials_2LoopScheduler.add(importConditions(snapshot));
      trials_2LoopScheduler.add(AgeRangeRoutineBegin(snapshot));
      trials_2LoopScheduler.add(AgeRangeRoutineEachFrame());
      trials_2LoopScheduler.add(AgeRangeRoutineEnd(snapshot));
      trials_2LoopScheduler.add(trials_2LoopEndIteration(trials_2LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_2LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_2);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_2LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials_3;
function trials_3LoopBegin(trials_3LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_3 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'trials_3'
    });
    psychoJS.experiment.addLoop(trials_3); // add the loop to the experiment
    currentLoop = trials_3;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_3 of trials_3) {
      snapshot = trials_3.getSnapshot();
      trials_3LoopScheduler.add(importConditions(snapshot));
      trials_3LoopScheduler.add(GenderRoutineBegin(snapshot));
      trials_3LoopScheduler.add(GenderRoutineEachFrame());
      trials_3LoopScheduler.add(GenderRoutineEnd(snapshot));
      trials_3LoopScheduler.add(trials_3LoopEndIteration(trials_3LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_3LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_3);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_3LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var CharactersLoop;
function CharactersLoopLoopBegin(CharactersLoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    CharactersLoop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'MASC_Characters.xlsx',
      seed: undefined, name: 'CharactersLoop'
    });
    psychoJS.experiment.addLoop(CharactersLoop); // add the loop to the experiment
    currentLoop = CharactersLoop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisCharactersLoop of CharactersLoop) {
      snapshot = CharactersLoop.getSnapshot();
      CharactersLoopLoopScheduler.add(importConditions(snapshot));
      CharactersLoopLoopScheduler.add(CharactersRoutineBegin(snapshot));
      CharactersLoopLoopScheduler.add(CharactersRoutineEachFrame());
      CharactersLoopLoopScheduler.add(CharactersRoutineEnd(snapshot));
      CharactersLoopLoopScheduler.add(CharactersLoopLoopEndIteration(CharactersLoopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function CharactersLoopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(CharactersLoop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function CharactersLoopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var InstructionsLoop;
function InstructionsLoopLoopBegin(InstructionsLoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    InstructionsLoop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'MASC_Instructions.xlsx',
      seed: undefined, name: 'InstructionsLoop'
    });
    psychoJS.experiment.addLoop(InstructionsLoop); // add the loop to the experiment
    currentLoop = InstructionsLoop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisInstructionsLoop of InstructionsLoop) {
      snapshot = InstructionsLoop.getSnapshot();
      InstructionsLoopLoopScheduler.add(importConditions(snapshot));
      InstructionsLoopLoopScheduler.add(Instruction2RoutineBegin(snapshot));
      InstructionsLoopLoopScheduler.add(Instruction2RoutineEachFrame());
      InstructionsLoopLoopScheduler.add(Instruction2RoutineEnd(snapshot));
      InstructionsLoopLoopScheduler.add(InstructionsLoopLoopEndIteration(InstructionsLoopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function InstructionsLoopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(InstructionsLoop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function InstructionsLoopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var VideoQuestionSliderLoop;
function VideoQuestionSliderLoopLoopBegin(VideoQuestionSliderLoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    VideoQuestionSliderLoop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'MASC_Cleaned_SingleRowPerQuestion_Corrected (1).xlsx',
      seed: undefined, name: 'VideoQuestionSliderLoop'
    });
    psychoJS.experiment.addLoop(VideoQuestionSliderLoop); // add the loop to the experiment
    currentLoop = VideoQuestionSliderLoop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisVideoQuestionSliderLoop of VideoQuestionSliderLoop) {
      snapshot = VideoQuestionSliderLoop.getSnapshot();
      VideoQuestionSliderLoopLoopScheduler.add(importConditions(snapshot));
      VideoQuestionSliderLoopLoopScheduler.add(PlayVideoRoutineBegin(snapshot));
      VideoQuestionSliderLoopLoopScheduler.add(PlayVideoRoutineEachFrame());
      VideoQuestionSliderLoopLoopScheduler.add(PlayVideoRoutineEnd(snapshot));
      VideoQuestionSliderLoopLoopScheduler.add(AskQuestionRoutineBegin(snapshot));
      VideoQuestionSliderLoopLoopScheduler.add(AskQuestionRoutineEachFrame());
      VideoQuestionSliderLoopLoopScheduler.add(AskQuestionRoutineEnd(snapshot));
      VideoQuestionSliderLoopLoopScheduler.add(ConfidenceSliderRoutineBegin(snapshot));
      VideoQuestionSliderLoopLoopScheduler.add(ConfidenceSliderRoutineEachFrame());
      VideoQuestionSliderLoopLoopScheduler.add(ConfidenceSliderRoutineEnd(snapshot));
      VideoQuestionSliderLoopLoopScheduler.add(VideoQuestionSliderLoopLoopEndIteration(VideoQuestionSliderLoopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function VideoQuestionSliderLoopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(VideoQuestionSliderLoop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function VideoQuestionSliderLoopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var t;
var frameN;
var continueRoutine;
var EthicsMaxDurationReached;
var slider_position;
var EthicsMaxDuration;
var EthicsComponents;
function EthicsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Ethics' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    EthicsClock.reset();
    routineTimer.reset();
    EthicsMaxDurationReached = false;
    // update component parameters for each repeat
    EthicsSlider.reset()
    // Run 'Begin Routine' code from EthicsSliderController
    slider_position = 0;
    EthicsSlider.markerPos = slider_position;
    
    psychoJS.experiment.addData('Ethics.started', globalClock.getTime());
    EthicsMaxDuration = null
    // keep track of which components have finished
    EthicsComponents = [];
    EthicsComponents.push(text_10);
    EthicsComponents.push(EthicsSlider);
    EthicsComponents.push(InstructionEthicsSlider);
    
    for (const thisComponent of EthicsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var _pj;
var keys;
function EthicsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Ethics' ---
    // get current time
    t = EthicsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_10* updates
    if (t >= 0.0 && text_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_10.tStart = t;  // (not accounting for frame time here)
      text_10.frameNStart = frameN;  // exact frame index
      
      text_10.setAutoDraw(true);
    }
    
    
    // *EthicsSlider* updates
    if (t >= 0.0 && EthicsSlider.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      EthicsSlider.tStart = t;  // (not accounting for frame time here)
      EthicsSlider.frameNStart = frameN;  // exact frame index
      
      EthicsSlider.setAutoDraw(true);
    }
    
    
    // Check EthicsSlider for response to end Routine
    if (EthicsSlider.getRating() !== undefined && EthicsSlider.status === PsychoJS.Status.STARTED) {
      continueRoutine = false; }
    // Run 'Each Frame' code from EthicsSliderController
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    keys = psychoJS.eventManager.getKeys(["left", "right", "return"]);
    if ((_pj.in_es6("left", keys) && (EthicsSlider.markerPos > EthicsSlider.ticks[0]))) {
        EthicsSlider.markerPos -= 1;
    } else {
        if ((_pj.in_es6("right", keys) && (EthicsSlider.markerPos < EthicsSlider.ticks.slice((- 1))[0]))) {
            EthicsSlider.markerPos += 1;
        } else {
            if (_pj.in_es6("return", keys)) {
                continueRoutine = false;
            }
        }
    }
    
    
    // *InstructionEthicsSlider* updates
    if (t >= 0.0 && InstructionEthicsSlider.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      InstructionEthicsSlider.tStart = t;  // (not accounting for frame time here)
      InstructionEthicsSlider.frameNStart = frameN;  // exact frame index
      
      InstructionEthicsSlider.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of EthicsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var chosen_value;
function EthicsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Ethics' ---
    for (const thisComponent of EthicsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Ethics.stopped', globalClock.getTime());
    psychoJS.experiment.addData('EthicsSlider.response', EthicsSlider.getRating());
    psychoJS.experiment.addData('EthicsSlider.rt', EthicsSlider.getRT());
    psychoJS.experiment.addData('EthicsSlider.history', EthicsSlider.getHistory());
    // Run 'End Routine' code from EthicsSliderController
    // Define the labels for the Ethics slider
    const ethics_labels = ["Oui", "Non"];
    
    // Get the slider position (markerPos)
    let slider_position = EthicsSlider.markerPos;
    
    // Map position to label
    let chosen_value;
    if (slider_position >= 1 && slider_position <= ethics_labels.length) {
        chosen_value = ethics_labels[slider_position - 1];
    } else {
        chosen_value = "No Response";
    }
    
    // Log the data
    psychoJS.experiment.addData('EthicsSlider_position', slider_position);
    psychoJS.experiment.addData('EthicsSlider.response', chosen_value);
    psychoJS.experiment.addData('EthicsSlider.rt', EthicsSlider.rt);
    
    // the Routine "Ethics" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var AgeRangeMaxDurationReached;
var AgeRangeMaxDuration;
var AgeRangeComponents;
function AgeRangeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'AgeRange' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    AgeRangeClock.reset();
    routineTimer.reset();
    AgeRangeMaxDurationReached = false;
    // update component parameters for each repeat
    Age_slider.reset()
    psychoJS.experiment.addData('AgeRange.started', globalClock.getTime());
    AgeRangeMaxDuration = null
    // keep track of which components have finished
    AgeRangeComponents = [];
    AgeRangeComponents.push(AgeQuestion);
    AgeRangeComponents.push(Age_slider);
    AgeRangeComponents.push(InstructionAgeSlider);
    
    for (const thisComponent of AgeRangeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function AgeRangeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'AgeRange' ---
    // get current time
    t = AgeRangeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from AgeRange_slider_controller
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    keys = psychoJS.eventManager.getKeys(["left", "right", "return"]);
    if ((_pj.in_es6("left", keys) && (Age_slider.markerPos > Age_slider.ticks[0]))) {
        Age_slider.markerPos -= 1;
    } else {
        if ((_pj.in_es6("right", keys) && (Age_slider.markerPos < Age_slider.ticks.slice((- 1))[0]))) {
            Age_slider.markerPos += 1;
        } else {
            if (_pj.in_es6("return", keys)) {
                continueRoutine = false;
            }
        }
    }
    
    
    // *AgeQuestion* updates
    if (t >= 0.0 && AgeQuestion.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      AgeQuestion.tStart = t;  // (not accounting for frame time here)
      AgeQuestion.frameNStart = frameN;  // exact frame index
      
      AgeQuestion.setAutoDraw(true);
    }
    
    
    // *Age_slider* updates
    if (t >= 0.0 && Age_slider.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Age_slider.tStart = t;  // (not accounting for frame time here)
      Age_slider.frameNStart = frameN;  // exact frame index
      
      Age_slider.setAutoDraw(true);
    }
    
    
    // Check Age_slider for response to end Routine
    if (Age_slider.getRating() !== undefined && Age_slider.status === PsychoJS.Status.STARTED) {
      continueRoutine = false; }
    
    // *InstructionAgeSlider* updates
    if (t >= 0.0 && InstructionAgeSlider.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      InstructionAgeSlider.tStart = t;  // (not accounting for frame time here)
      InstructionAgeSlider.frameNStart = frameN;  // exact frame index
      
      InstructionAgeSlider.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of AgeRangeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function AgeRangeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'AgeRange' ---
    for (const thisComponent of AgeRangeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('AgeRange.stopped', globalClock.getTime());
    psychoJS.experiment.addData('Age_slider.response', Age_slider.getRating());
    psychoJS.experiment.addData('Age_slider.rt', Age_slider.getRT());
    psychoJS.experiment.addData('Age_slider.history', Age_slider.getHistory());
    // Run 'End Routine' code from CollectAgeData
    // Define the labels for the age ranges
    const age_labels = ["18-29", "30-39", "40-49", "50-59", "60-69", "70-79", "80+"];
    
    // Get the slider position (markerPos)
    let slider_position = Age_slider.markerPos;
    
    // Map position to label
    let chosen_value;
    if (slider_position >= 1 && slider_position <= age_labels.length) {
        chosen_value = age_labels[slider_position - 1];
    } else {
        chosen_value = "No Response";
    }
    
    // Log the data
    psychoJS.experiment.addData('Age_slider_position', slider_position);
    psychoJS.experiment.addData('Age_slider.response', chosen_value);
    psychoJS.experiment.addData('Age_slider.rt', Age_slider.rt);
    
    // the Routine "AgeRange" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var GenderMaxDurationReached;
var GenderMaxDuration;
var GenderComponents;
function GenderRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Gender' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    GenderClock.reset();
    routineTimer.reset();
    GenderMaxDurationReached = false;
    // update component parameters for each repeat
    Gender_slider.reset()
    psychoJS.experiment.addData('Gender.started', globalClock.getTime());
    GenderMaxDuration = null
    // keep track of which components have finished
    GenderComponents = [];
    GenderComponents.push(GenderQuestion);
    GenderComponents.push(Gender_slider);
    GenderComponents.push(InstructionGenderSlider);
    
    for (const thisComponent of GenderComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function GenderRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Gender' ---
    // get current time
    t = GenderClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from Gender_slider_controller
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    keys = psychoJS.eventManager.getKeys(["left", "right", "return"]);
    if ((_pj.in_es6("left", keys) && (Gender_slider.markerPos > Gender_slider.ticks[0]))) {
        Gender_slider.markerPos -= 1;
    } else {
        if ((_pj.in_es6("right", keys) && (Gender_slider.markerPos < Gender_slider.ticks.slice((- 1))[0]))) {
            Gender_slider.markerPos += 1;
        } else {
            if (_pj.in_es6("return", keys)) {
                continueRoutine = false;
            }
        }
    }
    
    
    // *GenderQuestion* updates
    if (t >= 0.0 && GenderQuestion.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      GenderQuestion.tStart = t;  // (not accounting for frame time here)
      GenderQuestion.frameNStart = frameN;  // exact frame index
      
      GenderQuestion.setAutoDraw(true);
    }
    
    
    // *Gender_slider* updates
    if (t >= 0.0 && Gender_slider.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Gender_slider.tStart = t;  // (not accounting for frame time here)
      Gender_slider.frameNStart = frameN;  // exact frame index
      
      Gender_slider.setAutoDraw(true);
    }
    
    
    // *InstructionGenderSlider* updates
    if (t >= 0.0 && InstructionGenderSlider.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      InstructionGenderSlider.tStart = t;  // (not accounting for frame time here)
      InstructionGenderSlider.frameNStart = frameN;  // exact frame index
      
      InstructionGenderSlider.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of GenderComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var Gender_slider_position;
var labels;
function GenderRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Gender' ---
    for (const thisComponent of GenderComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Gender.stopped', globalClock.getTime());
    // Run 'End Routine' code from Gender_slider_controller
    Gender_slider_position = Gender_slider.markerPos;
    psychoJS.experiment.addData("Gender_slider_position", Gender_slider_position);
    
    psychoJS.experiment.addData('Gender_slider.response', Gender_slider.getRating());
    psychoJS.experiment.addData('Gender_slider.rt', Gender_slider.getRT());
    psychoJS.experiment.addData('Gender_slider.history', Gender_slider.getHistory());
    // Run 'End Routine' code from CollectGenderData
    labels = ["Femme", "Homme", "Autre", "Je pr\u00e9f\u00e8re ne pas le dire"];
    slider_position = Gender_slider.markerPos;
    if ((slider_position === 1)) {
        chosen_value = labels[0];
    } else {
        if ((slider_position === 2)) {
            chosen_value = labels[1];
        } else {
            if ((slider_position === 3)) {
                chosen_value = labels[2];
            } else {
                if ((slider_position === 4)) {
                    chosen_value = labels[3];
                } else {
                    chosen_value = "No Selection";
                }
            }
        }
    }
    psychoJS.experiment.addData("Gender_slider_position", slider_position);
    psychoJS.experiment.addData("Gender_slider.response", chosen_value);
    psychoJS.experiment.addData("Gender_slider.rt", Gender_slider.getRT());
    
    // the Routine "Gender" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var CountryOfResidenceMaxDurationReached;
var text_entered;
var typing_enabled;
var instruction_text;
var CountryOfResidenceMaxDuration;
var CountryOfResidenceComponents;
function CountryOfResidenceRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'CountryOfResidence' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    CountryOfResidenceClock.reset();
    routineTimer.reset();
    CountryOfResidenceMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from Type_Controller
    text_entered = "";
    typing_enabled = false;
    instruction_text = "Appuyez sur 'T' pour commencer a taper et sur 'Entree ' pour soumettre.";
    textbox.setText(instruction_text);
    
    psychoJS.experiment.addData('CountryOfResidence.started', globalClock.getTime());
    CountryOfResidenceMaxDuration = null
    // keep track of which components have finished
    CountryOfResidenceComponents = [];
    CountryOfResidenceComponents.push(text_7);
    CountryOfResidenceComponents.push(textbox);
    
    for (const thisComponent of CountryOfResidenceComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function CountryOfResidenceRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'CountryOfResidence' ---
    // get current time
    t = CountryOfResidenceClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_7* updates
    if (t >= 0.0 && text_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_7.tStart = t;  // (not accounting for frame time here)
      text_7.frameNStart = frameN;  // exact frame index
      
      text_7.setAutoDraw(true);
    }
    
    
    // *textbox* updates
    if (t >= 0.0 && textbox.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textbox.tStart = t;  // (not accounting for frame time here)
      textbox.frameNStart = frameN;  // exact frame index
      
      textbox.setAutoDraw(true);
    }
    
    // Run 'Each Frame' code from Type_Controller
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (-1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    
    keys = psychoJS.eventManager.getKeys();
    if (keys) {
        console.log(`Keys pressed: ${keys}`);
    }
    
    if (typing_enabled) {
        for (var key, _pj_c = 0, _pj_a = keys, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
            key = _pj_a[_pj_c];
    
            if (key === "return") {  // Submit input
                console.log(`Input submitted: '${text_entered}'`);
                psychoJS.experiment.addData("Country", text_entered);
                continueRoutine = false;
                typing_enabled = false;
    
            } else if (key === "backspace") {  // Handle backspace
                if (text_entered.length > 0) {
                    text_entered = text_entered.slice(0, -1);
                    console.log(`Backspace pressed. Updated text: '${text_entered}'`);
                }
    
            } else if (key === "period") {  // Handle period
                text_entered += ".";
                console.log(`Period pressed. Updated text: '${text_entered}'`);
    
            } else if (key === "space") {  // Handle space
                text_entered += " ";
                console.log(`Space pressed. Updated text: '${text_entered}'`);
    
            } else if (key.length === 1) {  // Handle single characters
                text_entered += key;
                console.log(`Key '${key}' added. Updated text: '${text_entered}'`);
            }
        }
    
        // Update the textbox
        textbox.setText(text_entered);
    
    } else if (_pj.in_es6("t", keys)) {  // Enable typing on 't' key
        typing_enabled = true;
        text_entered = "";
        textbox.setText("");
        console.log("Typing enabled. Textbox cleared.");
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of CountryOfResidenceComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function CountryOfResidenceRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'CountryOfResidence' ---
    for (const thisComponent of CountryOfResidenceComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('CountryOfResidence.stopped', globalClock.getTime());
    // Run 'End Routine' code from Type_Controller
    // Save the entered text
    psychoJS.experiment.addData('Country', text_entered);
    
    
    // the Routine "CountryOfResidence" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var InstructionMaxDurationReached;
var _key_resp_2_allKeys;
var InstructionMaxDuration;
var InstructionComponents;
function InstructionRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Instruction' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    InstructionClock.reset();
    routineTimer.reset();
    InstructionMaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    psychoJS.experiment.addData('Instruction.started', globalClock.getTime());
    InstructionMaxDuration = null
    // keep track of which components have finished
    InstructionComponents = [];
    InstructionComponents.push(WelcomeParticipant);
    InstructionComponents.push(key_resp_2);
    
    for (const thisComponent of InstructionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function InstructionRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Instruction' ---
    // get current time
    t = InstructionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *WelcomeParticipant* updates
    if (t >= 0.0 && WelcomeParticipant.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      WelcomeParticipant.tStart = t;  // (not accounting for frame time here)
      WelcomeParticipant.frameNStart = frameN;  // exact frame index
      
      WelcomeParticipant.setAutoDraw(true);
    }
    
    
    // *key_resp_2* updates
    if (t >= 0.0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }
    
    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        key_resp_2.duration = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of InstructionComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function InstructionRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Instruction' ---
    for (const thisComponent of InstructionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Instruction.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_2.corr, level);
    }
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        psychoJS.experiment.addData('key_resp_2.duration', key_resp_2.duration);
        routineTimer.reset();
        }
    
    key_resp_2.stop();
    // the Routine "Instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var CharactersMaxDurationReached;
var _key_resp_3_allKeys;
var CharactersMaxDuration;
var CharactersComponents;
function CharactersRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Characters' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    CharactersClock.reset();
    routineTimer.reset();
    CharactersMaxDurationReached = false;
    // update component parameters for each repeat
    text_2.setText('Nous vous proposons maintenant de rencontrer chacun des personnages. \n');
    Character.setImage(FileName);
    key_resp_3.keys = undefined;
    key_resp_3.rt = undefined;
    _key_resp_3_allKeys = [];
    psychoJS.experiment.addData('Characters.started', globalClock.getTime());
    CharactersMaxDuration = null
    // keep track of which components have finished
    CharactersComponents = [];
    CharactersComponents.push(text_2);
    CharactersComponents.push(text_3);
    CharactersComponents.push(Character);
    CharactersComponents.push(key_resp_3);
    
    for (const thisComponent of CharactersComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function CharactersRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Characters' ---
    // get current time
    t = CharactersClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_2* updates
    if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }
    
    
    // *text_3* updates
    if (t >= 0.0 && text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_3.tStart = t;  // (not accounting for frame time here)
      text_3.frameNStart = frameN;  // exact frame index
      
      text_3.setAutoDraw(true);
    }
    
    
    // *Character* updates
    if (t >= 0.0 && Character.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Character.tStart = t;  // (not accounting for frame time here)
      Character.frameNStart = frameN;  // exact frame index
      
      Character.setAutoDraw(true);
    }
    
    
    // *key_resp_3* updates
    if (t >= 0.0 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_3.tStart = t;  // (not accounting for frame time here)
      key_resp_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.clearEvents(); });
    }
    
    if (key_resp_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_3.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_3_allKeys = _key_resp_3_allKeys.concat(theseKeys);
      if (_key_resp_3_allKeys.length > 0) {
        key_resp_3.keys = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_3.rt = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].rt;
        key_resp_3.duration = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of CharactersComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function CharactersRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Characters' ---
    for (const thisComponent of CharactersComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Characters.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_3.corr, level);
    }
    psychoJS.experiment.addData('key_resp_3.keys', key_resp_3.keys);
    if (typeof key_resp_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_3.rt', key_resp_3.rt);
        psychoJS.experiment.addData('key_resp_3.duration', key_resp_3.duration);
        routineTimer.reset();
        }
    
    key_resp_3.stop();
    // the Routine "Characters" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Instruction2MaxDurationReached;
var _key_resp_5_allKeys;
var Instruction2MaxDuration;
var Instruction2Components;
function Instruction2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Instruction2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    Instruction2Clock.reset();
    routineTimer.reset();
    Instruction2MaxDurationReached = false;
    // update component parameters for each repeat
    text_5.setText(Text);
    key_resp_5.keys = undefined;
    key_resp_5.rt = undefined;
    _key_resp_5_allKeys = [];
    text_6.setText('Appuyez sur la touche espace pour continuer.');
    psychoJS.experiment.addData('Instruction2.started', globalClock.getTime());
    Instruction2MaxDuration = null
    // keep track of which components have finished
    Instruction2Components = [];
    Instruction2Components.push(text_5);
    Instruction2Components.push(key_resp_5);
    Instruction2Components.push(text_6);
    
    for (const thisComponent of Instruction2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Instruction2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Instruction2' ---
    // get current time
    t = Instruction2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_5* updates
    if (t >= 0.0 && text_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_5.tStart = t;  // (not accounting for frame time here)
      text_5.frameNStart = frameN;  // exact frame index
      
      text_5.setAutoDraw(true);
    }
    
    
    // *key_resp_5* updates
    if (t >= 0.0 && key_resp_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_5.tStart = t;  // (not accounting for frame time here)
      key_resp_5.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_5.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.clearEvents(); });
    }
    
    if (key_resp_5.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_5.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_5_allKeys = _key_resp_5_allKeys.concat(theseKeys);
      if (_key_resp_5_allKeys.length > 0) {
        key_resp_5.keys = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].name;  // just the last key pressed
        key_resp_5.rt = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].rt;
        key_resp_5.duration = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_6* updates
    if (t >= 0.0 && text_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_6.tStart = t;  // (not accounting for frame time here)
      text_6.frameNStart = frameN;  // exact frame index
      
      text_6.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Instruction2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Instruction2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Instruction2' ---
    for (const thisComponent of Instruction2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Instruction2.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_5.corr, level);
    }
    psychoJS.experiment.addData('key_resp_5.keys', key_resp_5.keys);
    if (typeof key_resp_5.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_5.rt', key_resp_5.rt);
        psychoJS.experiment.addData('key_resp_5.duration', key_resp_5.duration);
        routineTimer.reset();
        }
    
    key_resp_5.stop();
    // the Routine "Instruction2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var PlayVideoMaxDurationReached;
var _key_resp_4_allKeys;
var t0;
var PlayVideoMaxDuration;
var PlayVideoComponents;
function PlayVideoRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'PlayVideo' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    PlayVideoClock.reset();
    routineTimer.reset();
    PlayVideoMaxDurationReached = false;
    // update component parameters for each repeat
    Clip.setMovie(ClipName);
    key_resp_4.keys = undefined;
    key_resp_4.rt = undefined;
    _key_resp_4_allKeys = [];
    // Run 'Begin Routine' code from CollectDataVideo
    t0 = globalClock.getTime();
    psychoJS.experiment.addData("t0", t0);
    psychoJS.experiment.addData("ClipName", ClipName);
    
    psychoJS.experiment.addData('PlayVideo.started', globalClock.getTime());
    PlayVideoMaxDuration = null
    // keep track of which components have finished
    PlayVideoComponents = [];
    PlayVideoComponents.push(Clip);
    PlayVideoComponents.push(key_resp_4);
    
    for (const thisComponent of PlayVideoComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function PlayVideoRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'PlayVideo' ---
    // get current time
    t = PlayVideoClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Clip* updates
    if (t >= 0 && Clip.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Clip.tStart = t;  // (not accounting for frame time here)
      Clip.frameNStart = frameN;  // exact frame index
      
      Clip.setAutoDraw(true);
      Clip.play();
    }
    
    if (Clip.status === PsychoJS.Status.FINISHED) {  // force-end the Routine
        continueRoutine = false;
    }
    
    // *key_resp_4* updates
    if (t >= 0 && key_resp_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_4.tStart = t;  // (not accounting for frame time here)
      key_resp_4.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_4.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.clearEvents(); });
    }
    
    if (key_resp_4.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_4.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_4_allKeys = _key_resp_4_allKeys.concat(theseKeys);
      if (_key_resp_4_allKeys.length > 0) {
        key_resp_4.keys = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].name;  // just the last key pressed
        key_resp_4.rt = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].rt;
        key_resp_4.duration = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of PlayVideoComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var t1;
function PlayVideoRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'PlayVideo' ---
    for (const thisComponent of PlayVideoComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('PlayVideo.stopped', globalClock.getTime());
    Clip.stop();  // ensure movie has stopped at end of Routine
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_4.corr, level);
    }
    psychoJS.experiment.addData('key_resp_4.keys', key_resp_4.keys);
    if (typeof key_resp_4.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_4.rt', key_resp_4.rt);
        psychoJS.experiment.addData('key_resp_4.duration', key_resp_4.duration);
        routineTimer.reset();
        }
    
    key_resp_4.stop();
    // Run 'End Routine' code from CollectDataVideo
    t1 = globalClock.getTime();
    psychoJS.experiment.addData("t1", t1);
    
    // the Routine "PlayVideo" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var AskQuestionMaxDurationReached;
var t2;
var AskQuestionMaxDuration;
var AskQuestionComponents;
function AskQuestionRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'AskQuestion' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    AskQuestionClock.reset();
    routineTimer.reset();
    AskQuestionMaxDurationReached = false;
    // update component parameters for each repeat
    Questions.setText(Question);
    Answer_A.setText(Answer_1);
    Answer_B.setText(Answer_2);
    Answer_C.setText(Answer_3);
    Answer_D.setText(Answer_4);
    slider_2.reset()
    // Run 'Begin Routine' code from SliderStuff
    psychoJS.eventManager.clearEvents();
    
    // Run 'Begin Routine' code from QuestionDataCollectTime
    t2 = globalClock.getTime();
    psychoJS.experiment.addData("t2", t2);
    
    psychoJS.experiment.addData('AskQuestion.started', globalClock.getTime());
    AskQuestionMaxDuration = null
    // keep track of which components have finished
    AskQuestionComponents = [];
    AskQuestionComponents.push(Questions);
    AskQuestionComponents.push(Answer_A);
    AskQuestionComponents.push(Answer_B);
    AskQuestionComponents.push(Answer_C);
    AskQuestionComponents.push(Answer_D);
    AskQuestionComponents.push(slider_2);
    AskQuestionComponents.push(InstructionSlider);
    
    for (const thisComponent of AskQuestionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function AskQuestionRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'AskQuestion' ---
    // get current time
    t = AskQuestionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Questions* updates
    if (t >= 0.0 && Questions.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Questions.tStart = t;  // (not accounting for frame time here)
      Questions.frameNStart = frameN;  // exact frame index
      
      Questions.setAutoDraw(true);
    }
    
    
    // *Answer_A* updates
    if (t >= 0.0 && Answer_A.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Answer_A.tStart = t;  // (not accounting for frame time here)
      Answer_A.frameNStart = frameN;  // exact frame index
      
      Answer_A.setAutoDraw(true);
    }
    
    
    // *Answer_B* updates
    if (t >= 0.0 && Answer_B.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Answer_B.tStart = t;  // (not accounting for frame time here)
      Answer_B.frameNStart = frameN;  // exact frame index
      
      Answer_B.setAutoDraw(true);
    }
    
    
    // *Answer_C* updates
    if (t >= 0.0 && Answer_C.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Answer_C.tStart = t;  // (not accounting for frame time here)
      Answer_C.frameNStart = frameN;  // exact frame index
      
      Answer_C.setAutoDraw(true);
    }
    
    
    // *Answer_D* updates
    if (t >= 0.0 && Answer_D.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Answer_D.tStart = t;  // (not accounting for frame time here)
      Answer_D.frameNStart = frameN;  // exact frame index
      
      Answer_D.setAutoDraw(true);
    }
    
    
    // *slider_2* updates
    if (t >= 0.0 && slider_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider_2.tStart = t;  // (not accounting for frame time here)
      slider_2.frameNStart = frameN;  // exact frame index
      
      slider_2.setAutoDraw(true);
    }
    
    
    // Check slider_2 for response to end Routine
    if (slider_2.getRating() !== undefined && slider_2.status === PsychoJS.Status.STARTED) {
      continueRoutine = false; }
    // Run 'Each Frame' code from SliderStuff
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    keys = psychoJS.eventManager.getKeys(["left", "right", "return"]);
    if ((_pj.in_es6("left", keys) && (slider_2.markerPos > slider_2.ticks[0]))) {
        slider_2.markerPos -= 1;
    } else {
        if ((_pj.in_es6("right", keys) && (slider_2.markerPos < slider_2.ticks.slice((- 1))[0]))) {
            slider_2.markerPos += 1;
        } else {
            if (_pj.in_es6("return", keys)) {
                continueRoutine = false;
            }
        }
    }
    
    
    // *InstructionSlider* updates
    if (t >= 0.0 && InstructionSlider.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      InstructionSlider.tStart = t;  // (not accounting for frame time here)
      InstructionSlider.frameNStart = frameN;  // exact frame index
      
      InstructionSlider.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of AskQuestionComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var chosen_answer;
function AskQuestionRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'AskQuestion' ---
    for (const thisComponent of AskQuestionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('AskQuestion.stopped', globalClock.getTime());
    psychoJS.experiment.addData('slider_2.response', slider_2.getRating());
    psychoJS.experiment.addData('slider_2.rt', slider_2.getRT());
    // Run 'End Routine' code from SliderStuff
    slider_position = slider_2.markerPos;
    if ((slider_position === 1)) {
        chosen_answer = Answer_1;
    } else {
        if ((slider_position === 2)) {
            chosen_answer = Answer_2;
        } else {
            if ((slider_position === 3)) {
                chosen_answer = Answer_3;
            } else {
                if ((slider_position === 4)) {
                    chosen_answer = Answer_4;
                } else {
                    chosen_answer = "No selection";
                }
            }
        }
    }
    console.log(`Slider Position: ${slider_position}, Chosen Answer: ${chosen_answer}`);
    psychoJS.experiment.addData("ChosenAnswer", chosen_answer);
    if ((chosen_answer === Target)) {
        psychoJS.experiment.addData("Correct", 1);
        psychoJS.experiment.addData("Score", 1);
    } else {
        psychoJS.experiment.addData("Correct", 0);
        psychoJS.experiment.addData("Score", (- 1));
    }
    
    // Run 'End Routine' code from QuestionDataCollectTime
    if ((slider_2.getRating() === null)) {
        psychoJS.experiment.addData("slider_2.response", "No Response");
        psychoJS.experiment.addData("slider_2.rt", "No Response");
    } else {
        psychoJS.experiment.addData("slider_2.response", slider_2.getRating());
        psychoJS.experiment.addData("slider_2.rt", slider_2.getRT());
    }
    
    // the Routine "AskQuestion" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var ConfidenceSliderMaxDurationReached;
var t_confidence_start;
var t4;
var ConfidenceSliderMaxDuration;
var ConfidenceSliderComponents;
function ConfidenceSliderRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'ConfidenceSlider' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    ConfidenceSliderClock.reset();
    routineTimer.reset();
    ConfidenceSliderMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from Confidence_Slider_Controller
    confidence_slider.reset();
    confidence_slider.markerPos = 5;
    t_confidence_start = globalClock.getTime();
    console.log(`Begin Routine: Confidence slider initialized with markerPos=${confidence_slider.markerPos}`);
    
    confidence_slider.reset()
    // Run 'Begin Routine' code from LogConfidenceData
    t4 = globalClock.getTime();
    psychoJS.experiment.addData("t4", t4);
    
    psychoJS.experiment.addData('ConfidenceSlider.started', globalClock.getTime());
    ConfidenceSliderMaxDuration = null
    // keep track of which components have finished
    ConfidenceSliderComponents = [];
    ConfidenceSliderComponents.push(confidence_slider);
    ConfidenceSliderComponents.push(text_4);
    ConfidenceSliderComponents.push(text_8);
    
    for (const thisComponent of ConfidenceSliderComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function ConfidenceSliderRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'ConfidenceSlider' ---
    // get current time
    t = ConfidenceSliderClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from Confidence_Slider_Controller
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    keys = psychoJS.eventManager.getKeys(["left", "right", "return"]);
    if ((_pj.in_es6("left", keys) && (confidence_slider.markerPos > confidence_slider.ticks[0]))) {
        confidence_slider.markerPos -= 1;
        console.log(`Each Frame: Marker moved left to ${confidence_slider.markerPos}`);
    } else {
        if ((_pj.in_es6("right", keys) && (confidence_slider.markerPos < confidence_slider.ticks.slice((- 1))[0]))) {
            confidence_slider.markerPos += 1;
            console.log(`Each Frame: Marker moved right to ${confidence_slider.markerPos}`);
        } else {
            if (_pj.in_es6("return", keys)) {
                console.log(`Each Frame: 'Return' pressed. Final position: ${confidence_slider.markerPos}`);
                continueRoutine = false;
            }
        }
    }
    
    
    // *confidence_slider* updates
    if (t >= 0.0 && confidence_slider.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      confidence_slider.tStart = t;  // (not accounting for frame time here)
      confidence_slider.frameNStart = frameN;  // exact frame index
      
      confidence_slider.setAutoDraw(true);
    }
    
    
    // *text_4* updates
    if (t >= 0.0 && text_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_4.tStart = t;  // (not accounting for frame time here)
      text_4.frameNStart = frameN;  // exact frame index
      
      text_4.setAutoDraw(true);
    }
    
    
    // *text_8* updates
    if (t >= 0.0 && text_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_8.tStart = t;  // (not accounting for frame time here)
      text_8.frameNStart = frameN;  // exact frame index
      
      text_8.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ConfidenceSliderComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var confidence_position;
var t_confidence_end;
var confidence_rt;
function ConfidenceSliderRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'ConfidenceSlider' ---
    for (const thisComponent of ConfidenceSliderComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('ConfidenceSlider.stopped', globalClock.getTime());
    // Run 'End Routine' code from Confidence_Slider_Controller
    confidence_position = confidence_slider.markerPos;
    if ((confidence_position !== null)) {
        t_confidence_end = globalClock.getTime();
        confidence_rt = (t_confidence_end - t_confidence_start);
        console.log(`End Routine: Confidence position=${confidence_position}, RT=${confidence_rt}`);
        psychoJS.experiment.addData("ConfidencePosition", confidence_position);
        psychoJS.experiment.addData("ConfidenceRT", confidence_rt);
    } else {
        console.log("No confidence rating recorded.");
        psychoJS.experiment.addData("ConfidencePosition", "No selection");
        psychoJS.experiment.addData("ConfidenceRT", "No response");
    }
    
    psychoJS.experiment.addData('confidence_slider.response', confidence_slider.getRating());
    psychoJS.experiment.addData('confidence_slider.rt', confidence_slider.getRT());
    // Run 'End Routine' code from LogConfidenceData
    /*
    # Ensure confidence slider has a valid response
    if confidence_slider.getRating() is None:
    print("No response recorded for confidence_slider")
    thisExp.addData('confidence_slider.response', 'No Response')
    thisExp.addData('confidence_slider.rt', 'No Response')
    else:
    # Get confidence slider response and reaction time
    confidence_position = confidence_slider.getRating()
    confidence_rt = confidence_slider.getRT()
    
    # Log confidence-related data
    thisExp.addData('confidence_slider.response', confidence_position)
    thisExp.addData('confidence_slider.rt', confidence_rt)
    
    # Debugging logs
    print(f"Confidence Slider response: {confidence_slider.getRating()}")
    print(f"Confidence Slider RT: {confidence_slider.getRT()}")*/
    
    // the Routine "ConfidenceSlider" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var ThankYouMaxDurationReached;
var ThankYouMaxDuration;
var ThankYouComponents;
function ThankYouRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'ThankYou' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    ThankYouClock.reset(routineTimer.getTime());
    routineTimer.add(15.000000);
    ThankYouMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('ThankYou.started', globalClock.getTime());
    ThankYouMaxDuration = null
    // keep track of which components have finished
    ThankYouComponents = [];
    ThankYouComponents.push(Thanks);
    
    for (const thisComponent of ThankYouComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function ThankYouRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'ThankYou' ---
    // get current time
    t = ThankYouClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Thanks* updates
    if (t >= 0.0 && Thanks.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Thanks.tStart = t;  // (not accounting for frame time here)
      Thanks.frameNStart = frameN;  // exact frame index
      
      Thanks.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 15 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (Thanks.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Thanks.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ThankYouComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ThankYouRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'ThankYou' ---
    for (const thisComponent of ThankYouComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('ThankYou.stopped', globalClock.getTime());
    if (ThankYouMaxDurationReached) {
        ThankYouClock.add(ThankYouMaxDuration);
    } else {
        ThankYouClock.add(15.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
