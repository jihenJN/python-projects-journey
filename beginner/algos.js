var month = prompt("Enter the month");
var result = "";
if (month) {
  switch (month) {
    case "january":
    case "march":
    case "may":
    case "july":
    case "october":
    case "december":
      result = `${month} has 31 days`;
      break;
    case "february":
      var year = prompt("Enter the year");
      year % 4 == 0
        ? (result = `${month} has 29 days`)
        : (result = `${month} has 28 days`);
      break;
    case "april":
    case "june":
    case "august":
    case "september":
    case "november":
      result = `${month} has 30 days`;
      break;
    default:
      result = `${month} is not valid month`;
  }
  document.getElementById("output").textContent = result;
}
