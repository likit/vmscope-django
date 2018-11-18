'use strict';

const ARROW_KEY_LEFT = 37;
const ARROW_KEY_UP = 38;
const ARROW_KEY_RIGHT = 39;
const ARROW_KEY_DOWN = 40;
const Z = 90;

var viewModel = function() {
  var self = this;
  self.lastFoundEggInfoId = ko.observable(0);
  self.foundEggs = ko.observableArray([]);
  self.numEggs = ko.observable(35);
  self.isZoomed = ko.observable(false);
  self.numEggsFound = ko.computed(function() {
    return ko.utils.arrayFilter(self.foundEggs(), function(item) {
      return item.objType == 'egg';
    });
  });
  self.numArtifactsFound = ko.computed(function() {
    return ko.utils.arrayFilter(self.foundEggs(), function(item) {
      return item.objType == 'artifact';
    });
  });
}

var imageClickHandler = function(event) {
  // pass
}

var vm = new viewModel();
ko.applyBindings(vm);

var unzoomedPositions = [];
var centerX = 360;
var centerY = 305;
var originX = 360;
var originY = 305;
var centerXZoom = 360;
var centerYZoom = 305;
var slideWidth = 1800;
var slideLength = 4600;
var elaptime = 0;
var eggs = [];
var dusts = [];
var artifacts = [];
var stageTemp = [];
var numBact = 500;
var eggInfoId = [1,1,1,1,5,3,3,3,3,7,7,7,7,4,4,4,6,6,6,6];
var eggList = [];
var bubbles = [];
var bgDebris = [];
var droplets = [];
var eggLikes = [];
var debris = [];
var floatingDebris = [];


var stage,
    centerHashMark,
    upperHashMark, // do need?
    leftHashMark,
    rightHashMark,
    lowerHashMark, // do need?
    coordTextX,
    coordTextY,
    timeText,
    queue;

var arrow_key_handler = function(e) {
  switch(e.keyCode) {
    case 37: case 39: case 38:
    case 40: e.preventDefault(); break;
    default: break;
  }
}

var disableScrolling = function() {
  window.addEventListener("keydown", arrow_key_handler, false);
}

var enableScrolling = function() {
  window.removeEventListener("keydown", arrow_key_handler, false);
}

function onDPad(e) {
    switch(e.keyCode) {
        case ARROW_KEY_LEFT:
            moveEgg('left', 10);
            break;
        case ARROW_KEY_RIGHT:
            moveEgg('right', 10);
            break;
        case ARROW_KEY_UP:
            moveEgg('up', 10);
            break;
        case ARROW_KEY_DOWN:
            moveEgg('down', 10);
            break;
        case Z:
            zoom();
            break;
    }
}

function preload() {
    queue = new createjs.LoadQueue();
    queue.addEventListener("complete", draw);
    var items = [];

    $.when($.getJSON('/api/microscope/1').then(function(data) {
        $.each(data['parasites'], function(idx,d) {
            console.log(d)
            items.push({
                id: d['pk'],
                src: d['item']['image']
            });
            eggList.push(d['pk']);
        });
        queue.loadManifest(items);
        console.log(items, eggList);
        })
    );
}

function run() {
    disableScrolling(); // turn off default key events
    window.onkeydown = onDPad;

    var c = document.getElementById('canvas');
    var ctx = c.getContext('2d');
    ctx.beginPath();
    ctx.arc(350,330,320,0,2*Math.PI);
    ctx.stroke();
    ctx.clip();
    stage = new createjs.Stage('canvas');
    preload();
}

