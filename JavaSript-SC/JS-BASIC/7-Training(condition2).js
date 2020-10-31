// var s = '';
// for (var i = 0; i < 5; i++) {
//     s += '*';
// }
// console.log(s);

// var s = "";
// for (var i = 10; i > 0; i--) {
//     for (var l = 0; l < i; l++) {
//         s += "*";
//     }
//     s += "\n"
// }
// console.log(s);

var tinggi = parseInt(prompt('masukan tinggi yang anda ingin kan ? '))
var lop = "";
for (var line = 0; line <= tinggi; line++) {
    for (var bint = 0; bint < line; bint++) {
        lop += "*";
    }
    lop += "\n";
}
for (var line2 = tinggi; line2 >= 0; line2--) {
    for (var bint2 = 0; bint2 < line2; bint2++) {
        lop += "*";
    }
    lop += "\n";
}
console.log(lop);