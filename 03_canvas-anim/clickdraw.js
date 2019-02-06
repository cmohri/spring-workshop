// Clara Mohri, Michelle Tang
// SoftDev2 pd6
// K#03 -- They lock us in the tower whenever we get caught
// 2019-02-05

var c = document.getElementById("slate");
var ctx = c.getContext("2d");
var dotButton = document.getElementById("begin");
var stopButton = document.getElementById("stop");
ctx.fillStyle =	"#00ffff";


var r = 0;
var growing = true;
var id = 0

// Clears the canvas!
var clear = function(e){
  var width = c.getAttribute("width");
  var height = c.getAttribute("height");
  ctx.clearRect(0,0,width, height);

}

// Draws the circle
var drawDot = function(e){
  clear() // Clears the canvas so circles don't overlap

  // Determines whether the circle should grow or shrink
  if (r == (c.width/2)){ // Radius is max
    growing = false ;
    console.log("start shrinking") ;
  }
  if (r == 0){ // Radius is min
    growing = true
    console.log("start growing") ;
  }
  ctx.beginPath();
  ctx.arc(c.width / 2, c.height / 2, r, 0, 2* Math.PI);
  ctx.stroke();
  ctx.fill();
  // Increases/Decreases the radius based on whether it is growing or shrinking
  if (growing){
    r +=1;
  }
  else{
    r -=1;
  }
  console.log("Radius " + r);
  // Animate, record its ID num
  id = requestAnimationFrame(drawDot)
};

// Stops the animation
var stop = function(e){
  console.log("Stop animating") ;
  cancelAnimationFrame(id) // Stops animation based on ID num
  id = 0 // Reset ID to zero

};

dotButton.addEventListener("click", function (e){
  // Checks if there is an animation in progress, if there is prevent another
  if (id){
    console.log("Animation already in progress") ;
    e.preventDefault()
  }
  else{
    console.log("Start an animation")
    drawDot()
  } } );
stopButton.addEventListener("click", stop);
