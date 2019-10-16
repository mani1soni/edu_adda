#include<stdio.h>
int main()
{
	int i,j,temp,n,a[50];
	printf("Enter no of elements\n");
	scanf("%d",&n);
	printf("Enter elements in array\n");
	for(i=0;i<n;i++)
	scanf("%d",&a[i]);
	for(i=1;i<n;i++)
	{
		temp=a[i];
		for(j=i-1;j>=0;j--)
		{
			if(a[j]>temp)
			{
				a[j+1]=a[j];
			}
			else
			{
				break;
			}
		}
		a[j+1]=temp;
	}
	printf("the sorted array is :\n");
	for(i=0;i<n;i++)
	printf("%d ",a[i]);
}
