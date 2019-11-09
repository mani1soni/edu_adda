
1215 C - Swap Letters.cpp GNU C++14 Accepted
///==================================================///

	///

	///  Ir0nic_  ///

    ///  MEHUL BHUTALIA  ///

	/// Indian Institute Of Information Technology and Management,Gwalior.  ///

	///

///==================================================///

#include<bits/stdc++.h>

#define     T()                 ll tt;    cin>>tt;        while(tt--)

#define     ll                  long long

#define     vi                  vector<ll>

#define     pii                 pair<ll,ll>

#define     vpair               vector< pii >

#define     fast                ios_base::sync_with_stdio(false),cin.tie(0),cout.tie(0);

#define     repp(i,a,n)         for(ll i= a ; i < n ; ++i)

#define     rep(i,n)            for(ll i= 0 ; i < n ; ++i)

#define     p_b                 push_back

#define     p_f                 push_front

#define     pop_b               pop_back()

#define     pop_f               pop_front()

#define     m_p                 make_pair

#define      sumv(v)            accumulate(v.begin(),v.end(),0);

#define     sortv(v)            sort(v.begin(),v.end())

#define     sort_dec(v)         sort(v.begin(),v.end(),greater<ll>() )

#define     l_b(v,l)            lower_bound (v.begin(), v.end(), l)

#define     u_b(v,l)            upper_bound (v.begin(), v.end(), l)

#define     pq                  priority_queue

#define     ff                  first

#define     ss                  second

#define     len                 length()

#define     all(v)              v.begin(),v.end()

#define     mset(a,b)           memset(a,b,sizeof(a));



///==========INPUT=============///

#define     sc(a)           cin>>a;

#define     sc2(a,b)        cin>>a>>b;

#define     sc3(a,b,c)      cin>>a>>b>>c;

#define     sc4(a,b,c,d)    cin>>a>>b>>c>>d;



///==========PRINTING=============///

#define     prarr(arr)      rep(i,sizeof(arr)/sizeof(ll)) cout<<arr[i]<<" "; nl

#define     prvec(v)        rep(i,v.size()) cout<<v[i]<<" "; nl

#define     pr(x)           cout<<x<<"\n";

#define     pr2(x, y)       cout<<x<<" "<<y<<"\n";

#define     pr3(x, y, z)    cout<<x<<" "<<y<<" "<<z<<"\n";



///==========DEBUGGING=============///

#define     debug(a)            cout<<"*"<<a<<endl;

#define     debug2(a,b)         cout<<"$"<<a<<" "<<b<<endl;

#define     debug3(a,b,c)       cout<<"$"<<a<<" "<<b<<" "<<c<<endl;

#define     bug                 cout<<"#"<<endl;

#define     nl                  cout<<'\n';

#define     endl                '\n'



///==========CONSTANTS=============///

#define     max6     1000005

#define     max5     100004

#define     max4     10003

#define     mod      1000000007

#define     inf      1e18

ll powermod(ll _a,ll _b,ll _m)    {ll _r=1;while(_b){if(_b%2==1)_r=(_r*_a)%_m;_b/=2;_a=(_a*_a)%_m;}return _r;}

using namespace std;



int main()

{

    fast

    ll n;

    sc(n)

    string s1,s2;

    cin>>s1>>s2;

    ll c=0;

    rep(i,s1.len)

    {

        if(s1[i]!=s2[i])

            c++;

    }

    if(c%2==0)

    {

        vi v1,v2;

        for(ll i=0;i<n;i++)

        {

            if(s1[i]!=s2[i])

            {

                if(s1[i]=='a')

                {

                    v1.p_b(i+1);

                }

                else

                    v2.p_b(i+1);

            }

        }



        if(v1.size()%2==0)

        {

            pr((v1.size()+v2.size())/2)

            for(ll i=0;i<v1.size();i+=2)

                pr2(v1[i],v1[i+1])

            for(ll i=0;i<v2.size();i+=2)

                pr2(v2[i],v2[i+1])



        }

        else

        {

            pr((v1.size()+v2.size())/2+1)

            ll aa=v1[v1.size()-1];

            ll bb=v2[v2.size()-1];

            pr2(aa,aa)

            pr2(aa,bb)

            for(ll i=0;i<v1.size()-1;i+=2)

                pr2(v1[i],v1[i+1])

            for(ll i=0;i<v2.size()-1;i+=2)

                pr2(v2[i],v2[i+1])

        }

    }

    else

        pr(-1)

}
