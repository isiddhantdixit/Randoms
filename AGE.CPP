#include<stdio.h>
#include<conio.h>
  void main()
    {
    int age;
    clrscr();
    printf("Enter your age");
    scanf("%d",&age);
    if(age<18)
     printf("Minor");
      else
       {
	 if(age>45)
	 printf("adult");
	else
	 {
	 if(age>18)
       printf("Major");
       else

       printf("Adult");
       }
    }
    getch();
    }