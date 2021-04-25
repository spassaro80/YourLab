// Stats functions

var rightbars = document.querySelectorAll(".rightbar")
for (var bar of rightbars){
var tot = 0
var barLength = 0		
var tot = parseInt(bar.nextElementSibling.children[0].textContent)
	if (tot) {
	var barLength = (Math.round((parseInt(bar.textContent) / tot * 100)*100)/100).toString() + "%"
	}
	else {barLength = tot}
bar.children[0].style.width=barLength
}
var leftbars = document.querySelectorAll(".leftbar")
for (var bar of leftbars){
var tot = 0
var barLength = 0
var tot = parseInt(bar.previousElementSibling.children[0].textContent)
if (tot) {
var barLength = (Math.round((parseInt(bar.textContent) / tot * 100)*100)/100).toString() + "%"
var margin = (100-(Math.round((parseInt(bar.textContent) / tot * 100)*100)/100)).toString() + "%"
}
else {
barLength = 0
margin = 0	
}
bar.children[0].style.width=barLength
bar.children[0].style.marginLeft=margin
}

//  Stats for clocks (possession)

function timestrToSec(timestr) {
	var parts = timestr.split(":");
	return (parts[0] * 3600) +
		   (parts[1] * 60) +
		   (+parts[2]);
  }
  
function pad(num) {
	if(num < 10) {
	  return "0" + num;
	} else {
	  return "" + num;
	}
}
  
function formatTime(seconds) {
	return [pad(Math.floor(seconds/3600)),
			pad(Math.floor(seconds/60)%60),
			pad(seconds%60),
			].join(":");
}

var rightclocks=document.querySelectorAll(".rightclock")
for (rightclock of rightclocks) {
leftclock = rightclock.previousElementSibling.previousElementSibling
leftvalue = (leftclock.textContent.replace(/\s/g,''))
rightvalue = (rightclock.textContent.replace(/\s/g,''))
var tot = formatTime(timestrToSec(leftvalue) + timestrToSec(rightvalue));
if (tot !="00:00:00") {
	margin = 100 - Math.round((timestrToSec(leftvalue) / timestrToSec(tot)) * 100)
	leftclock.children[0].style.width = Math.round((timestrToSec(leftvalue) / timestrToSec(tot)) * 100).toString() + "%"
	leftclock.children[0].textContent = Math.round((timestrToSec(leftvalue) / timestrToSec(tot)) * 100).toString() + "%"
	rightclock.children[0].style.width = Math.round((timestrToSec(rightvalue) / timestrToSec(tot)) * 100).toString() + "%"
	rightclock.children[0].textContent = Math.round((timestrToSec(rightvalue) / timestrToSec(tot)) * 100).toString() + "%"
	leftclock.children[0].style.marginLeft = margin.toString() + "%"
} else {
	leftclock.children[0].style.width  = "0%"
	leftclock.children[0].textContent =  "0%"
	rightclock.children[0].style.width = "0%"
	rightclock.children[0].textContent = "0%"	
}
}

  


