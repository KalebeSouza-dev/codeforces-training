#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<ll,ll> pii;
#define pb push_back
#define read_vec(v,n) for(int i = 0; i < n; i++) cin >> v[i]

ll mdc(ll a, ll b) {
    while (b != 0) {
        ll resto = a % b;
        a = b;
        b = resto;
    }
    return a;
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL);

    ll x, y, a, b; cin >> x >> y >> a >> b;
    ll mm = x * y / mdc(x, y);
    
    cout << (b /mm ) - ((a - 1) / mm) << endl;

    return 0;
}