import numpy as np
import matplotlib.pyplot as plt
from numpy.typing import NDArray
from tqdm import tqdm
from scipy.linalg import lu_factor, lu_solve

v = 1
beta = 4
dy = 0.05
dx = 0.02 # tau
theta = 3/4
x_lst = dx * np.array([5, 10, 15, 20, 25])
N = int(1 / dy) - 1
num_steps = int(sorted(x_lst)[-1] / dx)
y = np.linspace(0, 1, N + 2, dtype=np.float64)

def create_matrix_A(*, n: int = N, v: float = v, dy: float = dy, beta: float = beta):
    factor1 = -1 / (v * (dy**2))
    factor2 = -beta**2 / v

    main_diag = 2 * np.ones(n + 1)
    off_diag = -1 * np.ones(n)
    
    matrix1 = np.diag(main_diag) + np.diag(off_diag, k=1) + np.diag(off_diag, k=-1)
    matrix2 = np.eye(n + 1)

    A = factor1 * matrix1 + factor2 * matrix2
    A[0, 1] = -2 # Neumann boundary condition at y=0
    return A

def create_r(*, n: int = N):
    r = np.zeros(n + 1) # r is a constant as it does not depend on x
    r[-1] = 1 / dy**2 # Dirichlet boundary condition at y=1
    return r

def create_u_0(*, n: int = N):
    '''
    Creates an initial concentration array `u_0` for x=0 as defined by the 
    Dirichlet boundary condition at x=0.

    The array `u_0` represents the concentration values at x=0 as a function of y.
    It includes the concentrations at y_0, y_1, ..., y_n but omits y_{n+1}.

    So, `u_0` = [c(0, y_0), c(0, y_1), ..., c(0, y_n)].
    '''
    return np.zeros(n + 1)

A = create_matrix_A()
r = create_r()

I = np.eye(N + 1)
matrix = I - theta * dx * A
lu, piv = lu_factor(matrix)
def theta_method(
    *,
    u_n: NDArray[np.float64],
    A: NDArray[np.float64] = A,
    r: NDArray[np.float64] = r,
    dx: float = dx,
    theta: float = theta
) -> NDArray[np.float64]:
    b = u_n + dx * (1 - theta) * (A @ u_n + r) + dx * theta * r
    u_next = lu_solve((lu, piv), b)
    return u_next

u = np.empty(
    shape=num_steps + 1, # +1 to include u_0
    dtype=[('x', np.float64), ('c_y', np.float64, (N + 2,))]
)
u_0_numerical = create_u_0()
u_0_full = np.append(u_0_numerical, 1) # Append 1 to include c(0, 1) = 1 Dirichlet boundary condition
u[0] = (0, u_0_full)
c_y_numerical = u_0_numerical

for n in tqdm(range(num_steps)):
    x = (n + 1) * dx
    c_y_numerical = theta_method(u_n=c_y_numerical)
    c_y_full = np.append(c_y_numerical, 1)
    u[n + 1] = (x, c_y_full)

for x in x_lst:
    c_y = u[u['x'] == x]['c_y'][0]
    plt.plot(y, c_y, label=f'$x = {x:.2f}$')
plt.xlabel('$y$')
plt.ylabel('$c(y)$')
plt.title('Numerical solutions $c(y)$ for different $x = n \\tau$')
plt.legend()
plt.grid(True)
plt.show()