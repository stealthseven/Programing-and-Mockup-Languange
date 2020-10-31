// Event Handeler (on<action>)
const p2 = document.querySelector('.p2');

function ubahWarna() {
    p2.style.backgroundColor = 'gold';
}

p2.onclick = ubahWarna;

// addEventListener
const p4 = document.querySelector('section#b p');
p4.addEventListener('dblclick', function () {
    const liBaru = document.createElement('li');
    const isiBaru = document.createTextNode('ini list baru');
    liBaru.appendChild(isiBaru);

    const ul = document.querySelector('section#b ul');
    ul.appendChild(liBaru);

});

p4.addEventListener('click', function () {
    p4.style.backgroundColor = 'gold';
    p4.style.color = 'red';
})