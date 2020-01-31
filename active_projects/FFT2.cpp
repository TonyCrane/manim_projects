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

struct Complex {
    double r, i;
    Complex() { r = 0, i = 0; }
    Complex(double real, double imag): r(real), i(imag) {}
}F[maxn], G[maxn];
Complex operator + (Complex a, Complex b) { return Complex(a.r + b.r, a.i + b.i); }
Complex operator - (Complex a, Complex b) { return Complex(a.r - b.r, a.i - b.i); }
Complex operator * (Complex a, Complex b) { return Complex(a.r * b.r - a.i * b.i, a.r * b.i + a.i * b.r); }

int len, rev[maxn], lim = 1;

void FFT(Complex* a) {
    for (int i = 0; i < lim; ++i) if (i < rev[i]) swap(a[i], a[rev[i]]);
    for (int dep = 1; dep <= log2(lim); ++dep) {
        int m = 1 << dep;
        Complex wn = Complex(cos(2 * PI / m), sin(2 * PI / m));
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
}

int main() {
    int n = read();
    while (lim <= n) lim <<= 1, len++;
    for (int i = 0; i < lim; ++i) rev[i] = (rev[i >> 1] >> 1) | ((i & 1) << (len - 1));
    return 0;
}