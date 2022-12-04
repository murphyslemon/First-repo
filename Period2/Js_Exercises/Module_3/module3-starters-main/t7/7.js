const trigger = document.getElementById('trigger');

function hover() {
    document.getElementById('target').src = 'img/picB.jpg';
}

function mouseOff() {
    document.getElementById('target').src = 'img/picA.jpg'
}

trigger.addEventListener('mouseover', hover);
trigger.addEventListener('mouseout', mouseOff);

