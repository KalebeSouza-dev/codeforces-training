#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<ll,ll> pii;
#define pb push_back
#define read_vec(v,n) for(int i = 0; i < n; i++) cin >> v[i]

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    int n, v; cin >> n;
    int i = 0, ii = 0, iii = 0;
    bool f = true;

    for (int j = 0; j < n; j ++){
        cin >> v;
        // cout << v << endl;
        // cout << i << ii << iii << endl;

        if (j == 0 && v != 25){
            f = false;
            i++;
            break;
        } 

        if (v == 25) {
            i ++;
            continue;
        } else if (v == 50){
            ii ++;
            if (i == 0){
                f = false;
                break; 
            } else {
                i--;
            }  
        } else {
            if (ii > 0 && i > 0){
                i --;
                ii --;
            } else if (i >= 3){
                i -= 3;
            } else {
                f = false;
                break; 
            }
            iii ++;
        }
    }

    if (f) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }

    return 0;
}