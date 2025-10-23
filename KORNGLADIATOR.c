#include<stdio.h>
#include<stdbool.h>
#include<string.h>
int x;
char Inventory[50] = "";
int main(){
  printf("What item: ");
  fgets(Inventory,sizeof(Inventory),stdin);
  Inventory[strcspn(Inventory,"\n")] = '\0';
  printf("How many item: ");
  scanf("%i",&x);
  if(x>=10){
  x +=1;
  
  }
  printf("You have bought %i %s",x,Inventory);
 
  

  return 0;
}