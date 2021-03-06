var c = document.getElementById("slate");
var ctx = c.getContext("2d");
var clear = document.getElementById("clear");
var toggle = document.getElementById("toggle");
var state = 0;

// clear canvas
var clr = function(e){
    ctx.clearRect(0, 0, c.width, c.height);
};

// update state to reflect whether drawing circles or rectangles
var update = function(e){
    state += 1;
};

// draw either circles or rectangles
// random size, random color
var draw = function(e){
    // prevent default ... 
    e.preventDefault();
    // coordinates within div where mouse was clicked
    var xcor = e.offsetX;
    var ycor = e.offsetY;
    var colors = ['red', 'blue', 'green', 'yellow', 'black', 'purple', 'turquoise', 'orange'];
    var random = colors[Math.floor(Math.random() * colors.length)];
    ctx.fillStyle = random;
    if (state % 2 == 0){
	// rectangles have random dimensions
	ctx.fillRect(xcor, ycor, Math.random()*15 + 10, Math.random()*15 + 10);
    }
    else{
	// circles have random radii
	var r = Math.random()*15 + 10;
	// begins filling ellipse at Math.Pi / 4
	ctx.beginPath();
	ctx.ellipse(xcor, ycor, r, r, Math.PI / 4, 0, 2 * Math.PI);
	ctx.fill();
    }
};

c.addEventListener("click", draw);
clear.addEventListener("click", clr);
toggle.addEventListener("click", update);
