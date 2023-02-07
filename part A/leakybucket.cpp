#include<bits/stdc++.h>
using namespace std;
int main()
{
int bucketsize,bufsize=0,ipsize,opsize,sizeleft,queries;
cout<<"Enter the bucket size\n";
cin>>bucketsize;
cout<<"Enter the rate of packet flow \n";
cin>>opsize;
cout<<"Enter the no of queries\n";
cin>>queries;

for(int i=0;i<queries;i++)
{
	cout<<"Enter the packet size\n";
	cin>>ipsize;
	sizeleft=bucketsize-bufsize;
	if(ipsize<=sizeleft)
	{
		cout<<"Packet accepted\n";
		bufsize+=ipsize;	
	}
	else{
		cout<<"Packet dropped!\n";	
	}
	cout<<"Packet sent\n";
	bufsize-=opsize;
	cout<<"Capacity left: "<<bucketsize-bufsize<<endl;
}	
}