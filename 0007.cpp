#include <iostream>
#include <vector>
using namespace std;

vector<int> arr;
vector<int> sp;
int n;

void build(int n, int id = 1, int tl = 0, int tr = -1) {
    if (tr == -1) tr = n - 1;
    if (tl == tr) {
        sp[id] = arr[tl];
    } else {
        int m = (tl + tr) / 2;
        build(n, id * 2, tl, m);
        build(n, id * 2 + 1, m + 1, tr);
        sp[id] = sp[id * 2] + sp[id * 2 + 1];
    }
}

int sum(int l, int r, int n, int id = 1, int tl = 0, int tr = -1) {
    if (tr == -1) tr = n - 1;
    if (l > r) {
        return 0;
    }
    if (l == tl && r == tr) {
        return sp[id];
    }
    int m = (tl + tr) / 2;
    return sum(l, min(r, m), n, id * 2, tl, m) +
           sum(max(l, m + 1), r, n, id * 2 + 1, m + 1, tr);
}

void add(int i, int d, int n, int id = 1, int tl = 0, int tr = -1) {
    if (tr == -1) tr = n - 1;
    if (tl == tr) {
        sp[id] += d;
    } else {
        int m = (tl + tr) / 2;
        if (i <= m) {
            add(i, d, n, id * 2, tl, m);
        } else {
            add(i, d, n, id * 2 + 1, m + 1, tr);
        }
        sp[id] = sp[id * 2] + sp[id * 2 + 1];
    }
}

//INDEXATION!!!!!
int main() {
    int m;
    cin >> n >> m;
    arr.resize(n);
    sp.resize(4 * n);

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    build(n);

    while (m--) {
        int a, b, c;
        cin >> a >> b >> c;
        if (a == 1) {
            cout << sum(b - 1, c - 1, n) << endl;
        } else if (a == 2) {
            add(b - 1, c, n);
        }
    }

    return 0;
}
