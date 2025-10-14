
#include <stdio.h>

int main(){
int number; // initializing integer
printf("Enter an integer: "); // giving user a prompt
scanf("%d", &number); // asking user for integer
if (number < 0)
  if (number%2 == 0) // creating a nested loop if number is pos or odd /positive even and same with zero
    {
      printf("%d is negative.\n", number);
      printf("The number %d is Even", number);
    }
  else
    {
      printf("%d is negative.\n", number);
      printf("The number %d is Even", number);
    }
else if (number > 0 )
  if (number%2 == 0)
  {
    printf("%d is Positive.\n", number);
    printf("The number %d is Even", number);
  }
  else
  {
    printf("%d is Positive.\n", number);
    printf("The number %d is Odd", number);
  }
else
  {
  printf("%d is Zero\n", number);
  }
return 0 ; //return output
}
