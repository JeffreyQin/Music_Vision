const imagePanel = document.getElementById('image-panel');
const Xlabel = document.getElementById('x-label');
const image = document.getElementById('image');
const finishButton = document.getElementById('finish-button')
const pitch1 = document.getElementById('pitch1-input')
const pitch2 = document.getElementById('pitch2-input')
const pitch3 = document.getElementById('pitch3-input')
const pitch4 = document.getElementById('pitch4-input')
const pitch5 = document.getElementById('pitch5-input')

var x = -1

const rawFolder = './music_score/raw_images/'
const labelledFolder = './music_sscore/labelled_images/'

document.addEventListener('DOMContentLoaded', () => {
    
})

image.addEventListener('click', (event) => {
    const boundingBox = image.getBoundingClientRect();
    x = event.clientX - boundingBox.left
    Xlabel.innerHTML = x

    const lineExist = document.querySelector('.label-line');
    if (lineExist) {
        lineExist.remove();
    }

    var labelLine = document.createElement('div');
    labelLine.className = 'label-line';
    labelLine.style.left = x + 'px';

    imagePanel.appendChild(labelLine)
});

finishButton.addEventListener('click', () => {
    confirmation = confirm('Confirm to proceed? You may not come back.')
    if (confirmation) {
        if (x == -1) {
            alert('No first no border found.')
        } else if (pitch1.value == '' || pitch2.value == '' || pitch3.value == '' || pitch4.value == '' || pitch5.value == '') {
            alert('Please fill in all required fields.')
        } else {
            processLabel()
            location.reload()
        }
    }
});