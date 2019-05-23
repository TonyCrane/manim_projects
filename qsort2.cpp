#include <bits/stdc++.h>
using namespace std;

template <typename T>
void Qsort(T arr[], int l, int r) {
	if (l >= r) return;
	int i = l, j = r;
	T key = arr[i];
	while (i < j) {
		while (i < j && arr[j] >= key) j--;
		swap(arr[i], arr[j]);
		while (i < j && arr[i] <= key) i++;
		swap(arr[i], arr[j]);
	}
	Qsort(arr, l, j - 1);
	Qsort(arr, i + 1, r);
}

int arr[100010], n, i;

int main() {
    scanf("%d", &n);
    for (i = 0; i < n; ++i)
        scanf("%d", &arr[i]);
    Qsort(arr, 0, n - 1);
    for (i = 0; i < n; ++i)
        printf("%d ", arr[i]);
    printf("\n");
    return 0;
}