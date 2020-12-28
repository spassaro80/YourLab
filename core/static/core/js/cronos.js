// // Crono functions

// var Crono = {
// 	on : false,
// } 

// var startbtns = document.getElementsByClassName("startbtn")
// var stopbtns = document.getElementsByClassName("stopbtn")
// var resetbtns = document.getElementsByClassName("resetbtn")

// // Create a crono object for every crono displayed and append into a crono array

// crono_obj = [];
// cronos = document.getElementsByClassName("crono")
// for (i=0; i<cronos.length; i++) {
// 	crono_obj.push(Object.create(Crono))
// }


// var avvia = document.querySelector("#avvia1")
// avvia.addEventListener("click", function() {
// 	crono = this.previousElementSibling
// 	i = Number(crono.id[5]) - 1
// 	startCrono(crono, i)
// 	// this.previousElementSibling.stepUp()
// })

// function startCrono(crono, i) {
// 	if(crono_obj[i].on == false) {
// 		crono_obj[i].on = true;
// 	}
// 	cronometro(crono, i);
// }

// function cronometro(crono,i) {
// 	if(crono_obj[i].on == true) {
// 		setTimeout(crono.stepUp(), 100);
// 	}
// }

// function stopCrono(crono,i) {
// 	crono_obj[i].on = false;
// }