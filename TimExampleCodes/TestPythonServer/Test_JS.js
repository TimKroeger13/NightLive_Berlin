

function AddOneLocal() {

    var InNumber = document.getElementById('inputText').value;

    if (isFinite(InNumber)) {
        document.getElementById('inputText').value = parseFloat(InNumber) + 1
    }




}

