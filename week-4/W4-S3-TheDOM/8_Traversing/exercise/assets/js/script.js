
var listEl = document.querySelectorAll("li");
if (listEl) {
     for(element of listEl) {
      element.style = "color: Blue;";
     };  
    }

var h2El = document.querySelector(".widget h2");
if (h2El) {
     h2El.textContent = "Reports";
     }

var pEl = document.querySelectorAll("p");
if (h2El) {
    h2El[2].textContent = "Optimise performance metrics here.";
    }

