let portfolio = document.getElementById("portfolio");
let signlogin = document.getElementById("signlogin");

let user = document.getElementById("user");
let biog = document.getElementById("biog");
let loggedIn = false;


let nameSub = document.getElementById("nameSub");
let biogSub = document.getElementById("biogSub");
let nameMain = document.getElementById("nameMain");
let biogMain = document.getElementById("biogMain");
let bgColor = document.getElementById("bgColor");

// pop-up menus
let write = document.getElementById("write");
    write.style.display="none";
let colors = document.getElementById("colors");
    colors.style.display="none";
let margin = document.getElementById("margin");
    margin.style.display="none";
let templates = document.getElementById("templates");
    templates.style.display="none";
    
box1 = document.getElementById("box1");
    box1Text = document.getElementById("box1Text");
box2 = document.getElementById("box2");
    box2Text = document.getElementById("box2Text");
box3 = document.getElementById("box3");
    box3Text = document.getElementById("box3Text");
box4 = document.getElementById("box4");
    box4Text = document.getElementById("box4Text");
box5 = document.getElementById("box5");
    box5Text = document.getElementById("box5Text");
box6 = document.getElementById("box6");
    box6Text = document.getElementById("box6Text");


nameSub.onclick = function(){
    const myName = document.getElementById("nameText").value;
    fetch("/my-page", {
        method: "POST",
        headers : {
            "Content-Type": "application/json",
            "Authorization": auth.currentUser.uid    // 👈 send UID here!
        },
        body: JSON.stringify({title : myName})
    })
    .then(() => {document.getElementById("user").textContent = `${myName}'s Portfolio`});
}

biogSub.onclick = function(){
    const myBio = document.getElementById("bio").value;
    fetch("/my-page", {
        method:"POST",
        headers: {
            "Content-Type":"application/json",
            "Authorization": auth.currentUser.uid    // 👈 send UID here!
        },
        body: JSON.stringify({biog:myBio})
    })
    .then(() => {document.getElementById("biog").textContent = myBio});
}



function showMenu(){
    menuArrow = document.getElementById("menuArrow");
    menu = document.getElementById("menu");
    menuLoadOut = document.getElementById("menuLoadOut");
    if(getComputedStyle(menu).top == "0px"){
        menu.style.top = "200px";
        menuLoadOut.style.display = "block";
        menuArrow.textContent = "/\\"
    }
    else if(getComputedStyle(menu).top == "200px"){
        menu.style.top = "0px";
        menuLoadOut.style.display = "none";
        menuArrow.textContent = "\\/"
    }
}

function writePop(){
    write.style.display = "block";
}
function colorsPop(){
    colors.style.display = "block";
}
function marginPop(){
    margin.style.display = "block";
}


function nameCloser(){
    write.style.display= "none";
}
function colorCloser(){
    colors.style.display = "none";
}
function marginCloser(){
    margin.style.display = "none";
}

//Make the DIV elements draggable:

/* CHANGE COLOR BUTTON */
function changeColor(color){
    fetch("/my-page", {
        method:"POST",
        headers: {
            "Content-Type":"application/json",
            "Authorization": auth.currentUser.uid    // 👈 send UID here!
        },
        body: JSON.stringify({background_color:color})
    })
    .then(() => {document.body.style.backgroundColor = color});
}
function changeNameColor(nameColor){
    fetch("/my-page", {
        method:"POST",
        headers: {
            "Content-Type":"application/json",
            "Authorization": auth.currentUser.uid    // 👈 send UID here!
        },
        body: JSON.stringify({name_color:nameColor})
    })
    .then(() => {user.style.color = nameColor});
}
function changeBiogColor(biogColor){
    fetch("/my-page", {
        method:"POST",
        headers: {
            "Content-Type":"application/json",
            "Authorization": auth.currentUser.uid    // 👈 send UID here!
        },
        body: JSON.stringify({biog_color:biogColor})
    })
    .then(() => {biog.style.color = biogColor});
}
/***************** ***************/
/***************** ***************/
/* CHANGING MARGINS!!!*/
/***************** ***************/
/***************** ***************/

