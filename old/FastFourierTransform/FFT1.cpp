#include <bits/stdc++.h>
using namespace std;

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

void FFT(int lim, Complex* a) {
    if (lim == 1) return;
    Complex a0[lim >> 1], a1[lim >> 1];
    for (int i = 0; i < lim; i += 2) 
        a0[i >> 1] = a[i], a1[i >> 1] = a[i + 1];
    FFT(lim >> 1, a0);
    FFT(lim >> 1, a1);
    Complex wn = Complex(cos(2.0 * PI / lim), sin(2.0 * PI / lim));
    Complex w  = Complex(1, 0);
    for (int k = 0; k < (lim >> 1); ++k) {
        a[k] = a0[k] + w * a1[k];
        a[k + (lim >> 1)] = a0[k] - w * a1[k];
        w = w * wn;
    }
}