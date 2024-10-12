// TODO: Add 2 new items to the sidebar called "Register" and "Help".

var sbEl = document.querySelector("ul");

var nsbEl = document.createElement("li");
nsbEl.textContent = "Register";
// sbEl.appendChild(nsbEl);

var nsbEl = document.createElement("li");
nsbEl.textContent = "Help";

sbEl.appendChild(nsbEl);

// TODO: MEGA CHALLENGE: can you add the Help link between Reports and Settings?

var nsb2El = document.createElement("li");
nsb2El.textContent = "Help";

sbEl.insertBefore(nsb2El, sbEl.childNodes[6]);
