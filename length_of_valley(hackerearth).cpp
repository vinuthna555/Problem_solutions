#include <iostream>
 
using namespace std;
void func(long int arr[],long int n)
{
	
	long int ans1[1000000];
	ans1[0]=0;
	long int ans2[1000000];
	ans2[n-1]=0;
	for(long int i=1;i<n;i++)
	{
		if(arr[i-1]>arr[i])
		ans1[i]=ans1[i-1]+1;
		else
		ans1[i]=0;
 
	}
	for(long int i=n-2;i>=0;i--)
	{
		if(arr[i]<arr[i+1])
		ans2[i]=ans2[i+1]+1;
		else
		ans2[i]=0;
	}
	for(long int i=0;i<n;i++)
	cout<<ans1[i]+ans2[i]+1<<" ";
	cout<<endl;
}
int main() {
	long int t;
	cin >> t;
	while(t--)
	{
		long int n,arr[1000000];
		cin>>n;
		for(long int i=0;i<n;i++)
		cin>>arr[i];
		func(arr,n);
	}			
 
	return 0;
}
