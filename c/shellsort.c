#include<stdio.h>
#define MAX 100
int main()
{
	int a[MAX],i,j,k,n,in;
	printf("enter the no of elements:\n");
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
	printf("Enter in value:\n");
	scanf("%d",&in);
	while(in>=1)
	{
		for(i=in;i<n;i++)
		{
			k=a[i];
			for(j=i-in;j>=0;j=j-in)
			{
				if(k<a[j])
				a[j+in]=a[j];
				else
				break;
			}
			a[j+in]=k;
		}
		in=in-2;
	//	printf("in value%d",in);
	}
	printf("sorted list is:\n");
	for(i=0;i<n;i++)
	printf("%d ",a[i]);
	printf("\n");
}
