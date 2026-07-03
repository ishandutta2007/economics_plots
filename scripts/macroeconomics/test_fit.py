import numpy as np

years = np.array([1600, 1825, 1950, 1990, 2022])
gdp_values = np.array([770e9, 1.75e12, 12.4e12, 51.0e12, 164.0e12])
log_gdp = np.log(gdp_values)

# Fit quadratic curve: log(GDP) = C*t^2 + B*t + A
C, B, A = np.polyfit(years, log_gdp, 2)

print(f"Quadratic fit coefficients (1600-2022):")
print(f"  C (t^2 coef): {C}")
print(f"  B (t coef): {B}")
print(f"  A (intercept): {A}")

r_acceleration = 2 * C
print(f"Growth rate acceleration: {r_acceleration * 100:.6f}% per year")

r_2022 = B + 2 * C * 2022
print(f"Growth rate in 2022 according to fit: {r_2022 * 100:.4f}%")

for target, name in [(1e15, "$1 Quadrillion"), (1e16, "$10 Quadrillion")]:
    target_log = np.log(target)
    roots = np.roots([C, B, A - target_log])
    future_roots = [r for r in roots if r > 2022]
    print(f"{name} crossing year: {future_roots}")