function draw() {
    coordTextX = new createjs.Text('X='+centerX.toString(), '20px Arial', '#017c1e');
    coordTextX.x = 280;
    coordTextX.y = 600;
    coordTextY = new createjs.Text('Y='+centerY.toString(), '20px Arial', '#017c1e');
    coordTextY.x = 360;
    coordTextY.y = 600;
    timeText = new createjs.Text('Time=0 sec', '20px Arial', '#017c1e');
    timeText.x = 300;
    timeText.y = 570;
    var circle = new createjs.Shape();
    centerHashMark = new createjs.Shape();
    leftHashMark = new createjs.Shape();
    rightHashMark = new createjs.Shape();
    upperHashMark = new createjs.Shape();
    lowerHashMark = new createjs.Shape();

    centerHashMark.graphics.beginStroke('#000');
    centerHashMark.graphics.drawRect(360,305,0,50);
    centerHashMark.graphics.endStroke();
    centerHashMark.alpha = 0.5;
    
    leftHashMark.graphics.beginStroke('#000');
    leftHashMark.graphics.drawRect(50,305,0,50);
    leftHashMark.graphics.endStroke();
    leftHashMark.alpha = 0.5;

    rightHashMark.graphics.beginStroke('#000');
    rightHashMark.graphics.drawRect(650,305,0,50);
    rightHashMark.graphics.endStroke();
    rightHashMark.alpha = 0.5;
    
    lowerHashMark.graphics.beginStroke('#000');
    lowerHashMark.graphics.drawRect(330,630,50,0);
    lowerHashMark.graphics.endStroke();
    lowerHashMark.alpha = 0.2;
    
    upperHashMark.graphics.beginStroke('#000');
    upperHashMark.graphics.drawRect(330,30,50,0);
    upperHashMark.graphics.endStroke();
    upperHashMark.alpha = 0.2;

    circle.graphics.setStrokeStyle(6);
    circle.graphics.beginStroke('#ffffff');
    circle.graphics.beginFill(createjs.Graphics.getRGB(220, 220, 188, 1));
    circle.graphics.drawCircle(350, 330, 320);
    circle.graphics.endStroke();
    stage.addChild(circle);
    for (var i = 0; i < vm.numEggs(); i++) {
        var eggIndex = Math.floor(Math.random() * eggList.length);
        var egg = new createjs.Bitmap(queue.getResult(eggList[eggIndex]));
        egg.x = Math.random() * slideLength;
        egg.y = Math.random() * slideWidth;
        egg.identifier = egg.x.toString() + '-' + egg.y.toString();
        while (egg.x < 200 || egg.y < 200) {
            egg.x = Math.random() * slideLength;
            egg.y = Math.random() * slideWidth;
        } 
        // egg.scaleX = 0.3;
        // egg.scaleY = 0.3;
        egg.scaleX = 0.3 * 1/2.1;
        egg.scaleY = 0.3 * 1/2.1;
        //egg.alpha = 0.75;
        egg.eggType = eggList[eggIndex];
        egg.addEventListener('click', function(e) { imageClickHandler(e); });
        egg.rotation = Math.random() * 360;
        egg.objType = 'egg';
        egg.infoId = eggInfoId[eggIndex];
        eggs.push(egg);
    }
    for (var i = 0; i < 50; i++) {
        var idx = Math.floor(Math.random() * eggList.length);
        var item = new createjs.Bitmap(queue.getResult(eggLikes[idx]));
        item.x = Math.random() * slideLength;
        item.y = Math.random() * slideWidth;
        //egg.alpha = 0.75;
        item.scaleX = 0.5;
        item.scaleY = 0.5;
        item.addEventListener('click', function(e) { imageClickHandler(e); });
        item.rotation = Math.random() * 360;
        item.objType = 'artifact';
        item.identifier = item.x.toString() + '-' + item.y.toString();
        artifacts.push(item);
    }

    for (var i = 0; i < 500; i++) {
        var idx = Math.floor(Math.random() * bgDebris.length);
        d = new createjs.Bitmap(queue.getResult(bgDebris[idx]));
        d.x = Math.random() * slideLength;
        d.y = Math.random() * slideWidth;
        while (d.x < 100 || d.y < 100) {
            d.x = Math.random() * slideLength;
            d.y = Math.random() * slideWidth;
        } 
        d.oriX = d.x;
        d.oriY = d.y;
        d.scaleX = d.scaleY = Math.random() + 0.2;
        d.scaleX = d.scaleY *= 1/2.3;
        d.rotation = Math.random() * 360;
        d.objType = 'artifact';
        artifacts.push(d);
    }
    var stageBubbles = [];
    for (var i = 0; i < 300; i++) {
        var idx = Math.floor(Math.random() * bubbles.length);
        d = new createjs.Bitmap(queue.getResult(bubbles[idx]));
        d.x = Math.random() * slideLength;
        d.y = Math.random() * slideWidth;
        // d.scaleX = d.scaleY = Math.random();
        d.scaleX = d.scaleY *= 1/2.3;
        d.rotation = Math.random() * 360;
        d.objType = 'artifact';
        stageBubbles.push(d);
    }
    for (var i = 0; i < 500; i++) {
        var idx = Math.floor(Math.random() * droplets.length);
        d = new createjs.Bitmap(queue.getResult(droplets[idx]));
        d.alpha = Math.random();
        if(d.alpha<0.7) {
          d.alpha += 0.3;
        }
        d.x = Math.random() * slideLength;
        d.y = Math.random() * slideWidth;
        d.scaleX = d.scaleY = Math.random() * 1.5;
        d.scaleX = d.scaleY *= 1/2.3;
        d.rotation = Math.random() * 360;
        d.objType = 'artifact';
        artifacts.push(d);
    }
    for (var i = 0; i < 300; i++) {
        var idx = Math.floor(Math.random() * debris.length);
        d = new createjs.Bitmap(queue.getResult(debris[idx]));
        // d.alpha = Math.random();
        d.x = Math.random() * slideLength;
        d.y = Math.random() * slideWidth;
        while (d.x < 100 || d.y < 100) {
            d.x = Math.random() * slideLength;
            d.y = Math.random() * slideWidth;
        } 
        d.oriX = d.x;
        d.oriY = d.y;
        d.scaleX = d.scaleY = Math.random() + 0.2;
        d.scaleX = d.scaleY *= 1/2.3;
        d.rotation = Math.random() * 360;
        d.objType = 'artifact';
        artifacts.push(d);
    }
    for (var i=0; i < numBact; i++) {
        var bacts = ['bact1', 'bact2', 'bact3', 'bact4'];
        var idx = Math.floor(Math.random() * bacts.length);
        var d = new createjs.Bitmap(queue.getResult(bacts[idx]));
        d.scaleX = 0.25;
        d.scaleY = 0.25;
        d.scaleX = d.scaleY *= 1/2.3;
        d.alpha = Math.random();
        d.rotation = Math.random() * 360;
        d.x = Math.random() * 700;
        d.y = Math.random() * 700;
        dusts.push(d);
    }
    for (var i=0; i < 30; i++) {
        var bacts = ['bact5', 'bact6'];
        var idx = Math.floor(Math.random() * bacts.length);
        var d = new createjs.Bitmap(queue.getResult(bacts[idx]));
        d.scaleX = d.scaleY = Math.random() * 1.3;
        d.scaleX = d.scaleY *= 1/2.3;
        d.alpha = Math.random();
        d.rotation = Math.random() * 360;
        d.x = Math.random() * 700;
        d.y = Math.random() * 700;
        dusts.push(d);
    }
    for (var i=0; i<dusts.length; i++) {
        stage.addChild(dusts[i]);
    }
    var tempItem;
    for (var i=0; i<eggs.length; i++) {
        stageTemp.push(eggs[i]);
    }
    for (var i=0; i<artifacts.length; i++) {
        stageTemp.push(artifacts[i]);
    }
    for (var i=0; i<100; i++) {
        var idx = Math.floor(Math.random() * stageTemp.length);
        if (idx + 5 < stageTemp.length) {
            tempItem = stageTemp[idx + 5];
            stageTemp[idx + 5] = stageTemp[idx];
            stageTemp[idx] = tempItem;
        }
    }
    // floating debris on the topmost layer
    for (var i = 0; i < 50; i++) {
        var idx = Math.floor(Math.random() * floatingDebris.length);
        d = new createjs.Bitmap(queue.getResult(floatingDebris[idx]));
        d.x = Math.random() * slideLength;
        d.y = Math.random() * slideWidth;
        d.scaleX = d.scaleY = Math.random() + 0.2;
        d.scaleX = d.scaleY *= 1/2.3;
        d.rotation = Math.random() * 360;
        d.objType = 'artifact';
        stageTemp.push(d);
    }
    for (var i=0; i<stageTemp.length; i++) {
        stage.addChild(stageTemp[i]);
    }
    stage.addChild(centerHashMark, leftHashMark, rightHashMark,
                    upperHashMark, lowerHashMark);
    stage.addChild(coordTextX, coordTextY, timeText);
    for(var idx=0; idx < stageBubbles.lenght; idx++) {
        stage.addChild(stageBubbles[idx]);
    }
    stage.update();
    // set tick here so it starts after preload is complete.
    createjs.Ticker.addEventListener("tick", tick);
    createjs.Ticker.setFPS(30);
}

