#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<ll,ll> pii;
#define pb push_back
#define read_vec(v,n) for(int i = 0; i < n; i++) cin >> v[i]

void solve(){
    int n, m; cin >> n >> m;
    string x, s; cin >> x >> s;
    
    int ans = -1;
    string cur = x;

    for (int i = 0; i <= 11; i++) {
        if (cur.find(s) != string::npos) {
            ans = i;
            break;
        }
        if ((int)cur.size() > 2 * m + n) break;
        cur += cur;
    }

    cout << ans << "\n";
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    int t; cin >> t;
    while(t--){
        solve();
    }
    return 0;
}
