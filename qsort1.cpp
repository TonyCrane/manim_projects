#include <bits/stdc++.h>
using namespace std;

void swap(int &a, int &b) {
    int tmp = a;
    a = b;
    b = tmp;
}

void Insertsort(int arr[], int l, int r) {
    for (int i = l + 1; i <= r; ++i) {
        for (int j = i; j > 0 && arr[j] < arr[j - 1]; --j) {
            swap(arr[j], arr[j - 1]);
        }
    }
}

void Qsort(int a[], int l, int r) {
    if (l >= r) return;
    if (r - l + 1 < 10) {
        Insertsort(a, l, r);
        return;
    }
    int i = l, j = r, k, flag = 0, pivot = rand() % (r - l + 1) + l;
    swap(a[l], a[pivot]);
    while (i < j) {
        while (j > i && a[j] >= a[l]) {
            if (a[j] == a[l]) {
                for (k = j-1; k > i; k--)
                    if (a[k] != a[j]) {
                        swap(a[k], a[j]);
                        break;
                    }
                if (k == i) {
                    if (a[l] >= a[i])
                        swap(a[l], a[i]);
                    else
                    {
                        swap(a[i], a[j]);
                        swap(a[l], a[i-1]);
                        i--;
                        j--;
                    }
                    flag = 1;
                    break;
                }
                else continue;
            }
            j--;
        }
        if (flag) break;
        while (i < j && a[i] <= a[l]) {
            if (a[i] == a[l] && i != l) {
                for (k = i+1; k < j; k++) {
                    if (a[k] != a[i]) {
                        swap(a[k], a[i]);
                        break;
                    }
                }
                if (k == j) {
                    swap(a[l], a[j]);
                    flag = 1;
                    break;
                }
                else continue;
            }
            i++;
        }
        if (flag) break;
        swap(a[i], (i == j) ? a[l] : a[j]);
    }
    Qsort(a, l, i-1);
    Qsort(a, j+1, r);
}

int arr[100010], n;

int main() {
    srand((int)time(NULL));
    scanf("%d", &n);
    for (int i = 0; i < n; ++i)
        scanf("%d", &arr[i]);
    Qsort(arr, 0, n - 1);
    for (int i = 0; i < n; ++i)
        printf("%d ", arr[i]);
    printf("\n");
    return 0;
}