// Options for the latancy
var options = {
    enableHighAccuracy: true,
    timeout: 5000,
    maximumAge: 0
};

// Get Location function
function getLocation() {
    var x = document.getElementById("latlon");
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition, null, options);
    } else {
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
}

// Send Location back localy
function showPosition(position) {
    var x = document.getElementById("latlon");
    x.innerHTML = "Latitude: " + position.coords.latitude +
        "<br>Longitude: " + position.coords.longitude;
    SendPostion(position)
}

// Creting Jason and run tranform it back and forth for testing
function SendPostion(position) {
    const PosLat = position.coords.latitude
    const PosLon = position.coords.longitude

    const CoordinateJason = JSON.stringify({ // Creates a String in the Jason format. But its still only a String.
        "location": {
            "type": "point",
            "coordinates": [
                PosLat,
                PosLon
            ],
            "specific": "unknown"
        }
    });

    const jasonFormat = JSON.parse(CoordinateJason) // jasonFormat is now a Jason file
    console.log(jasonFormat) // You can also take a look at it in the debug mode, to see that everything is sorted right and its not loger a string.

    run(CoordinateJason);
}

//sending data
function run(CoordinateJason) {

    console.log(CoordinateJason)

    // Creating Our XMLHttpRequest object
    var xhttp = new XMLHttpRequest();

    // Making our connection
    xhttp.open('POST', "http://localhost:1234/", true); // Where to send the data and how
    xhttp.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded;charset=UTF-8'); // Jason is sended as as String

    //Sendig Data with Key
    var dataForSending = "NLBObject=" + CoordinateJason
    xhttp.send(dataForSending); //Send the data to the server

    console.log("[SENDED] Json sended to the server");

}

function GetServerData() {
    const url = 'http://localhost:1234/GetData'
    fetch(url)
        .then(response => response.json())
        .then(json => {
            JasonToMap(json)
            document.getElementById("ServerData").innerHTML = JSON.stringify(json)
        })
}

//example function

function JasonToMap(jsonData) {

    console.log("[RECEIVED] Json was received from the server")
    console.log(jsonData)

}