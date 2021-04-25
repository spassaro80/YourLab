var sidebar = document.querySelector(".sidenav")
sidebar.addEventListener("mouseover", function() {
	this.style.width="300px"
})
sidebar.addEventListener("mouseout", function() {
	this.style.width="60px";
})