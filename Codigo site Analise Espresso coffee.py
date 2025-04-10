import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

st.set_page_config(page_title="Análise de Café", layout="wide")

st.title("Análise de Extração de Café")

# Labels fixos como banco de dados
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

st.markdown("### Insira os dados de preparo para cada tipo de café:")

# Criar dataframe base com labels
df_input = pd.DataFrame({
    "Tipo de café": labels,
    "Pó de café (g)": [None] * len(labels),
    "Líquido extraído (g)": [None] * len(labels),
    "TDS (%)": [None] * len(labels)
})

# Mostrar editor de tabela
df_editado = st.data_editor(
    df_input,
    use_container_width=True,
    num_rows="fixed",
    hide_index=True,
    key="tabela"
)

# Botão para gerar gráfico
if st.button("Gerar gráfico"):
    # Verificar se todos os valores estão preenchidos
    if df_editado.isnull().values.any():
        st.error("Por favor, preencha todos os campos da tabela antes de gerar o gráfico.")
    else:
        extracao = []
        tds = df_editado["TDS (%)"].tolist()

        # Calcular extração para cada linha
        for i, row in df_editado.iterrows():
            in_cafe = row["Pó de café (g)"]
            out_liquido = row["Líquido extraído (g)"]
            tds_percentual = row["TDS (%)"]
            extracao_calc = (out_liquido * tds_percentual) / in_cafe
            extracao.append(extracao_calc)

        # Marcadores baseados no tipo de café
        marcadores = ['x' if 'Conventional' in label else 'o' for label in labels]
        colors = plt.cm.get_cmap('tab20', len(labels))

        # Plot do gráfico
        fig, ax = plt.subplots(figsize=(10, 8))
        ax.axhspan(8, 12, facecolor='lightgreen', alpha=0.3)
        ax.axvspan(18, 22, facecolor='lightgreen', alpha=0.3)

        for i in range(len(labels)):
            ax.scatter(extracao[i], tds[i], label=labels[i],
                       color=colors(i), marker=marcadores[i], s=100)

        ax.grid(True, which='both', linestyle='--', linewidth=0.5)
        ax.set_xlabel('Extração (%)')
        ax.set_ylabel('TDS (%)')
        ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.25),
                  fontsize='small', ncol=2)
        plt.tight_layout()

        st.pyplot(fig)
