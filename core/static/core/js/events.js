var generalcrono = document.querySelector('#crono1');
var events = document.querySelectorAll("input")
for (var newevent of events) {
    newevent.addEventListener("change", function(){
        console.log(generalcrono.value + " " + this.parentElement.parentElement.previousElementSibling.textContent + " " + this.name.slice(-1))
        var crono=generalcrono.value
        const url = "{% url 'core:new_event' match.pk %}" + "?crono=" + crono
        fetch(url).then(response => response.json()).then(function(data) {
            console.log(data.created)
        })
    })
}