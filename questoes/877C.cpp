#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<ll,ll> pii;
#define pb push_back
#define read_vec(v,n) for(int i = 0; i < n; i++) cin >> v[i]

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    int n; cin >> n;
    vector<int> impar, par, out;
    for (int i = 1; i < n + 1; i++){
        if (i % 2 == 0){
            par.pb(i);
        } else {
            impar.pb(i);
        }
    }
    out.insert(out.end(), par.begin(), par.end());
    out.insert(out.end(), impar.begin(), impar.end());
    out.insert(out.end(), par.begin(), par.end());

    cout << out.size() << endl;
    for (int i = 0; i < out.size(); i++){
        cout << out[i] << " ";
    }
    cout << "\n";

    return 0;
}