/*
Clara Mohri
SoftDev2 Pd06
K09 -- Connect the Dots
2019-03-13
*/

var pic = document.getElementById("vimage");
var b = document.getElementById("c");
var move = document.getElementById("m");
var list = [];

var draw = function(e){
    x2 = e.offsetX;
    y2 = e.offsetY;
    //console.log("drawing");
    var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    c.setAttribute("cx", e.offsetX);
    c.setAttribute("cy", e.offsetY);
    c.setAttribute("r", "20");
    c.setAttribute("fill", "red");
    c.setAttribute("stroke", "black");
    c.setAttribute("vx", "1");
    c.setAttribute("vy", "1");
    pic.appendChild(c);
    list.push(c);
};



var move = function(e) {
    window.cancelAnimationFrame(requestID)

    for (var i  = 0; i < list.length; i++ ){
	var circle = list[i];
	var cx = Number(circles[i].getAttribute("cx"));
	var cy = Number(circles[i].getAttribute("cy"));
	var xv = Number(circles[i].getAttribute("xv"));
	var yv = Number(circles[i].getAttribute("yv"));
	
	if (cx >= pic.getAttribute("width") || cx <= 0){
    	    xVel *= -1;
    	    list[i].setAttribute("xv", xv);
	}
	if (cy >= pic.getAttribute("height") || cy <= 0){
    	    yv *= -1;
    	    list[i].setAttribute("yvel", yv);
	}
	list[i].setAttribute('cx', cx + xv);      
	list[i].setAttribute('cy', cy + yv);
    }
    
    requestID = window.requestAnimationFrame(move);
    
}

var clear = function(e){
    while (pic.lastChild) {
	pic.removeChild(pic.lastChild);
    }
    x1 = undefined;
    x2 = undefined;
};

pic.addEventListener("click", draw);
b.addEventListener("click", clear);
move.addEventListener("click", move);




