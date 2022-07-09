
var options = {
    enableHighAccuracy: true,
    timeout: 5000,
    maximumAge: 0
};

function getLocation() {
    var x = document.getElementById("demo");
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition, null, options);
    } else {
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
}

function showPosition(position) {
    var x = document.getElementById("demo");
    x.innerHTML = "Latitude: " + position.coords.latitude +
        "<br>Longitude: " + position.coords.longitude;
}
