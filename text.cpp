#include<bits/stdc++.h>

using namespace std;

bool pri[1000001];

void prime()
{
    
    memset(pri,true,sizeof(pri));
    
    for(int i=2;i*i<=1000001;i++)
    
    {
        
        if(pri[i])
            
        {
            
            for(int j=i*i;j<=1000001;j+=i)
            
            pri[j]=false;
            
        }
        
        
        
    }
    
    pri[0]=pri[1]=false;
    
    return;
    
}

string solve (int N)

{
    
    if(N<=2)
        
        return "No";
    
    if(N%2==0)
        
        return"Yes";
    
    else if(pri[N])
        
        return "No";
    
    else
        
        return"Yes";
    
}




int main() {
    
    
    
    
    ios::sync_with_stdio(0);
    
    cin.tie(0);
    
    prime();
    
    int T;
    
    cin >> T;
    
    for(int t_i=0; t_i<T; t_i++)
    
    {
        
        int N;
        
        cin >> N;
        
        
        
        
        string out_;
        
        out_ = solve(N);
        
        cout << out_;
        
        cout << "\n";
        
    }
    
}
