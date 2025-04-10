import matplotlib.pyplot as plt
import numpy as np

# Dados fornecidos
extracao = [19.97578042, 20.10653034, 18.55023605, 22.258602,
            17.04259947, 20.68181579, 16.0463482, 19.08092593]
tds = [3.83, 1.75, 6.91, 3.74, 4.82, 4.66, 7.07, 3.77]

# Legendas associadas
labels = [
    "Simple espresso (Conventional coffee)",
    "Lungo espresso (Conventional coffee)",
    "Double espresso (Conventional coffee)",
    "Double lungo espresso (Conventional coffee)",
    "Simple espresso (Specialty coffee)",
    "Lungo espresso (Specialty coffee)",
    "Double espresso (Specialty coffee)",
    "Double lungo espresso (Specialty coffee)"
]

# Definir marcadores com base no tipo de café
marcadores = ['x' if 'Conventional' in label else 'o' for label in labels]

# Cores distintas
colors = plt.cm.get_cmap('tab20', len(extracao))

# Criar figura
fig, ax = plt.subplots(figsize=(10, 8))

# Adicionar áreas destacadas
ax.axhspan(8, 12, facecolor='lightgreen', alpha=0.3)
ax.axvspan(18, 22, facecolor='lightgreen', alpha=0.3)

# Plotar os pontos
for i in range(len(extracao)):
    ax.scatter(extracao[i], tds[i], label=labels[i],
               color=colors(i), marker=marcadores[i], s=100)

# Configurar grades
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

# Rótulos dos eixos
ax.set_xlabel('Extração (%)')
ax.set_ylabel('TDS (%)')

# Legenda menor na parte inferior do gráfico
ax.legend(loc='upper center', bbox_to_anchor=(
    0.5, -0.25), fontsize='small', ncol=2)

# Ajuste de layout
plt.tight_layout()
plt.show()
