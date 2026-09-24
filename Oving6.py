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


# Oppgave 5
# Leser inn filen, hopper over rad 1 til og med 8, skipper også de siste 10 radene
df = pd.read_csv("pvgis.csv", skiprows = 8, skipfooter=10, engine="python")

# Omgjør tiden til datetime, 
df["time"] = pd.to_datetime(df["time"], format = "%Y%m%d:%H%M")

# Setter tiden som indeks
df = df.set_index("time")

# Velger en dato, 8.juni
dag = df.loc["2023-07-8", "G(i)"]

