const startButton = document.getElementById('start');
const stopButton = document.getElementById('stop');
const audioPlayer = document.getElementById('player');
const downloadLink = document.getElementById('download');
stopButton.disabled = true;
//var transcript;

//function getValue(value){
//	alert(value);
	
//	transcript = value;
//	}
const speechRecorder = (stream) => {
    mediaRecorder = new MediaRecorder(stream);
    mediaRecorder.addEventListener('dataavailable', (e) => {
        recordedChunks.push(e.data);
        if (mediaRecorder.state == "inactive") {
            let blob = new Blob(recordedChunks,{type: "audio/ogg;"});
            //let blob = new Blob(recordedChunks, {type: 'base64'});
            const audioBlob = blob
            const audioUrl = URL.createObjectURL(audioBlob);

            audioPlayer.controls = true;
            audioPlayer.src = audioUrl;
            downloadLink.href = audioUrl;
            let nameoffile = Math.floor((Math.random()*100) + 1);
            //let nameoffile = new Date().toISOString() + '.wav'
            //let nameoffile = 'file.wav'
            downloadLink.download = nameoffile ;

            blob = blobToFile(blob, nameoffile)
            // console.log(blob)
            //var data = '';
            //var reader = new window.FileReader();
            //reader.readAsDataURL(blob);
            //reader.readAsBinaryString(blob)
            //reader.onloadend = function() {
            	//base64 = reader.result;
            	//base64 = base64.split(',')[1];
            	//sendData(base64, nameoffile);
            	//data = base64;
            //}
            
            sendData(blob,nameoffile);
        }
      });
}

function blobToFile(theBlob, fileName){       
     return new File([theBlob], fileName, { lastModified: new Date().getTime(), type: theBlob.type })
}

// function blobToFile(theBlob, fileName){
//     //A Blob() is almost a File() - it's just missing the two properties below which we will add
//     theBlob.lastModifiedDate = new Date();
//     theBlob.name = fileName;
//     return theBlob;
// }

function sendData(base64,nameoffile) {
    var form = new FormData();
    form.append('file', base64);
    form.append('fname', nameoffile);
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/result/', true);
    xhr.send(form);
    //console.log(e.target.responseText);
    //var xhr1 = new XMLHttpRequest();
    //xhr1.open('PUT', '/', true);
    xhr.onreadystatechange = function(e) {
    	if (this.readyState == XMLHttpRequest.DONE && this.status == 200) {
    	//	document.getElementById('p1').innerHTML = window.var1;
    		console.log(e.target.responseText);
    		$("#p1").text(e.target.responseText);
    		}
    	};
   
    //$.ajax({
    //    type: 'POST',
    //    url:'/',
    //    data: form,
    //    cache: false,
    //    processData: false,
    //    contentType: false,
    //    success: function(response) {
    //        console.log(response);
    //    },
    //    error: function(error) {
    //        console.log(error);
    //    }
    //});
}

startButton.addEventListener('click', () => {
    document.getElementById('status').innerHTML = "Recording...";
    startButton.disabled = true;
    stopButton.disabled = false;
    recordedChunks = [];
    mediaRecorder.start();
});

stopButton.addEventListener('click', () => {
    document.getElementById('status').innerHTML = "Click on start to record.";
    stopButton.disabled = true;
    startButton.disabled = false;
    mediaRecorder.stop();
    //sendData(data, nameoffile);
});



navigator.mediaDevices.getUserMedia({
    audio: true, video: false
}).then(speechRecorder).catch((err) => {
    startButton.disabled = false;
    stopButton.disabled = true;
});
