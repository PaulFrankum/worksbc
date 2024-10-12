const fullName = "  john doe  ";
const formattedName = fullName
  .trim()
  .split(" ")
  .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
  .join(" ");
console.log(formattedName); // Outputs: "John Doe"

// initals

const formattedName2 = fullName
  .trim()
  .split(" ")  
  .map((word) => word.charAt(0).toUpperCase())
  .join("");
  console.log(formattedName2); // Outputs: "JD"

// change Name to surname, Firstname

const formattedName3 = formattedName
  .split(" ")
  .reverse()
  .join(', ')
  console.log(formattedName3); // Outputs: "Doe, John"

// repeat name

let result = formattedName.repeat(4);
console.log(result)


// change name from John to David
const formattedName4 = formattedName.replace("John","David");
console.log(formattedName4); // Outputs: "David Doe

// change o to z
const formattedName5 = formattedName.replaceAll("o","z");
console.log(formattedName5); // Outputs: Jzhn Dze

// show four letter
const formattedName6 = formattedName.at(3);
console.log(formattedName6); // Outputs: show 4 letter

