var c = document.getElementById("slate");
var ctx = c.getContext("2d");
var clear = document.getElementById("clear");
var toggle = document.getElementById("toggle");
var ctr = 0;

// clear canvas
var clr = function(e){
    ctx.clearRect(0, 0, c.width, c.height);
};

// update ctr to reflect whether drawing circles or rectangles
var update = function(e){
    ctr += 1;
    console.log(ctr);
};

// draw either circles or rectangles
// random size, random color
var draw = function(e){
    e.preventDefault();
    var xcor = e.offsetX;
    var ycor = e.offsetY;
    var colors = ['red', 'blue', 'green', 'yellow', 'black', 'purple', 'turquoise', 'orange'];
    var random = colors[Math.floor(Math.random() * colors.length)];
    ctx.fillStyle = random;
    if (ctr % 2 == 0){
	// rectangles have random dimensions
	ctx.fillRect(xcor, ycor, Math.random()*15 + 10, Math.random()*15 + 10);
    }
    else{
	// circles have random radii
	var r = Math.random()*15 + 10;
	ctx.beginPath();
	ctx.ellipse(xcor, ycor, r, r, Math.PI / 4, 0, 2 * Math.PI);
	ctx.fill();
    }
};

c.addEventListener("click", draw);
clear.addEventListener("click", clr);
toggle.addEventListener("click", update);
