// Timer functions

var Crono = {
	ore : 0, 
	minuti : 0, 
	secondi : 0, 
	decimi : 000,
	on : true,
	vis : ""

} 

// Create a crono object for every crono displayed and append into a crono array

crono_obj = [];
cronos = document.getElementsByClassName("crono")
for (i=0; i<cronos.length; i++) {
	crono_obj.push(Object.create(Crono))
	crono_obj[i].ore=parseInt(cronos[i].value[0] + cronos[i].value[1])
	crono_obj[i].minuti=parseInt(cronos[i].value[3] + cronos[i].value[4])
	crono_obj[i].secondi=parseInt(cronos[i].value[6] + cronos[i].value[7])
}

var startbtns = document.getElementsByClassName("startbtn")
var stopbtns = document.getElementsByClassName("stopbtn")
var resetbtns = document.getElementsByClassName("resetbtn")

function startCrono(crono, i) {
	if(crono_obj[i].on == true) {
		crono_obj[i].on = false;
		cronometro(crono, i);
	}
}

function cronometro(crono, i) {
	if(crono_obj[i].on == false) {
		crono_obj[i].decimi = crono_obj[i].decimi + 100;
		if(crono_obj[i].decimi > 900) {
			crono_obj[i].decimi = 0;
			crono_obj[i].secondi++;
		}
		if(crono_obj[i].secondi > 59) {
			crono_obj[i].secondi = 0;
			crono_obj[i].minuti++;
		}
		if(crono_obj[i].minuti > 59) {
			crono_obj[i].minuti = 0;
			crono_obj[i].ore++;
		}
		showCrono(crono, i);
		setTimeout(function() {cronometro(crono, i)}, 100);
		console.log(crono, i)
	}
}
function showCrono(crono, i) {
	if(crono_obj[i].ore < 10) crono_obj[i].vis = "00:"; else crono_obj[i].vis = ore + ":";
	if(crono_obj[i].minuti < 10) crono_obj[i].vis = crono_obj[i].vis + "0";
	crono_obj[i].vis = crono_obj[i].vis + crono_obj[i].minuti + ":";
	if(crono_obj[i].secondi < 10) crono_obj[i].vis = crono_obj[i].vis + "0";
	crono_obj[i].vis = crono_obj[i].vis + crono_obj[i].secondi + "." + crono_obj[i].decimi;
	crono.value = crono_obj[i].vis;
}
function stopCrono(crono, i) {
	crono_obj[i].on = true;
	showCrono(crono, i);
}
function resetCrono(crono, i) {
	if(crono_obj[i].on == false) {
		crono_obj[i].on = true;
	}
    crono_obj[i].ore = crono_obj[i].minuti = crono_obj[i].secondi = crono_obj[i].decimi = 0;
	crono_obj[i].vis = "";
	showCrono(crono, i);
}

for(i=0; i < startbtns.length; i++) {
startbtns[i].addEventListener('click', function() {
		crono = this.closest("#button_container").closest(".cronom").children[0]
		i = Number(crono.id[5]) - 1
	startCrono(crono, i) 	
});
};

for(i=0; i < stopbtns.length; i++) {

stopbtns[i].addEventListener('click', function() {
	crono = this.closest("#button_container").closest(".cronom").children[0]
	i = Number(crono.id[5]) - 1
	stopCrono(crono, i) 	
});
};

for(i=0; i < resetbtns.length; i++) {
	resetbtns[i].addEventListener('click', function() {
	crono = this.closest("#button_container").closest(".cronom").children[0]
	i = Number(crono.id[5]) - 1
	resetCrono(crono, i)	
});
};

