#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<ll,ll> pii;
#define pb push_back
#define read_vec(v,n) for(int i = 0; i < n; i++) cin >> v[i]

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    int n; cin >> n;
    vector<pair<int,int>> v; 

    for (int i = 1; i < n + 1; i++) {
        int x; cin >> x;
        v.pb({x, i});
    }
    sort(v.begin(), v.end());

    ll out = 0;
    for (int i = 0; i < n - 1; i++){
        out += abs(v[i].second - v[i+1].second);
    }
    cout << out << "\n";

    return 0;
}