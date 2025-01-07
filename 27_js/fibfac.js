//Team Margie :: Margie Cao, Jayden Zhang
//SoftDev pd5
//K27 - Basic functions in JavaScript
//2025-01-06m

//JavaScript implementations of Day0 recursive Scheme functions

//factorial:

//<your team's fact(n) implementation>
let fact = function(n) {
  if (n == 1) {
    return 1;
  }
  else {
    return n * (fact(n-1));
  }
}

//TEST CALLS
// (writing here can facilitate EZer copy/pasting into dev console now and later...)
fact(1) // 1
fact(5) // 120
fact(10) // 3628800

//-----------------------------------------------------------------


//fib:

//<your team's fib(n) implementation>
let fib = function(n) {
  if (n == 1) {
    return 1;
  }
  else if (n == 2) {
    return 1;
  }
  else {
    return fib(n-2) + fib(n-1)
  }
}

//TEST CALLS
// (writing here can facilitate EZer copy/pasting into dev console now and later...)
fib(1) // 1
fib(2) // 1
fib(3) // 2
fib(5) // 5
fib(10) // 55
//=================================================================