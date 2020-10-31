// var arrayw = ['1', 2, "makan ayam", [1, 3, 4, 55], 1, 3];

// console.log(arrayw.length)
// console.log(arrayw[3][2])

//menambah isi array dengan indikator indeks
var a = [];
a[1] = "rafa";
a[2] = 'rahadi';

console.log(a)

//menghapus isi array
a[2] = undefined;

//menampilkan isi arrat 
var bhe = ["rafa", "rahadi", '1', '2', ];
for (var i = 0; i < bhe.length; i++) {
    console.log('mahasiswa ke-' + (i + 1) + ' : ' + bhe[i])
}

//edit array menggunakan methode 
//menampilkan array menggunakna join
var dataA = ["shandi", "rudi", "budhi"];
console.log(dataA.join("-"));
//memanipulasi array menggunakna push
var dataB = ["shandi", "rudi", "budhi"];
dataB.push("comatkamit", "indigay");
console.log(dataB.join("-"));
//memanipulasi array menggunakna pop
var dataC = ["shandi", "rudi", "budhi"];
dataC.pop("budhi");
console.log(dataC.join("-"));
// memanipulasi array menggunakan unshift & shift
var dataD = ["shandi", "1", "budhi"];
dataD.unshift("tedjo");
// dataD.shift("shandi");
console.log(dataD.join("-"));
// memanipulasi array menggunakan splice
var dataE = ["shandi", "rudi", "budhi"];
dataE.splice(1, 0, "lordLuhut", "luhutGendeng");
console.log(dataE.join("-"));
dataE.splice(2, 2);
console.log(dataE.join("-"));
// memanipulasi array menggunakan slice
// slice(awal, akhir)
var dataF = ["shandi", "rudi", "budhi", "nuna", 'wisnu', "luhut"];
var dataPengambil = dataF.slice(3, 5);
console.log(dataPengambil.join("-"));

// memanipulasi array menggunakan forEach
var angka = [1, 2, 4, 5, 7, 8, 2, 1, 3];
angka.forEach(function (e) {
    console.log(e);
});

// memanipulasi array menggunakan map
var angka = [1, 2, 4, 5, 7, 8, 2, 1, 3];
var angka2 = angka.map(function (es) {
    return es * 2;
})
console.log(angka2.join("-"));

// memanipulasi array menggunakan sort
var angka = [1, 2, 4, 5, 7, 8, 2, 1, 3];
var angka3 = angka.sort()
console.log(angka3.join("-"))
// memanipulasi array menggunakan sort tambahan
var dataKamu = [11, 22, 4, 5, 71, 8, 2, 21, 3];
var dataAku = dataKamu.sort(function (x, y) {
    return x - y;
})
console.log(dataAku.join("-"))
// memanipulasi array menggunakan filter & find
var bangke = [1, 2, 4, 5, 7, 8, 2, 1, 3];
var angka4 = bangke.filter(function (g) {
    return g > 5;
});
console.log(angka4.join("|-|"))

var angka5 = bangke.find(function (q) {
    return q > 5;
});
console.log(angka5);