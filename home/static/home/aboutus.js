// HOME
// let subMenu = document.getElementById("subManu");
// var ifullbg = document.getElementById("idfullbg");
var inav = document.getElementById("idnav");
let subMenu = document.getElementById("subManu");
// var ifullbg = document.getElementById("idfullbg");
// var iycard = document.getElementById("idycard");
// var iquestion = document.getElementById("idquestion");
// var ians_ycard = document.getElementById("idans_ycard");
// var ianswer = document.getElementById("idanswer");

// About US
var ifullbg = document.getElementById("idfullbg");
var idesc1 = document.getElementById("iddesc1");


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
    uptheme_aboutus();
}

function uptheme_aboutus(){
    if(localStorage.getItem("lbooltheme")==="false"){
        inav.classList.add("blacknav");
        inav.classList.add("navbar-dark");
        ifullbg.classList.add("blackfullbg");
        idesc1.classList.add("blackdesc1");
        localStorage.setItem("lbooltheme","true");
    }
    else if(localStorage.getItem("lbooltheme")==="true"){
        inav.classList.remove("blacknav");
        inav.classList.remove("navbar-dark");
        ifullbg.classList.remove("blackfullbg");
        idesc1.classList.remove("blackdesc1");
        localStorage.setItem("lbooltheme","false");
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