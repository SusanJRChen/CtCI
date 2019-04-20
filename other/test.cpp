#include <iostream>
#include <vector>
#include <tuple>
#include <cassert>
#include <iostream>
#include <cmath>

// Approximate the solution to the differential equation D(y)(t) = -y(t)*t
double f(double t, double y)
{
    return -y * t;
}

std::tuple<std::vector<double>, std::vector<double>, std::vector<double>>
euler(double f(double, double),
      double t0, double y0, double tf,
      size_t n)
{
    assert(n > 0);
    double h{(tf - t0) / n};
    std::vector<double> t(n + 1);
    std::vector<double> y(n + 1);
    std::vector<double> dy(n + 1);
    y[0] = y0;
    for (size_t k{0}; k < n; ++k)
    {
        t[k] = t0 + k * h;
        double s0{f(t[k], y[k])};
        dy[k] = s0;
        y[k + 1] = y[k] + h * s0;
    }
    t[n] = tf;
    dy[n] = f(tf, y[n]);
    return std::make_tuple(t, y, dy);
}

int main()
{
    std::size_t const N{20};
    double t0{0.3};
    double y0{2.7};
    auto result = euler(f, t0, y0, 0.9, N);
    // Print the t-values
    for (std::size_t k{0}; k < N; ++k)
    {
        std::cout << std::get<0>(result)[k] << ", ";
    }
    std::cout << std::get<0>(result)[N] << std::endl;
    // Print the approximations y[k] ~ y(t[k])
    for (std::size_t k{0}; k < N; ++k)
    {
        std::cout << std::get<1>(result)[k] << ", ";
    }
    std::cout << std::get<1>(result)[N] << std::endl;
    // Print the actual solution y( t[k] )
    for (std::size_t k{0}; k < N; ++k)
    {
        double t{std::get<0>(result)[k]};
        std::cout << y0 * std::exp(0.5 * t0 * t0 - 0.5 * t * t) << ", ";
    }
    {
        double t{std::get<0>(result)[N]};
        std::cout << y0 * std::exp(0.5 * t0 * t0 - 0.5 * t * t) << std::endl;
    }
    return 0;
}