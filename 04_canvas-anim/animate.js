/*
The Office Launch Party
Clara Mohri Michelle Tang
K04 -- What is it saving the screen from?
2019-02-06
*/

var c = document.getElementById("playground");
var ctx = c.getContext("2d");
var dotButton = document.getElementById("circle");
var dvdButton = document.getElementById("dvd");
var stopButton = document.getElementById("stop");
ctx.fillStyle =	"#00ffff";

var r = 0;
var growing = true;
var id = 0;

// Clears the canvas!
var clear = function(e){
  var width = c.getAttribute("width");
  var height = c.getAttribute("height");
  ctx.clearRect(0,0,width, height);

}

// Draws the circle
var drawDot = function(e){
    window.cancelAnimationFrame(id);
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
    cancelAnimationFrame(id); // Stops animation based on ID num
    id = 0; // Reset ID to zero
};

dotButton.addEventListener("click", function (e){
    drawDot();
});
			   
stopButton.addEventListener("click", stop);


var dvdLogoSetup = function() {
    window.cancelAnimationFrame(id);
    clear();

    var rectWidth = 100;
    var rectHeight = 50;

    var rectX = Math.floor(Math.random()* (c.width-rectWidth));
    var rectY = Math.floor(Math.random() * (c.height - rectHeight));

    var xVel = 1;
    var yVel = 1;

    var logo = new Image();
    logo.src = "logo_dvd.jpg";
    

    var dvdLogo  = function() {
	ctx.drawImage(logo, rectX, rectY, rectWidth, rectHeight);
	

	rectX += xVel;
	rectY += yVel;

	if (rectX == 0 || rectX == c.width - rectWidth){
	    xVel *= -1;
	}
	if (rectY == 0 || rectY == c.height - rectHeight){
	    yVel *= -1;
	}
	
	
	id = window.requestAnimationFrame(dvdLogo);
    };
	
    dvdLogo();

};


dvdButton.addEventListener("click", dvdLogoSetup);
