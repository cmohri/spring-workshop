
function getData(){

    var newL = [];
    d3.csv("https://raw.githubusercontent.com/stuy-softdev/workshop/master/thluffy/21_js-mfr/2006_-_2012_School_Demographics_and_Accountability_Snapshot.csv?token=AG6ZZWEGWQ7UTMOPYFI3EZS42BQQC", function(csv){
	var row = [];
	for (i in csv){
	    //console.log(i);
	    row.push(csv[i]);
	}
	newL.push(row);

    })
    
    console.log(newL);
    var education = []
    console.log(newL[0].length);
    for (var i = 0; i < newL.length; i++){
	console.log(i);
	education.push(newL[i][2]);
    }
    console.log(education);
    
/*unable to get this to work*/
    
};


getData();


var para = document.createElement("p");
var node = document.createTextNode("This is new.");
para.appendChild(node);

var element = document.getElementById("div1");
element.appendChild(para);
