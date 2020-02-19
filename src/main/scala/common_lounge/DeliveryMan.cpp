#include <cstdio>
#include <algorithm>
#include <functional>

using namespace std;

bool sortbyfirst(const pair<int, int> &a,
                 const pair<int, int> &b) {
    return a.first > b.first;
}

int main() {
    int n;
    scanf("%d", &n);
    int x;
    scanf("%d", &x);
    int y;
    scanf("%d", &y);
    pair<int, int> diff[n];
    int a[n];
    //order for Andy
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }
    //orders for Bob
    int b[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &b[i]);
    }
    for (int i = 0; i < n; i++) {
        diff[i].first = abs(a[i] - b[i]);
        diff[i].second = i;
    }
    //sort in decreasing order
    sort(diff, diff + n, sortbyfirst);
    int tips = 0;
    for (int i = 0; i < n && (x > 0 || y > 0); i++) {
        int j = diff[i].second;
        if (x > 0 && y > 0) {
            if (a[j] >= b[j]) {
                tips += a[j];
                x -= 1;
            } else {
                tips += b[j];
                y -= 1;
            }
        } else if (x > 0) {
            tips += a[j];
            x -= 1;
        } else {
            tips += b[j];
            y -= 1;
        }
    }
    printf("%d", tips);
    return 0;
}