import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt

# Oppgave 1
# tidsvariabel - et døgn, 24 timer
t = np.linspace(0, 24, 1000)

# gauss variabler
A = 800 # maks innstråling
mu = 13 # tidpunkt for maks innstråling
sigma = 3 # bredden av toppen

# Gauss modell:
G = A * np.exp(-(t - mu)**2 / (2 * sigma**2))

# plot
plt.plot(t, G, color = 'hotpink')
plt.xlabel("Tid [timer]")
plt.ylabel("Innstråling [W/m^2]")
plt.legend("G")
plt.grid(True)
plt.savefig(r"C:\repos\ELK330-Oving6\Oppgave1.png")
plt.show()

