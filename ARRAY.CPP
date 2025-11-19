#include<stdio.h>
#include<conio.h>
   void main()
      {
      int x[6];
      int i;
      int great;
      clrscr();
      printf("Enter six value.....");
      for(i=0;i<=5;i++)
	{
	scanf("%d\n",&x[i]);
	}
	great=x[0];
      printf("\nEntered six values are.....\n");
      for(i=0;i<=5;i++)
	{
	if (great < x[i])
	 great=x[i];
	 }
	printf("greatest value = %d\n",great);
	getch();
	}
