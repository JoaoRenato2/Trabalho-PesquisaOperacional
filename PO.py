import numpy as np
from pulp import *

N, M = 50, 50

np.random.seed(0)
cost_matrix = np.random.randint(10, 100, size=(N, M))

prob = LpProblem("Minimizar Custo de Designação", LpMinimize)

x = LpVariable.dicts("x", (range(N), range(M)), 0, 1, LpBinary)

prob += lpSum([cost_matrix[i][j] * x[i][j] for i in range(N) for j in range(M)])

for i in range(N):
    prob += lpSum([x[i][j] for j in range(M)]) <= 1

for j in range(M):
    prob += lpSum([x[i][j] for i in range(N)]) == 1

prob.solve()

print("Status:", LpStatus[prob.status])
for i in range(N):
    for j in range(M):
        if x[i][j].varValue == 1:
            print(f"Funcionário {i} atribuído à tarefa {j}")
print("Custo Total:", value(prob.objective))
