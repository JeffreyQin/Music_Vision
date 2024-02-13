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
    loadImage();
    constructInputPanel();
});

image.addEventListener('click', (event) => {
    const boundingBox = image.getBoundingClientRect();
    chordX = event.clientX - boundingBox.left
    Xlabel.innerHTML = `chord ${chordIdx} X: ${chordX}`;

    let lineExist = document.querySelector('.label-line');
    if (lineExist) {
        lineExist.remove();
    }

    let labelLine = document.createElement('div');
    labelLine.className = 'label-line';
    labelLine.style.left = chordX + 'px';

    imagePanel.appendChild(labelLine);
})

addButton.addEventListener('click', () => {
    if (!checkInput()) {
        alert('Please fill in all required fields.')
    } else {
        let lineExist = document.querySelector('.label-line');
        lineExist.remove();
        takeInput();
        constructInputPanel();
    }
});

finishButton.addEventListener('click', () => {
    if (!checkInput()) {
        alert('Please fill in all required fields.')
    } else {
        let confirmation = confirm('Please confirm to proceed. You cannot come back.');
        if (confirmation) {
            alert('das')
            takeInput();
            generateLabel();
        }
    }
});

async function generateLabel() {
    alert('dsadas')
    fetch('http://localhost:1109/generateLabel', {
        method: "POST",
        headers: {
            "Content-Type": "application/json; charset=utf-8"
        },
        body: JSON.stringify({
            image: image.src,
            labels: inputList
        })
    }).then(() => {

    });
}

function loadImage() {
    fetch('http://localhost:1109/getImage')
        .then(result => result.json())
        .then(result => {
            const img_file = result['img_file'];
            image.src = img_file;
        })
}

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
    duration.disabled = true;
    for (let i = 0; i < 5; i++) {
        pitch[i].disabled = true;
    }
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