function moveName(direction){
    if(direction=="right")
        currentDirect = window.getComputedStyle(user).right;
    if(direction=="left")
        currentDirect = window.getComputedStyle(user).right;
    if(direction=="up")
        currentDirect = window.getComputedStyle(user).top;
    if(direction=="bottom")
        currentDirect = window.getComputedStyle(user).top;

    currentDirect = currentDirect.slice(0,-2);

    if(direction=="right"){
        console.log(direction);
        currentDirect = Number(currentDirect) - 10;
        console.log(currentDirect);
        user.style.right = currentDirect + "px";
    }
    if(direction=="left"){
        console.log(direction);
        currentDirect = Number(currentDirect) + 10;
        console.log(currentDirect);
        user.style.right = currentDirect + "px";
    }
    if(direction=="up"){
        console.log(direction);
        currentDirect = Number(currentDirect) - 10;
        console.log(currentDirect);
        user.style.top = currentDirect + "px";
    }
    if(direction=="bottom"){
        console.log(direction);
        currentDirect = Number(currentDirect) + 10;
        console.log(currentDirect);
        user.style.top = currentDirect + "px";
    }
}

function moveBiog(direction){
    if(direction=="right")
        currentDirect = window.getComputedStyle(biog).right;
    if(direction=="left")
        currentDirect = window.getComputedStyle(biog).right;
    if(direction=="up")
        currentDirect = window.getComputedStyle(biog).top;
    if(direction=="bottom")
        currentDirect = window.getComputedStyle(biog).top;

    currentDirect = currentDirect.slice(0,-2);

    if(direction=="right"){
        console.log(direction);
        currentDirect = Number(currentDirect) - 10;
        console.log(currentDirect);
        biog.style.right = currentDirect + "px";
    }
    if(direction=="left"){
        console.log(direction);
        currentDirect = Number(currentDirect) + 10;
        console.log(currentDirect);
        biog.style.right = currentDirect + "px";
    }
    if(direction=="up"){
        console.log(direction);
        currentDirect = Number(currentDirect) - 10;
        console.log(currentDirect);
        biog.style.top = currentDirect + "px";
    }
    if(direction=="bottom"){
        console.log(direction);
        currentDirect = Number(currentDirect) + 10;
        console.log(currentDirect);
        biog.style.top = currentDirect + "px";
    }
}


dragElement(write);
dragElement(colors);
dragElement(margin);
dragElement(templates);

function dragElement(elmnt) {
var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
if (document.getElementById(elmnt.id+"headbar")) {
    /* if present, the header is where you move the DIV from:*/
    document.getElementById(elmnt.id+"headbar").onmousedown = dragMouseDown;
} else {
    /* otherwise, move the DIV from anywhere inside the DIV:*/
    elmnt.onmousedown = dragMouseDown;
}

function dragMouseDown(e) {
    e = e || window.event;

    // Don't start dragging if the target is a <select> or inside one
    if (e.target.tagName === "SELECT" || e.target.closest("select")) {
        return;
    }

    e.preventDefault();
    pos3 = e.clientX;
    pos4 = e.clientY;
    document.onmouseup = closeDragElement;
    document.onmousemove = elementDrag;
}

function elementDrag(e) {
    e = e || window.event;
    e.preventDefault();
    // calculate the new cursor position:
    pos1 = pos3 - e.clientX;
    pos2 = pos4 - e.clientY;
    pos3 = e.clientX;
    pos4 = e.clientY;
    // set the element's new position:
    elmnt.style.top = (elmnt.offsetTop - pos2) + "px";
    elmnt.style.left = (elmnt.offsetLeft - pos1) + "px";
}

function closeDragElement() {
    /* stop moving when mouse button is released:*/
    document.onmouseup = null;
    document.onmousemove = null;
}
}


/* MOVES TO FRONT */
write.addEventListener('mousedown', (ev) => {
    write.style.zIndex = 3;
    colors.style.zIndex = 2;
    margin.style.zIndex = 2;
    templates.style.zIndex = 2;
})
colors.addEventListener('mousedown', (ev) => {
    colors.style.zIndex = 3;
    write.style.zIndex = 2;
    margin.style.zIndex = 2;
    templates.style.zIndex = 2;
})
margin.addEventListener('mousedown', (ev) => {
    colors.style.zIndex = 2;
    write.style.zIndex = 2;
    margin.style.zIndex = 3;
    templates.style.zIndex = 2;
})
templates.addEventListener('mousedown', (ev) => {
    colors.style.zIndex = 2;
    write.style.zIndex = 2;
    margin.style.zIndex = 2;
    templates.style.zIndex = 3;
})


function templatesPop(){
    templates.style.display = "block";
}

function templatesCloser(){
    templates.style.display = "none";
}

