/*
Clara Mohri
SoftDev2 Pd06
K09 -- Connect the Dots
2019-03-13
*/

var pic = document.getElementById("vimage");
var b = document.getElementById("c");
var x1, x2, y1, y2;

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
    pic.appendChild(c);    
    var l = document.createElementNS("http://www.w3.org/2000/svg", "line");    
    if (x1 & x2){
	console.log("Draw line");
	l.setAttribute("x1", x1);
	l.setAttribute("y1", y1);
	l.setAttribute("x2", x2);
	l.setAttribute("y2", y2);
	l.setAttribute("stroke", "black");
	pic.appendChild(l);
    }
    x1 = x2;
    y1 = y2;
};

var clear = function(e){
    while (pic.lastChild) {
	pic.removeChild(pic.lastChild);
    }
    x1 = undefined;
    x2 = undefined;
};

pic.addEventListener("click", draw);
b.addEventListener("click", clear);
