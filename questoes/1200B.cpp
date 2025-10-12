#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<ll,ll> pii;
#define pb push_back
#define read_vec(v,n) for(int i = 0; i < n; i++) cin >> v[i]

void solve(){
    int n, m , k; cin >> n >> m >> k;
    vector<int> v(n);
    read_vec(v, n);

    for (int i = 0; i < n - 1; i++){
        int need = max(0, v[i + 1] - k);
        m += v[i] - need;
        if (m < 0){
            cout << "NO" << endl;
            return;
        } 
    }

    cout << "YES" << endl;
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    int t; cin >> t;
    while (t--){
        solve();
    }

    return 0;
}