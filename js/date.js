// determining date
let mydate = new Date();
let year = mydate.getYear();

if (year < 1000) year += 1900;

let day = mydate.getDay();
let month = mydate.getMonth();
let daym = mydate.getDate();
let dayarray = new Array(
  "Sunday", "Monday", "Tuesday", "Wednesday",
  "Thursday", "Friday", "Saturday"
);
let montharray = new Array(
  "January", "February", "March", "April", "May", "June", "July",
  "August", "September", "October", "November", "December"
);

document.write(
  dayarray[day] + ", " + montharray[month] + " ", + daym + ", "
  + year
);
