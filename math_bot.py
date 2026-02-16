import sympy as sp

def algebra_example():
    # Algebra: Solving equations
    x = sp.symbols('x')
    equation = sp.Eq(x**2 + 2*x + 1, 0)
    solution = sp.solve(equation, x)
    return solution

def geometry_example():
    # Geometry: Area of a circle
    radius = sp.symbols('r')
    area = sp.pi * radius**2
    return area

def trigonometry_example():
    # Trigonometry: sin, cos and tan
    x = sp.symbols('x')
    sin_x = sp.sin(x)
    cos_x = sp.cos(x)
    return sin_x, cos_x

def analysis_example():
    # Analysis: Derivative
    x = sp.symbols('x')
    f = x**2
    derivative = sp.diff(f, x)
    return derivative

def linear_algebra_example():
    # Linear Algebra: Matrix operations
    A = sp.Matrix([[1, 2], [3, 4]])
    B = sp.Matrix([[5, 6], [7, 8]])
    product = A * B
    return product

def statistics_example():
    # Statistics: Expected value, variance
    x = sp.symbols('x')
    probability_distribution = sp.DiracDelta(x)
    expected_value = sp.integrate(x * probability_distribution, (x, -sp.oo, sp.oo))
    variance = sp.integrate((x - expected_value)**2 * probability_distribution, (x, -sp.oo, sp.oo))
    return expected_value, variance

def complex_numbers_example():
    # Complex Numbers: Operations
    z1 = sp.sympify('2 + 3*I')
    z2 = sp.sympify('1 - 4*I')
    addition = z1 + z2
    multiplication = z1 * z2
    return addition, multiplication

def differential_equations_example():
    # Differential Equations: Solve dy/dx = y
    y = sp.Function('y')(x)
    differential_eq = sp.Eq(y.diff(x), y)
    solution = sp.dsolve(differential_eq, y)
    return solution

def main():
    print("Algebra Example:", algebra_example())
    print("Geometry Example:", geometry_example())
    print("Trigonometry Example:", trigonometry_example())
    print("Analysis Example:", analysis_example())
    print("Linear Algebra Example:", linear_algebra_example())
    print("Statistics Example:", statistics_example())
    print("Complex Numbers Example:", complex_numbers_example())
    print("Differential Equations Example:", differential_equations_example())

if __name__ == '__main__':
    main()