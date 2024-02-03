
const image_panel = document.getElementById('image-panel')
const x_label = document.getElementById('x-label')

document.addEventListener('')
image_panel.addEventListener('click', (event) => {
    alert('dsad')
    const boundingBox = image.getBoundingClientRect();
    const x = event.clientX - boundingBox.left
    x_label.innerHTML = x
});