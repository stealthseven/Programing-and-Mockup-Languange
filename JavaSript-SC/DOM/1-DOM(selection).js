// DOM selection
// document.getElementById() 
// -> element
const judul = document.getElementById('judul');
judul.style.color = "green";
judul.style.backgroundColor = "lightyellow";
judul.innerHTML = "tenangAja";

// document.getElementsByTagName()
// -> HTMLcollection 
//  p = HTMLcollection
const p = document.getElementsByTagName('p');
// p[0].style.backgroundColor = 'gold';
for (let i = 0; i < p.length; i++) {
    p[i].style.backgroundColor = 'lightyellow';
}
const h1 = document.getElementsByTagName('h1')[0]
h1.style.fontSize = "50px";

// document.getElementsByClassName()
// -> HTMLcollection 
const p1 = document.getElementsByClassName('p1')[0];
p1.innerHTML = 'Tulisan ini berubah';


// document.getquerySelector() 
// -> element
const p4 = document.querySelector('#b p')
p4.style.color = " green";
p4.style.fontSize = "40px"

const baris2 = document.querySelector('section#b ul li:nth-child(2)');
baris2.style.backgroundColor = 'lightgreen'

// document.getquerySelector() 
// -> element
const Z = document.querySelectorAll('p');
Z[2].style.backgroundColor = 'pink'

// node root
const sectionB = document.getElementById('b');
const par4 = sectionB.getElementsByTagName('p')[0];
par4.style.backgroundColor = "red"