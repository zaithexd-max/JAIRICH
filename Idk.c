#include<stdio.h>
#include<stdbool.h>
#include<string.h>
int main(){
char noun[50] = "";
char verb[50] = "";
char adjective1[50] = "";
char adjective2[50] = "";
char adjective3[50] = "";
printf("Enter an adjective (description): ");
fgets(adjective1,sizeof(adjective1),stdin);
adjective1[strcspn(adjective1,"\n")] = '\0';

printf("Enter an noun (animal or person): ");
fgets(noun,sizeof(noun),stdin);
noun[strcspn(noun,"\n")] = '\0';

printf("Enter an adjective2 (description): ");
fgets(adjective2,sizeof(adjective2),stdin);
adjective2[strcspn(adjective2,"\n")] = '\0';

printf("Enter an verb (description): ");
fgets(verb,sizeof(verb),stdin);
verb[strcspn(verb,"\n")] = '\0';

printf("Enter an adjective3 (description): ");
fgets(adjective3,sizeof(adjective3),stdin);
adjective3[strcspn(adjective3,"\n")] = '\0';

printf("\n\n\nToday I went to a %s Zoo",adjective1);
printf("\nI %s %s",verb,noun);
printf("\nI want to clap him %s",adjective2);
printf("\nI done it %s",adjective3);




  /*
char item[50] = "";
int quantity = 0;
float price = 0.0f;

printf("What item would you like to buy: ");
fgets(item,sizeof(item),stdin);
item[strcspn(item, "\n")] = '\0';//replace the \n in item array with \0 Therefore,it doesnt create new line.
printf("How much is it: ");
scanf("%f",&price);
printf("How many would you like?: ");
scanf("%d",&quantity);
printf("\nYou have bought %d %s",quantity,item);
float Total = quantity*price;
printf("\nTotal price: $%.2f",Total);*/
  /*
  int age = 25;
  float gpa = 2.5;
  float temp = -19.99;
  printf("Youre %d years old\n",age);
  printf("Your gpa is %.1f\n",gpa);
  printf("The temp is %.2f°F",temp);
  double pie = 3.14159265358979;
  printf("%.15f",pie);
  char grade = 'A';
  printf("%c",grade);
  char name[]="Nigga";
  printf("%s\n",name);
  printf("Youre my %s",name);
  bool isOnline = true;
  bool isStudent = false;
  if(isOnline || isStudent){
    printf("Online\n");
  }else{
    printf("Offline\n");
  }
  printf("%d",isOnline);
  float price1 = 19.99;
  float price2 = 142.50;
  float price3 = -100.25;

  printf("%+06.1f\n",price1);
  printf("%+06.1f\n",price2);
  printf("%+06.1f\n",price3);
  int  x = 10;
  int y = 3;
  int z= 0;
  //z = x/y;
  z = x % y;
  x++;
  printf("%d",x);*/
  /*
  int age = 0;
  float gpa = 0.0f;
  char grade = '\0';
  char name[30] = "";
  float num1 = 0.0f;
  float num2 = 0.0f;
  char sign = '\0';
  printf("Enter first number: ");
  scanf("%f",&num1);
  getchar();
  printf("Enter the sign: ");
  scanf("%c",&sign);
  printf("Enter second number: ");
  scanf("%f",&num2);
  if(sign == '+'){
    float num3 = num1 + num2;
    printf("%f",num3);
  }else if (sign == '-'){
    float num3 = num1 - num2;
    printf("%f",num3);
  }else if (sign == '*'){
    float num3 = num1*num2;
    printf("%f",num3);
  }else if (sign == '/'){
    float num3 = num1/num2;
    printf("%f",num3);
  }
  */
  /*
  printf("Enter Your Gpa: ");
  scanf("%f",&gpa);
  if(gpa < 4){
    printf("Womp womp grade F students");
  }else{
    printf("Nah aint no way ");
  }
*/
  /*
  
  printf("Enter your age:");
  scanf("%d",&age);

  printf("Enter your gpa:");
  scanf("%f",&gpa);

  printf("Enter your grade:");
  scanf(" %c",&grade);
  getchar();
  printf("Enter your full name:");
  fgets(name,sizeof(name),stdin);
  name[strlen(name)-1]='\0';

  printf("\n\n\n");
  printf("Result:\n");
  printf("Your age is %d\n",age);
  printf("Your gpa is %.2f\n",gpa);
  printf("Your Grade is %c\n",grade);
  printf("Your full name is %s\n",name);
  return 0;
  
*/
}