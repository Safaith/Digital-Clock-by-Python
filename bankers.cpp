// 13 4
// 7 0 1 2 0 3 0 4 2 3 0 3 2
#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n, capacity;
    cin >> n >> capacity;
    vector<int> v(n);
    for (auto &i : v)
        cin >> i;

    set<int> s;
    map<int, int> mp;
    int fault_cnt = 0;
    for (int i = 0; i < n; i++)
    {
        if (s.count(v[i]) == 0)
        {
            fault_cnt++;
            if (s.size() == capacity)
            {
                int ind = INT_MAX, val;
                for (auto &j : s)
                {
                    if (mp[j] < ind)
                    {
                        ind = mp[j];
                        val = j;
                    }
                }
                s.erase(val);
            }
            s.insert(v[i]);
        }
        mp[v[i]] = i;
    }
    cout << fault_cnt << endl;
    return 0;
}
