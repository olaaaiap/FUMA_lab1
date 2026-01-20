import numpy as np
from numpy.random import default_rng
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ---- Clasificación de punto: 0 fuera, 1 circulo, 2 cuadrado ----
def experimento_disjunto(x, y, a):
    if (x - 3*a)**2 + (y - a)**2 <= a**2:
        return 1
    elif (x > a/2) and (x < 1.5*a) and (y > a/2) and (y < 1.5*a):
        return 2
    else:
        return 0

def estimar_pi(N, a, seed=None):
    rng = default_rng(seed)
    x = rng.uniform(0, 40, size=N)
    y = rng.uniform(0, 80, size=N)

    n_circulo = 0
    n_cuadrado = 0

    for i in range(N):
        r = experimento_disjunto(x[i], y[i], a)
        if r == 1:
            n_circulo += 1
        elif r == 2:
            n_cuadrado += 1

    return (n_circulo / n_cuadrado) if n_cuadrado > 0 else np.nan


# --------- Parámetros ----------
a = 10
seed = 20
n_max = 200_000
step = 2_000
interval_ms = 20

# 1) Construir eje X (N) y eje Y (pi estimado)
x = np.arange(step, n_max + 1, step)
y = np.array([estimar_pi(n, a=a, seed=seed) for n in x])

# 2) Filtrar valores no válidos
mask = np.isfinite(y)
x = x[mask]
y = y[mask]

# Si por algún motivo todo fueran valores no válidos, evitamos crash
if len(x) == 0:
    raise ValueError("Todas las estimaciones han salido no válidas.")

# 3) Plot base
fig, ax = plt.subplots()
line, = ax.plot(x[:1], y[:1], label="pi estimado")
ax.axhline(np.pi, linestyle="--", label="pi real")

ax.set(
    xlim=[0, x[-1]],
    ylim=[3.0, 3.3],
    xlabel="Repeticiones (N)",
    ylabel="Estimación de pi",
    title=f"Convergencia Monte Carlo (a={a})"
)
ax.legend()
ax.grid(True)

# 4) Animación
def update(frame):
    line.set_xdata(x[:frame])
    line.set_ydata(y[:frame])
    return (line,)

ani = FuncAnimation(fig=fig, func=update, frames=len(x) + 1, interval=interval_ms, blit=True)

# Guarda GIF
ani.save("pi_convergencia.gif")
# plt.show()
