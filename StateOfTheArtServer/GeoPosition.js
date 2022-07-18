
function CreateLeafletMap(json) {

    var map = L.map('map').setView([52.5101148, 13.3303686], 12);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '© OpenStreetMap'
    }).addTo(map);

    for (let i = 0; i < json["location"]["coordinates"].length; i++) {
        lat = json["location"]["coordinates"][i][0]
        long = json["location"]["coordinates"][i][1]

        var marker = L.marker([lat, long]).addTo(map);
    }

    var barStyle = {
        "color": "#0020C4",
        "weight": 2,
        "opacity": 1
    };

    var nightclubsStyle = {
        "color": "#C60060",
        "weight": 2,
        "opacity": 1
    };

    L.geoJSON(bar, { style: barStyle }).addTo(map);
    L.geoJSON(nightclubs, { style: nightclubsStyle }).addTo(map);



}


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

    location.reload();

}

function GetServerData() {

    const Mapbox = document.getElementById('map');

    if (Mapbox.childNodes.length == 2) {

        location.reload();

    }

    const url = 'http://localhost:1234/GetData'
    fetch(url)
        .then(response => response.json())
        .then(json => {
            CreateLeafletMap(json)
            document.getElementById("ServerData").innerHTML = JSON.stringify(json)
        })
}

