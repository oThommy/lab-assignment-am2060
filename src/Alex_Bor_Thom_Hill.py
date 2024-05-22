##############################################################################
import numpy as np
import matplotlib.pyplot as plt
##############################################################################


# Constants
dy  = 0.05 #default is 0.05
tau = 0.02
v   = 1
beta = 4
theta = 3/4

n_lst = [5, 10, 15, 20, 25]
solutions = []
alphas = []


y = np.array([0+i*dy for i in range(int(round(1/dy))+1)])
n_y = len(y)



# K
K = np.zeros((n_y, n_y))
np.fill_diagonal(K, 2)
for i in range(n_y):
    for j in range(n_y):
        if abs(i-j) == 1:
            K[i,j] = -1
            
# Neumann boundary condition at y=0  
#K[0, 0] = 1 
K[0, 1] = 2 

K = v**(-1) *(-(n_y)**2 * K)

# M
M = np.eye(n_y)
#M[0,0] = 1/2
M = ((-beta**2)/v) *M


# Dirichlet at y=1
r = np.zeros(n_y)
r[-1] = ((n_y)**2)/v

# A
A = K + M

def theta_method(c, A = A, r = r, tau = tau, theta = theta):
    I = np.eye(n_y)
    c_next = np.linalg.solve((I- tau * theta *A), c + tau* ( (1 - theta)*(A@c+r) + theta * r))
    return c_next


for n in n_lst:
    c = np.zeros(n_y) 
    for _ in range(n):
        c = theta_method(c, A, r, tau, theta)
    solutions.append(c.copy())
    alpha = (3*c[-1] - 4*c[-2] + c[-3]) / (2*dy)  # Second-order backward difference
    alphas.append(alpha)
    
# Plotting
plt.figure(figsize=(10, 6))
for i, solution in enumerate(solutions):
    plt.plot(y, solution, label=f'x = {n_lst[i] * tau:.2f}')
plt.xlabel('y')
plt.ylabel('c (y)')
plt.title('Numerical Solution of c(y) at different times')
plt.legend()
plt.grid(True)

plt.xlim(0, 2)
plt.ylim(0, max([max(sol) for sol in solutions] + [1])+1)

plt.show()