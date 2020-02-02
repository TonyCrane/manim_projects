#include <bits/stdc++.h>
using namespace std;

const int maxn = 2000010;
const double PI = acos(-1);

struct Complex {
    double r, i;
    Complex() { r = 0, i = 0; }
    Complex(double real, double imag): r(real), i(imag) {}
}F[maxn], G[maxn];
Complex operator + (Complex a, Complex b) { return Complex(a.r + b.r, a.i + b.i); }
Complex operator - (Complex a, Complex b) { return Complex(a.r - b.r, a.i - b.i); }
Complex operator * (Complex a, Complex b) { return Complex(a.r * b.r - a.i * b.i, a.r * b.i + a.i * b.r); }

int rev[maxn], len, lim = 1;

void FFT(Complex* a, int opt) {
    for (int i = 0; i < lim; ++i) if (i < rev[i]) swap(a[i], a[rev[i]]);
    for (int dep = 1; dep <= log2(lim); ++dep) {
        int m = 1 << dep;
        Complex wn = Complex(cos(2.0 * PI / m), opt * sin(2.0 * PI / m));
        for (int k = 0; k < lim; k += m) {
            Complex w = Complex(1, 0);
            for (int j = 0; j < m / 2; ++j) {
                Complex t = w * a[k + j + m / 2];
                Complex u = a[k + j];
                a[k + j] = u + t;
                a[k + j + m / 2] = u - t;
                w = w * wn;
            }
        }
    }
    if (opt == -1) for (int i = 0; i < lim; ++i) a[i].r /= lim;
}

int main() {
    int n, m; scanf("%d %d", &n, &m);
    for (int i = 0; i <= n; ++i) scanf("%d", &F[i].r);
    for (int i = 0; i <= m; ++i) scanf("%d", &G[i].r);
    while (lim <= n + m) lim <<= 1, len++;
    for (int i = 0; i < lim; ++i) rev[i] = (rev[i >> 1] >> 1) | ((i & 1) << (len - 1));
    FFT(F, 1); FFT(G, 1);
    for (int i = 0; i <= m; ++i) F[i] = F[i] * G[i];
    FFT(F, -1);
    for (int i = 0; i <= n + m; ++i) {
        printf("%d ", (int)(F[i].r + 0.5));
    }
    return 0;
}