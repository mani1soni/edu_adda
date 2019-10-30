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
