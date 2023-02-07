#include<bits/stdc++.h>
using namespace std;

int crc(char *ip,char *op,char *poly,int mode)
{
	strcpy(op,ip);
	if(mode)
	{
		for(int i=1;i<strlen(poly);i++)
		{
			strcat(op,"0");
		}
	}
	
	//xor
	for(int i=0;i<strlen(ip);i++)
	{
		if(op[i]=='1')
		{
			for(int j=0;j<strlen(poly);j++)
			{
				if(op[i+j]==poly[j])
				op[i+j]='0';
				
				else
				op[i+j]='1';
				
			}
		}
	}	
	
	for(int i=0;i<strlen(op);i++)
	{
		if(op[i]=='1')
		return 0;
	}
	return 1;
}

int main()
{
	char ip[50],op[50],recv[50];
	char poly[]="10011";
	cout<<"Enter the input in binary\n";
	cin>>ip;
	crc(ip,op,poly,1);
	cout<<"Transmitted message: "<<ip<<op+strlen(ip)<<endl;
	cout<<"\nEnter received msg in binary\n";
	cin>>recv;
	if(crc(recv,op,poly,0))
	cout<<"No error\n";
	else
	cout<<"Error\n";
	return 0;
}