function zoom() {
  if(vm.isZoomed()===true) {
    zoomOut();
  } else {
    zoomIn();
  }
}

function zoomIn() {
  vm.isZoomed(true);
  unzoomedPositions = [];
  var p;
  centerXZoom = centerX;
  centerYZoom = centerY;
  for(var i=0; i<stageTemp.length; i++) {
      p = {x: stageTemp[i].x, y: stageTemp[i].y};
      unzoomedPositions.push(p);
      var deltaX = p.x - originX;
      var deltaY = p.y - originY;
      stageTemp[i].x = stageTemp[i].x + (deltaX * 1.2);
      stageTemp[i].y = stageTemp[i].y + (deltaY * 1.2);
      stageTemp[i].scaleX = stageTemp[i].scaleY *= 2.3;
  }
  for(var i=0; i<dusts.length; i++) {
      dusts[i].scaleX = dusts[i].scaleY *= 2.3;
  }
  stage.update();
}

function zoomOut() {
  vm.isZoomed(false);
  console.log('zooming out..');
  var deltaX = centerXZoom - centerX;
  var deltaY = centerYZoom - centerY;
  for(var i=0; i<stageTemp.length; i++) {
      stageTemp[i].scaleX = stageTemp[i].scaleY *= 1/2.3;
      stageTemp[i].y = unzoomedPositions[i].y - deltaY * 0.5;
      stageTemp[i].x = unzoomedPositions[i].x - deltaX * 0.5;
  }
  centerX = centerXZoom + deltaX * 0.5;
  centerY = centerYZoom + deltaY * 0.5;
  for(var i=0; i<dusts.length; i++) {
      dusts[i].scaleX = dusts[i].scaleY *= 1/2.3;
  }
  stage.update();
}

