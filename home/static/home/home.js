// HOME
let subMenu = document.getElementById("subManu");
var ifullbg = document.getElementById("idfullbg");
var inav = document.getElementById("idnav");
var ifullbg = document.getElementById("idfullbg");
var iycard = document.getElementById("idycard");
var iquestion = document.querySelectorAll("#idquestion");
var ians_ycard = document.querySelectorAll("#idans_ycard");
var ianswer = document.querySelectorAll("#idanswer");
// localStorage.setItem("lbooltheme","false");
var whooshcard = document.querySelectorAll("#idycard");

// Question card hover

function whooshgo(){
    var whoosh = new Audio("whoosh.mp3");
    whoosh.play();
}


console.log(whooshcard);
for(var i=0; i<whooshcard.length;i++)
{
    console.log(whooshcard[i]);
    whooshcard[i].addEventListener("mouseover",whooshgo);
}


// Question card hover end

function toggleMenu() {
    subMenu.classList.toggle("openmanu");
}


function handlereload(){
    if(localStorage.getItem("lbooltheme")==="true"){
        localStorage.setItem("lbooltheme","false");
    }
    else if(localStorage.getItem("lbooltheme")==="false"){
        localStorage.setItem("lbooltheme","true");
    }
    changetheme();
}


function changetheme(){
    if(localStorage.getItem("lbooltheme")==="true"){
        inav.classList.remove("blacknav");
        inav.classList.remove("navbar-dark");
        ifullbg.classList.remove("blackfullbg");
        for(var i=0;i<whooshcard.length;i++)
        {
            whooshcard[i].classList.remove("blackycard");
        }
        for(var j=0;j<iquestion.length;j++)
        {
            iquestion[j].classList.remove("blackquestion");
        }
        for(var k=0;k<ians_ycard;k++)
        {
            ians_ycard[i].classList.remove("blackans_ycard");
        }
        for(var l=0;l<ianswer.length;l++)
        {
            ianswer[l].classList.remove("blackanswer");
        }
        localStorage.setItem("lbooltheme","false");
    } 
    else{
        inav.classList.add("blacknav");
        inav.classList.add("navbar-dark");
        ifullbg.classList.add("blackfullbg");
        for(var i=0;i<whooshcard.length;i++)
        {
            
            whooshcard[i].classList.add("blackycard");
        }
        for(var j=0;j<iquestion.length;j++)
        {
            iquestion[j].classList.add("blackquestion");
        }
        for(var k=0;k<ians_ycard.length;k++)
        {
            console.log("1");
            ians_ycard[k].classList.add("blackans_ycard");
        }
        for(var l=0;l<ianswer.length;l++)
        {
            console.log("1");
            ianswer[l].classList.add("blackanswer");
        }
        
        localStorage.setItem("lbooltheme","true");
    }
}

window.onload = handlereload;

let nav = document.querySelector("nav");
let buttno = document.getElementById("idbuttno");
window.addEventListener("scroll", function () {

    const offset = window.pageYOffset;

    if (offset > 60) {
        nav.classList.add("scroll");
        buttno.classList.add("scrollbuttno");
    }
    else {
        nav.classList.remove("scroll");
        buttno.classList.remove("scrollbuttno");
    }
});

// Vanilla Tilt
VanillaTilt.init(document.querySelectorAll(".dev_card"), {
    max: 25,
    speed: 400
});