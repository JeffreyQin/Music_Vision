const labelPanel = document.getElementById('label-panel');
const imagePanel = document.getElementById('image-panel');
const image = document.getElementById('image');

const addButton = document.getElementById('add-button');
const finishButton = document.getElementById('finish-button');

let chordPanel;
let Xlabel, durationLabel, pitchLabel;
let duration, pitch;
var chordIdx = 0
var chordX = -1
var inputList = []

document.addEventListener('DOMContentLoaded', () => {
    chordIdx = 0
    constructInputPanel();
});

image.addEventListener('click', (event) => {
    const boundingBox = image.getBoundingClientRect();
    chordX = event.clientX - boundingBox.left
    Xlabel.innerHTML = `chord ${chordIdx} x: ${chordX}`;

    let lineExist = document.querySelector('.label-line');
    if (lineExist) {
        lineExist.remove();
    }

    let labelLine = document.createElement('div');
    labelLine.className = '.label-line';
    labelLine.style.left = chordX + 'px';

    imagePanel.appendChild(labelLine);
})

addButton.addEventListener('click', () => {
    if (!checkInput()) {
        alert('Please fill in all required fields.')
    } else {
        takeInput();
        constructInputPanel();
    }
});

finishButton.addEventListener('click', () => {
    if (!checkInput()) {
        alert('Please fill in all required fields.')
    } else {
        confirmation = confirm('Please confirm to proceed. You cannot come back.')
        if (confirmation) {
            takeInput();
            location.reload();
        }
    }
});

function constructInputPanel() {
    chordIdx ++;
    chordX = -1;
    chordPanel = document.createElement('div');
    Xlabel = document.createElement('p');
    Xlabel.innerHTML = `chord ${chordIdx} X: `;
    chordPanel.appendChild(Xlabel);
    durationLabel = document.createElement('label');
    durationLabel.innerHTML = `chord ${chordIdx} duration: `;
    chordPanel.appendChild(durationLabel);
    duration = document.createElement('input');
    chordPanel.appendChild(duration);
    chordPanel.appendChild(document.createElement('p'));
    pitchLabel = document.createElement('label');
    pitchLabel.innerHTML = `chord ${chordIdx} pitch: `;
    chordPanel.appendChild(pitchLabel);
    pitch = [];
    for (let i = 0; i < 5; i++) {
        pitch.push(document.createElement('input'));
        pitch[i].className = 'pitch-input';
        chordPanel.appendChild(pitch[i]);
    }
    chordPanel.appendChild(document.createElement('p'));
    labelPanel.appendChild(chordPanel);
}

function takeInput() {
    inputList.push({
        index: chordIdx - 1,
        x: chordX,
        duration: duration.value,
        pitch0: pitch[0].value,
        pitch1: pitch[1].value,
        pitch2: pitch[2].value,
        pitch3: pitch[3].value,
        pitch4: pitch[4].value
    });
};

function checkInput() {
    let lineExist = document.querySelector('.label-line');
    if (!lineExist) {
        return false;
    }
    if (duration.value == "") {
        return false;
    }
    for (let i = 0; i < 5; i++) {
        if (pitch[i].value == "") {
            return false
        }
    }
    return true;
}