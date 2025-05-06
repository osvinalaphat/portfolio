const firebaseConfig = {
    //I got this from the firebase Console
    apiKey: "AIzaSyBScCHQRvwumXBR9Ef1Z0cdhdmc9BexuG4",
    authDomain: "portfolio-d5c42.firebaseapp.com",
    projectId: "portfolio-d5c42",
    storageBucket: "portfolio-d5c42.firebasestorage.app",
    messagingSenderId: "893202911708",
    appId: "1:893202911708:web:17c379569b9dee2dbdff19",
    measurementId: "G-BWKCMW42G6"
};


const app = firebase.initializeApp(firebaseConfig); //initialize firebase
const auth = firebase.auth(); //login and signup functions
const analytics = firebase.analytics(); //tracks usage across the website

window.signup = function(){
    const email = document.getElementById("signup-email").value;
    const password = document.getElementById("signup-password").value;
    
    auth.createUserWithEmailAndPassword(email, password)
        .then((userCredential) => {
            alert("Signup successful!");
            loadMyPage();
        })
        .catch((error) => {
            console.error("Signup error:", error);
            alert("Error " + error.message);
        });
}

window.login = function(){
    const email = document.getElementById("login-email").value;
    const password = document.getElementById("login-password").value;

    console.log("Starting login process...");
    
    auth.signInWithEmailAndPassword(email, password)
        .then((userCredential) => {
            alert("Login successful!");
            loadMyPage();
        })
        .catch((error) => {
            alert("Error: " + error.message);
        });
}
async function loadMyPage() {
    const response = await fetch("/my-page", {
        method: "GET",
        headers: {
            "Authorization": auth.currentUser.uid  // 👈 same, sending UID in header
        }
        
    });
    
    
    const data = await response.json();
    
    // Now update your page with the saved data:
    user.textContent = `${data.title}'s Portfolio`;
    biog.textContent = data.biog;
    document.body.style.backgroundColor = data.background_color;
    user.style.color = data.name_color;
    biog.style.color = data.biog_color;
    portfolio.style.display="block";
    signlogin.style.display="none";
}

