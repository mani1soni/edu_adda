void decimalToBinary(number){
  int c,k;
  for (c = 31; c >= 0; c--)
    {
      k = number >> c;
      if (k & 1)
        printf("1");
      else
        printf("0");
    }
}
