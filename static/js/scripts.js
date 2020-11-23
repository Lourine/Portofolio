var i = 0;
var txt = 'Lorem ipsum dummy text blabla.';
var speed = 50;
if (i < txt.length) {
    document.getElementById("demo").innerHTML += txt.charAt(i);
    i++;
    setTimeout( speed);
  }