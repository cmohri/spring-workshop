var canvas = document.getElementById("playground").getContext("2d");
var prevX, prevY;

function wipe() {
  canvas.clearRect(0,0,600,600);
  prevX = null;
}

function draw(event) {

  var x = event.offsetX;
  var y = event.offsetY;

  canvas.beginPath();
  canvas.fillStyle = "red";
  canvas.ellipse(x,y,10,10,Math.PI/4,0,2*Math.PI);
  canvas.fill();
  if (prevX) {
    canvas.fillStyle = "black";
    canvas.moveTo(prevX,prevY);
    canvas.lineTo(x,y);
  }
  canvas.stroke();
  prevX = x;
  prevY = y;
  canvas.closePath();
}
