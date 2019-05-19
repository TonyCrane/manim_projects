#include <bits/stdc++.h>
using namespace std;

int a[1000010];

void Qsort(int l, int r) {
    int i = l, j = r;
    int key = a[i];
    do {
        while (a[j] > key) j--;
        swap(a[i], a[j]);
        while (a[i] < key) i++;
        swap(a[i], a[j]);
    } while (i < j);
    if (l < j)   Qsort(l, j);
    if (++i < r) Qsort(i, r);
}
