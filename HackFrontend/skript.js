function mykennnummer1() {

    var erkennung = document.getElementById("kennummer").value;

	if (erkennung == "AAA") { 
	document.getElementsByTagName("input")[0].setAttribute("class", "democlass");
	document.getElementById('imag').src = "img/AAA/1.png";
	document.getElementById('imag2').src = "img/AAA/2.png";
	document.getElementById('imag3').src = "img/AAA/3.png";
	document.getElementById('imag4').src = "img/AAA/4.png";
    } 
    else if (erkennung == "BBB") { 
	document.getElementsByTagName("input")[0].setAttribute("class", "democlass");
	document.getElementById('imag').src = "img/AAA/1.png";
	document.getElementById('imag2').src = "img/AAA/2.png";
	document.getElementById('imag3').src = "img/AAA/3.png";
	document.getElementById('imag4').src = "img/AAA/4.png";
    } else {
    document.getElementsByTagName("input")[0].setAttribute("class", "democlass2");
    document.getElementById('imag').src = "";
	document.getElementById('imag2').src = "";
	document.getElementById('imag3').src = "";
	document.getElementById('imag4').src = "";
}

// document.getElementById('imag').src = "img/"+erkennung+"/1.png";
// document.getElementById('imag2').src = "img/"+erkennung+"/2.png";
// document.getElementById('imag3').src = "img/"+erkennung+"/3.png";
// document.getElementById('imag4').src = "img/"+erkennung+"/4.png";
}
