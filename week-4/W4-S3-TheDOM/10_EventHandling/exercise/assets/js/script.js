// 1. use document.getElementById to select the searchTerm Button
const sEl = document.getElementById("searchTerm")
// 2. use document.getElementById to select the searchButton Button
const sbEl = document.getElementById("searchButton")
// 3. add an event listener to the searchButton that calls the search function when clicked
sbEl.addEventListener("click", search);

function search() {
// 4. use the value property of the searchInput to get the search term
const search = sEl.value
// 5. select the searches div using document.getElementById
const searches = document.getElementById("searches");
// 6. create a new li element using document.createElement
const newlist = document.createElement("li");
// 7. set the innerHTML of the new paragraph to the search term
newlist.innerHTML = search
// 8. append the new paragraph to the searches div
searches.appendChild(newlist)
document.getElementById('searchTerm').value="";


}
