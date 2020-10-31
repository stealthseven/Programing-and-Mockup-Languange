// Selection
// const close = document.getElementsByClassName('close')[0];
// const card = document.getElementsByClassName('card')[0];

// close.addEventListener('click', function () {
//     card.style.display = 'none';
// })

// DOM TRAVERSAL 
// const closeBtn = document.querySelectorAll('.close');

// for (let i = 0; i < closeBtn.length; i++) {
//     closeBtn[i].addEventListener('click', function (e) {
//         e.target.parentElement.style.display = 'none';
//     });
// }

closeBtn.forEach(function (el) {
    el.addEventListener('click', function (e) {
        e.target.parentElement.style.display = 'none';
    });
});