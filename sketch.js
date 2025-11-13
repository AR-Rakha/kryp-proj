

let kryptList = "abcdefghijklmnopqrstuvxyzæøå";
let current;
let phase = 0;       // 0 = show start, 1 = scramble, 2 = decrypt
let lockIndex = 0;   // used in decrypt phase
let timer = 0;

function setup() {
  createCanvas(500, 200);
  textAlign(CENTER, CENTER);
  textSize(64);

  // start with startText
	
  current = startText.split("");
}

function draw() {
  background(255);

  if (phase === 0) {
    // hold startText for a moment
    if (frameCount > 60) { // wait ~1 sec
      if (endText!="") { // wait ~1 sec
				phase = 1;
			}else{
				frameCount=0;
			}
    }
  } 
  else if (phase === 1) {
    // scrambling phase
    for (let i = 0; i < current.length; i++) {
      current[i] = kryptList[floor(random(kryptList.length))];
    }

    timer++;
    if (timer > 30) { // after ~1 sec, switch to decrypt
      timer = 0;
      phase = 2;
      lockIndex = 0;
    }
  } 
  else if (phase === 2) {
    // decrypt into endText
    let i = lockIndex;
    while (i < endText.length) {
      current[i] = kryptList[floor(random(kryptList.length)-1)];
      i++;
    }

    if (frameCount % 50 === 0 && lockIndex < endText.length) {
      current[lockIndex] = endText[lockIndex];
      lockIndex++;
    }
  }

  text(current.join(""), width / 2, height / 2);
}
