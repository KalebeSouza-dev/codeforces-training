#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<ll,ll> pii;
#define pb push_back
#define read_vec(v,n) for(int i = 0; i < n; i++) cin >> v[i]

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    int n, c; cin >> n >> c;
    int ma = 0;
    vector<int> d(n);
    read_vec(d, n);
    for (int i = 0; i < n - 1; i++){
        if (d[i] - d[i + 1] > ma) ma = d[i] - d[i + 1];
    }
    cout << max(ma - c, 0) << endl;

    return 0;
}