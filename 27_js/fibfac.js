//Team Margie :: Margie Cao, Jayden Zhang
//SoftDev pd5
//K27 - Basic functions in JavaScript
//2025-01-06m

//JavaScript implementations of Day0 recursive Scheme functions

//factorial:

//<your team's fact(n) implementation>
function fact(n) {
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
function fib(n) {
  if (n == 1) {
    return 1;
  }
  if (n == 2) {
    return 1;
  }
  else {
    return fib(n-2) + fib(n-1)
  }
}

//TEST CALLS
// (writing here can facilitate EZer copy/pasting into dev console now and later...)
fib(1)
fib(2)
fib(3)
fib(10)
fib(15)
//=================================================================
