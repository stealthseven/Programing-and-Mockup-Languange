var tanya = true;
while (tanya) {
    // menangkap pilihan player
    var ppl = prompt("Masukkan pilihan mu [gajah, semut, orang]");

    // menangkap pilihan komputer 
    // membangkitkan bilangan random 
    var comp = Math.random();

    if (comp < 0.34) {
        comp = "gajah";
    } else if (comp >= 0.34 && comp < 0.77) {
        comp = "orang";
    } else {
        comp = "semut";
    }

    // menentukan rules 
    var hasil = ''
    if (ppl == comp) {
        hasil = 'seri';
    } else if (ppl == 'gajah') {
        if (comp == 'orang') {
            hasil = 'menang';
        } else {
            hasil = 'kalah';
        }
    } else if (ppl == 'orang') {
        if (comp == 'semut') {
            hasil = 'menang';
        } else {
            hasil = 'kalah';
        }
    } else if (ppl == 'semut') {
        if (comp == 'gajah') {
            hasil = 'menang';
        } else {
            hasil = 'kalah';
        }
    } else {
        hasil = 'data yang kamu masukan salah'
    }

    // bentuk rules yang lain
    // var hasil = ''
    // if (ppl == comp) {
    //     hasil = 'seri';
    // } else if (ppl == 'gajah') {
    //     hasil = (comp == 'orang') ? 'menang' : 'kalah';
    // } else if (ppl == 'orang') {
    //     hasil = (comp == 'gajah') ? 'kalah' : 'menang';
    // } else if (ppl == 'semut') {
    //     hasil = (comp == 'gajah') ? 'kalah' : 'menang';
    // } else {
    //     hasil = 'data yang kamu masukan salah'
    // }


    // tampilkan hasilnya
    alert('kamu memilih ' + ppl + ' dan komputer memilih ' + comp + ' maka kamu ' + hasil);

    tanya = confirm('apakah anda mau main lagi ?');
}
alert('terimakasih sudah bermain')