// function hitung2Vol(a, b) {
//     volumeA = a * a * a;
//     volumeB = b * b * b;

//     hasilAkhir = volumeA + volumeB
//     return hasilAkhir
// }

// var test = hitung2Vol(2, 4)
// console.log(test)

// arguments (array)
function hitungTambah() {
    var hasil = 0;
    for (var i = 0; i < arguments.length; i++) {
        hasil += arguments[i];
    }
    return hasil
}
var coba = hitungTambah(2, 2, 2, 2, 2, 2);
console.log(coba);