function moveEgg(direction, step) {
    createjs.Ticker.setPaused(true);
    switch(direction) {
        case 'left':
            if (centerX > 360) {
                centerX = centerX - step;
                centerXZoom = centerXZoom - step;
                coordTextX.text = 'X='+centerX.toString();
                for (var i=0; i<stageTemp.length; i++) {
                    stageTemp[i].x = stageTemp[i].x + step;
                    if(unzoomedPositions.length > 0) {
                      unzoomedPositions[i].x += step;
                    }
                }
                for (var i=0; i<dusts.length; i++) {
                    if (dusts[i].x > 650) {
                        dusts[i].x = 50;
                    } else {
                        dusts[i].x = dusts[i].x + step;
                    }
                }
            }
            break;
        case 'right':
            if(centerX < slideLength - 100) {
                centerX = centerX + step;
                centerXZoom = centerXZoom + step;
                coordTextX.text = 'X='+centerX.toString();
                for (var i=0; i<stageTemp.length; i++) {
                    stageTemp[i].x = stageTemp[i].x - step;
                    if(unzoomedPositions.length > 0) {
                    unzoomedPositions[i].x -= step;
                    }
                }
                for (var i=0; i<dusts.length; i++) {
                    if (dusts[i].x < 50) {
                        dusts[i].x = 650
                    }
                    dusts[i].x = dusts[i].x - step;
                }
            }
            break;
        case 'down':
            if(centerY < slideWidth - 100) {
                centerY = centerY + step;
                centerYZoom = centerYZoom + step;
                coordTextY.text = 'Y='+centerY.toString();
                for (var i=0; i<stageTemp.length; i++) {
                    stageTemp[i].y = stageTemp[i].y - step;
                    if(unzoomedPositions.length > 0) {
                    unzoomedPositions[i].y -= step;
                    }
                }
                for (var i=0; i<dusts.length; i++) {
                    if (dusts[i].y < step) {
                        dusts[i].y = 650
                    }
                    dusts[i].y = dusts[i].y - step;
                }
            }
            break;
        case 'up':
            if (centerY > 305) {
                centerY = centerY - step;
                centerYZoom = centerYZoom - step;
                coordTextY.text = 'Y='+centerY.toString();
                for (var i=0; i<stageTemp.length; i++) {
                    stageTemp[i].y = stageTemp[i].y + step;
                    if(unzoomedPositions.length > 0) {
                      unzoomedPositions[i].y += step;
                    }
                }
                for (var i=0; i<dusts.length; i++) {
                    if (dusts[i].y > 650) {
                        dusts[i].y = step
                    }
                    dusts[i].y = dusts[i].y + step;
                }
            }
            break;
    }
    createjs.Ticker.setPaused(false);
}

function oscillate() {
    var signs;
    if (elaptime > 3000) {
        signs = [-0.5, 0.5];
    } else if (elaptime > 2000) {
        signs = [-2, 2];
    } else if (elaptime > 1000) {
        signs = [-4, 2];
    } else {
        signs = [-8, 2];
    }
    elaptime = elaptime + 1;
    for (var i=0; i<dusts.length; i++) {
        dusts[i].x = dusts[i].x + (Math.random() * signs[Math.floor(Math.random() * 2)]);
        if (elaptime < 3000) {
            dusts[i].rotation = dusts[i].rotation - (Math.random() * 10);
            if (dusts[i].rotaion < 0) {
                dusts[i].rotaion = 360;
            }
        }
        if (dusts[i].x < 50) {
            dusts[i].x = 650;
        }
        dusts[i].y = dusts[i].y + (Math.random() * signs[Math.floor(Math.random() * 2)]);
        if (dusts[i].y < 10) {
            dusts[i].y = 650;
        }
    }
}

function tick() {
    oscillate();
    var et =  elaptime/30;
    timeText.text = 'Time='+et.toFixed(0)+' sec';
    stage.update();
}

run();