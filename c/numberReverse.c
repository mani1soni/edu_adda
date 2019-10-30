int numberReverse(number){
  int reverse = 0;
  while (number != 0)
  {
    reverse = reverse * 10;
    reverse = reverse + n%10;
    n = n/10;
  }
  return reverse;
}


//Using recursion method

long numberReverse(long number) {
   static long reverse = 0;
   
   if (number == 0)
      return 0;
   
   reverse = reverse * 10;
   reverse = reverse + number % 10;
   numberReverse(number/10);
   return reverse;
}
