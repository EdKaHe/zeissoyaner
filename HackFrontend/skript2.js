(function($) { //Benötigen ja in disem Fall keine Animation, da dieser Kreis immer ausgefüllt ist
  $('.third.circle').circleProgress({
    value: 0,
    thickness: 20,
    animation: true,
    size: 250,
    startAngle: 1.5*Math.PI,
    emptyFill: "#D0D2E8",
    fill: {gradient: ['#141E8C', '#141E8C']}
}); 
})(jQuery);




function mykennnummer2() {

prozent = document.getElementById('pie').innerHTML;

(function($) { //Benötigen ja in disem Fall keine Animation, da dieser Kreis immer ausgefüllt ist
  $('.third.circle').circleProgress({
    value: 0 + (prozent/100),
    thickness: 20,
    animation: false,
    size: 250,
    startAngle: 1.5*Math.PI,
    emptyFill: "#D0D2E8",
    fill: {gradient: ['#141E8C', '#141E8C']}
}); 
})(jQuery);

    var erkennung = document.getElementById("kennummer").value;
	if (erkennung == "AAA") { 
    document.getElementById('pie').innerHTML = "80";
    document.getElementById('status2').innerHTML = "";
    document.getElementById('status').innerHTML = "Accepted";
	document.getElementsByTagName("input")[0].setAttribute("class", "democlass");

    var ctx = $('#myChart');
var ctx = document.getElementById("myChart");
ctx.height = 200;

var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
        datasets: [{
            label: 'Number of samples',
            data: [90, 80, 70, 80, 30, 20, 30, 20, 40, 30, 80, 20],
            backgroundColor: [
                'rgba(208, 210, 232, 100)',
                'rgba(208, 210, 232, 100)',
                'rgba(208, 210, 232, 100)',
                'rgba(208, 210, 232, 100)',
                'rgba(208, 210, 232, 100)',
                'rgba(208, 210, 232, 100)',
                'rgba(208, 210, 232, 100)',
                'rgba(208, 210, 232, 100)',
                'rgba(208, 210, 232, 100)',
                'rgba(208, 210, 232, 100)',
                'rgba(20, 30, 140, 100)',
                'rgba(208, 210, 232, 100)'
            ],
            // borderColor: [
            //     'rgba(255,99,132,1)',
            //     'rgba(54, 162, 235, 1)',
            //     'rgba(255, 206, 86, 1)',
            //     'rgba(75, 192, 192, 1)',
            //     'rgba(153, 102, 255, 1)',
            //     'rgba(255, 159, 64, 1)'
            // ],
            // borderWidth: 1
        }]
    },
    maintainAspectRatio: false,
    options: {
        scales: {

            yAxes: [{
                ticks: {
                    beginAtZero:true
                }
            }]
        }
    }
});



    } 
    else if (erkennung == "BBB") { 
    document.getElementById('pie').innerHTML = "20";
    document.getElementById('status').innerHTML = "";
    document.getElementById('status2').innerHTML = "Declined";
	document.getElementsByTagName("input")[0].setAttribute("class", "democlass");

    var ctx = $('#myChart');
var ctx = document.getElementById("myChart");
ctx.height = 200;

var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
        datasets: [{
            label: 'Number of samples',
            data: [90, 80, 70, 80, 30, 20, 30, 20, 40, 30, 80, 20],
            backgroundColor: [
                'rgba(208, 210, 232, 100)',
                'rgba(208, 210, 232, 100)',
                'rgba(208, 210, 232, 100)',
                'rgba(208, 210, 232, 100)',
                'rgba(208, 210, 232, 100)',
                'rgba(208, 210, 232, 100)',
                'rgba(208, 210, 232, 100)',
                'rgba(208, 210, 232, 100)',
                'rgba(208, 210, 232, 100)',
                'rgba(208, 210, 232, 100)',
                'rgba(208, 210, 232, 100)',
                'rgba(20, 30, 140, 100)',
            ],
            // borderColor: [
            //     'rgba(255,99,132,1)',
            //     'rgba(54, 162, 235, 1)',
            //     'rgba(255, 206, 86, 1)',
            //     'rgba(75, 192, 192, 1)',
            //     'rgba(153, 102, 255, 1)',
            //     'rgba(255, 159, 64, 1)'
            // ],
            // borderWidth: 1
        }]
    },
    maintainAspectRatio: false,
    options: {
        scales: {

            yAxes: [{
                ticks: {
                    beginAtZero:true
                }
            }]
        }
    }
});


    } else {
    document.getElementsByTagName("input")[0].setAttribute("class", "democlass2");

}

// document.getElementById('imag').src = "img/"+erkennung+"/1.png";
// document.getElementById('imag2').src = "img/"+erkennung+"/2.png";
// document.getElementById('imag3').src = "img/"+erkennung+"/3.png";
// document.getElementById('imag4').src = "img/"+erkennung+"/4.png";

}






