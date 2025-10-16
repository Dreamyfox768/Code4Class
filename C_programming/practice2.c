int get_input();
int display(int val);

int main(){
int input = get_input();
int divisible = display(input);
if (divisible == 1){
printf("%d is divisible by 9\n", input);
}
else{
printf("%d is not divisible by 9\n", input);
}
}

int get_input()
{
int num1;
printf("Enter an integer[1,999999]:");
scanf("%d", &num1);
while (num1 <= 1 ||num1 >= 999999)
{
printf("Invalid input. Try again.\n");
printf("Enter an integer[1,999999]:");
scanf("%d", &num1);
}
return num1;
}

int display(int val){
int sum;
int a;
sum =0;
int numbers;
for ( a = val; a >0; a /= 10) {
numbers = a % 10;
printf("%d\n", numbers);
sum += numbers;
}
if (sum % 9 == 0){
return 1;
}
else{
return 0;
}
}
