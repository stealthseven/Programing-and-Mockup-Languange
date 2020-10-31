// Button without toggle
// const button = document.getElementById('ubahWarna');
// const container = document.getElementsByClassName('container')[0];
// const h1 = document.getElementsByTagName('h1')[0];
// button.addEventListener('click', function () {
//     container.style.backgroundColor = 'blue';
//     h1.style.color = 'lightblue';
//     document.body.style.backgroundColor = 'aqua';

// })

// Button with toggle
const button = document.getElementById('ubahWarna');
const container = document.getElementsByClassName('container')[0];
const h1 = document.getElementsByTagName('h1')[0];
button.addEventListener('click', function () {
    container.classList.toggle('colorChange1');
    h1.classList.toggle('colorChange2');
    document.body.classList.toggle('colorChange3');
});

// Random Color
const newButton = document.createElement('button');
const newText = document.createTextNode('Random');
newButton.appendChild(newText);
newButton.setAttribute('type', 'button');
const buttonX = document.getElementById('ubahWarna');
buttonX.after(newButton);

newButton.addEventListener('click', function () {
    const r = Math.round(Math.random() * 255 + 1);
    const g = Math.round(Math.random() * 255 + 1);
    const b = Math.round(Math.random() * 255 + 1);
    document.body.style.backgroundColor = 'rgb(' + r + ',' + g + ',' + b + ')';
});

// Range
const slideR = document.querySelector('input[name=red]')
const slideG = document.querySelector('input[name=green]')
const slideB = document.querySelector('input[name=blue]')

slideR.addEventListener('input', function () {
    const r = slideR.value;
    const g = slideG.value;
    const b = slideB.value;
    document.body.style.backgroundColor = 'rgb(' + r + ',' + g + ',' + b + ')';
});

slideG.addEventListener('input', function () {
    const r = slideR.value;
    const g = slideG.value;
    const b = slideB.value;
    document.body.style.backgroundColor = 'rgb(' + r + ',' + g + ',' + b + ')';
});

slideB.addEventListener('input', function () {
    const r = slideR.value;
    const g = slideG.value;
    const b = slideB.value;
    document.body.style.backgroundColor = 'rgb(' + r + ',' + g + ',' + b + ')';
});