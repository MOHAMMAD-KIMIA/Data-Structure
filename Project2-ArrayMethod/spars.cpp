#include<iostream>
using namespace std;

int c=0;
int list[50][3];
int f(int m[50][50],int n)
{
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++)
		{
			if(m[i][j]!=0)
			{
				list[c][0]=i;
				list[c][1]=j;
				list[c][2]=m[i][j];
				c++;
			}
		}
	}
}