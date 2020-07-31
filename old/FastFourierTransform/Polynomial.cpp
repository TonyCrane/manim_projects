/*************************************************************
 *  > File Name        : P3803_FFT.cpp
 *  > author           : Tony_Wong
 *  > Created Time     : 2019/12/12 12:18:32
 *  > algorithm        : FFT
**************************************************************/

#include <bits/stdc++.h>
using namespace std;

inline int read() {
    int x = 0; int f = 1; char ch = getchar();
    while (!isdigit(ch)) {if (ch == '-') f = -1; ch = getchar();}
    while (isdigit(ch))  {x = x * 10 + ch - 48; ch = getchar();}
    return x * f;
}

const int maxn = 2100010;
const double PI = acos(-1.0);

int cnt, rev[maxn], lim = 1;

struct Complex {
    double r, i;
    Complex() { r = 0, i = 0; }
    Complex(double real, double imag): r(real), i(imag) {}
}F[maxn], G[maxn];
Complex operator + (Complex a, Complex b) { return Complex(a.r + b.r, a.i + b.i); }
Complex operator - (Complex a, Complex b) { return Complex(a.r - b.r, a.i - b.i); }
Complex operator * (Complex a, Complex b) { return Complex(a.r * b.r - a.i * b.i, a.r * b.i + a.i * b.r); }

void FFT(Complex* a, int opt) {
    for (int i = 0; i < lim; ++i) if (i < rev[i]) swap(a[i], a[rev[i]]);
    for (int s = 1; s <= log2(lim); ++s) {
        int m = 1 << s;
        Complex wn = Complex(cos(2 * PI / m), opt * sin(2 * PI / m));
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
    if (opt == -1) for (int i = 0; i < lim; ++i) F[i].r /= lim;
}

int main() {
    int n = read(), m = read();
    for (int i = 0; i <= n; ++i) F[i].r = read();
    for (int i = 0; i <= m; ++i) G[i].r = read();
    while (lim <= n + m) lim <<= 1, cnt++;
    for (int i = 0; i < lim; ++i) rev[i] = (rev[i >> 1] >> 1) | ((i & 1) << (cnt - 1));
    FFT(F, 1); FFT(G, 1);
    for (int i = 0; i <= lim; ++i) F[i] = F[i] * G[i];
    FFT(F, -1);
    for (int i = 0; i <= n + m; ++i) {
        printf("%d ", (int)(F[i].r + 0.5));
    }
    return 0;
}