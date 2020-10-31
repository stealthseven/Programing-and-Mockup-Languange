// EMELEMNT MANIPULATION 

// const ubahJudul = document.getElementById('judul');
// ubahJudul.innerHTML = 'hiyak hiyak';

// const ubahSectionA = document.querySelector("#a")
// ubahSectionA.innerHTML = "hellow Everybodhi"

// const ubahJudul = document.querySelector('#a');
// ubahJudul.style.color = "gold";
// ubahJudul.style.backgroundColor = "lightyellow";

// const ubahJudul = document.getElementsByTagName('h1')[0];
// ubahJudul.setAttribute('name', 'Rafa');
// ubahJudul.removeAttribute('name')

// const p2 = document.querySelector('.p2');
// p2.setAttribute('class', 'label');

///////////////////////////////////////////////////////////////////////
// NODE MANIPULATION
// buat elemen baru

// appendChild = masukan data terakhir
const pBaru = document.createElement('p');
const txtPBaru = document.createTextNode('Ini Adalah Paragraf Baru');
// simpan tulisan ke dalam paragraf
pBaru.appendChild(txtPBaru);
// simpan txtPBaru di akhir section A
const sectionA = document.getElementById('a');
sectionA.appendChild(pBaru);

// insertBefore = masukan data sebelum sebuah item
const liBaru = document.createElement('li');
const isiLi = document.createTextNode('ini list baru');
liBaru.appendChild(isiLi);

const ul = document.querySelector('section#b ul');
const liBaru2 = ul.querySelector('li:nth-child(2)');

ul.insertBefore(liBaru, liBaru2);

// remove
const link = document.getElementsByTagName('a')[0];
sectionA.removeChild(link);

// replace
const sectionB = document.getElementById('b');
const par4 = sectionB.querySelector('p');
// 
const h2Baru = document.createElement('h2');
const teksH2Baru = document.createTextNode('judul baru');
// 
h2Baru.appendChild(teksH2Baru);
sectionB.replaceChild(h2Baru, par4);