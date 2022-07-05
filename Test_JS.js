

function AddOneLocal() {

    var InNumber = document.getElementById('inputText').value;

    if (isFinite(InNumber)) {
        document.getElementById('inputText').value = parseFloat(InNumber) + 1
    }


    var file = document.getElementById("uploadfile").value;
    $.post('localhost:22222', //this is where I am hosting the server
        { SendData: file },
        function (returnedArray) {
            var newData = //the response from python server, in array format;
                //set up different variables from the array
                //update the returned_info div with the new data
            }
    )

}

