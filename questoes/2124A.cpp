#include <bits/stdc++.h>

using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while(t--){
        int n; cin >> n;
        bool f = true;
        vector<int> arr(n);
        for(auto &x : arr) cin >> x;

        for(int i = 0; i < n; i++){
            for(int j = i + 1; j < n; j++){
                if(arr[i] > arr[j]){
                    cout << "YES\n2\n";
                    cout << arr[i] << " " << arr[j] << "\n";
                    f = false;
                    break;
                }
            }
            if (not f) break;
        }

        if (f) cout << "NO\n";
    }
    return 0;
}