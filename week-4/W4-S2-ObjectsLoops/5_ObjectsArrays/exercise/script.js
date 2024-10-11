// create your coffee object array here
var orders1 = {customer: "Alice", Coffee: "latte", Milk: " Yes",};
var orders2 = {customer: "Bob", Coffee: "cortado", Milk: " No",};
var orders3 = {customer: "Charlie", Coffee: "flat white", Milk: " Yes",};

const orders = [orders1, orders2, orders3]

// create your print order function here

for (let i = 0; i < orders.length; i++)  {
    console.log("Name " + orders[i].customer + " is " + orders[i].Coffee+" Milk " + orders[i].Milk);
}