function centre(){
    console.log("it works");
    document.getElementById("user").style.left = "40%"
    document.getElementById("biog").style.left = "43%"
  }

function changeBox1Name(value){
    box1Text.textContent = value;
    if(value=="serviceHours")
        box1Text.textContent = "Service Hours";
}
function changeBox2Name(value){
    box2Text.textContent = value;
    if(value=="serviceHours")
        box2Text.textContent = "Service Hours";
}
function changeBox3Name(value){
    box3Text.textContent = value;
    if(value=="serviceHours")
        box3Text.textContent = "Service Hours";
}
function changeBox4Name(value){
    box4Text.textContent = value;
    if(value=="serviceHours")
        box4Text.textContent = "Service Hours";
}
function changeBox5Name(value){
    box5Text.textContent = value;
    if(value=="serviceHours")
        box5Text.textContent = "Service Hours";
}
function changeBox6Name(value){
    box6Text.textContent = value;
    if(value=="serviceHours")
        box6Text.textContent = "Service Hours";
}

function templatesChange(value){
    if(value =="1"){
        user.style.left = "40%";
        biog.style.left = "45%";

        box1.style.width = "30%";
        box1.style.height = "49%";
        box1.style.left = "0%";
        box1.style.bottom = "51%";

        box2.style.width = "30%";
        box2.style.height = "50.5%";
        box2.style.left = "70%";
        box2.style.bottom = "0%";

        box3.style.width = "40%";
        box3.style.height = "50.5%";
        box3.style.left = "30%";
        box3.style.bottom = "0%";

        box4.style.width = "30%";
        box4.style.height = "49%";
        box4.style.left = "70%";
        box4.style.bottom = "51%";

        box5.style.width = "30%";
        box5.style.height = "50.5%";
        box5.style.left = "70%";
        box5.style.bottom = "0%";

        box6.style.width = "0%";
        box6.style.height = "0%";
        box5.style.left = "0%";
        box5.style.bottom = "0%";
    }
    if(value =="2"){
        user.style.left = "10%";
        biog.style.left = "15%";

        box1.style.width = "30%";
        box1.style.height = "33%";
        box1.style.left = "40%";
        box1.style.bottom = "67%";

        box2.style.width = "30%";
        box2.style.height = "33%";
        box2.style.left = "70%";
        box2.style.bottom = "67%";

        box3.style.width = "30%";
        box3.style.height = "33%";
        box3.style.left = "40%";
        box3.style.bottom = "33.5%";

        box4.style.width = "30%";
        box4.style.height = "33%";
        box4.style.left = "70%";
        box4.style.bottom = "33.5%";

        box5.style.width = "30%";
        box5.style.height = "33%";
        box5.style.left = "40%";
        box5.style.bottom = "0%";

        box6.style.width = "30%";
        box6.style.height = "33%";
        box6.style.left = "70%";
        box6.style.bottom = "0%";
        
    }
    if(value =="3"){
        user.style.left = "40%";
        biog.style.left = "45%";

        box1.style.width = "33%";
        box1.style.height = "33%";
        box1.style.left = "0%";
        box1.style.bottom = "33%";

        box2.style.width = "33%";
        box2.style.height = "33%";
        box2.style.left = "0%";
        box2.style.bottom = "0%";

        box3.style.width = "34%";
        box3.style.height = "33%";
        box3.style.left = "33%";
        box3.style.bottom = "33%";

        box4.style.width = "34%";
        box4.style.height = "33%";
        box4.style.left = "33%";
        box4.style.bottom = "0%";

        box5.style.width = "33%";
        box5.style.height = "33%";
        box5.style.left = "67%";
        box5.style.bottom = "33%";

        box6.style.width = "33%";
        box6.style.height = "33%";
        box6.style.left = "67%";
        box6.style.bottom = "0%";
    }
}

function changeBox1Color(value){
    box1.style.borderColor = value;
    box1Text.style.color = value;
}
function changeBox2Color(value){
    box2.style.borderColor = value;
    box2Text.style.color = value;
}
function changeBox3Color(value){
    box3.style.borderColor = value;
    box3Text.style.color = value;
}
function changeBox4Color(value){
    box4.style.borderColor = value;
    box4Text.style.color = value;
}
function changeBox5Color(value){
    box5.style.borderColor = value;
    box5Text.style.color = value;
}
function changeBox6Color(value){
    box6.style.borderColor = value;
    box6Text.style.color = value;
}
