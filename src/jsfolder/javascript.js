Webcam.set({
  width: 320,
  height: 240,
  image_format: 'jpeg',
  jpeg_quality: 90
});
Webcam.attach('#my_camera');

var canvas = document.getElementById('viewport'),
  context = canvas.getContext('2d');

function take_snapshot() {
  // take snapshot and get image data
  Webcam.snap(function(data_uri) {
    base_image = new Image();
    base_image.src = data_uri;
    base_image.onload = function() {
      context.drawImage(base_image, 0, 0, 320, 240);

      let data = canvas.toDataURL('image/png');

      fetch(data)
        .then(res => res.blob())
        .then(blobData => {
        	 var params = {
            // Request parameters
            "returnFaceId": "true",
            "returnFaceLandmarks": "false",
            "returnFaceAttributes": "age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise",
        };

          $.post({
              url: "https://junghwanheo.cognitiveservices.azure.com/face/v1.0/detect?" + $.param(params),
              contentType: "application/octet-stream",
              headers: {
                'Ocp-Apim-Subscription-Key': 'insertyourAPIkey'
              },
              processData: false,
              data: blobData
            })
            .done(function(data) {

              let emotions = data[0]["faceAttributes"]["emotion"];

              console.log(emotions)

              let neutral = emotions["neutral"]
              let contempt = emotions["contempt"]
              let sadness = emotions["sadness"]
              let happiness = emotions["happiness"]

              let mood = ['negative', 'positive', 'neutral']

              let finalMood = null;
              if (contempt+sadness >.4)
                  finalMood = mood[0]
              else if (happiness >.4)
                  finalMood = mood[1]
              else
                  finalMood = mood[2]
              
         

              $("#results").html("You seem <strong>" + finalMood + "</strong>.<br><br> Are you feeling this way? <br> If yes, click <i>Continue</i>. If not, try taking taking another snapshot.");

              if($(".main-webcam a").length > 0){
                console.log("too long!")
                $(".main-webcam a").remove();
              }
              $(".main-webcam").append('<a href="' + finalMood + '.html"><button class="btn btn-primary">Continue</button></a>')
            })
            .fail(function(err) {
              $("#results").html(JSON.stringify(err));
            })
        });
    }
  });
};
