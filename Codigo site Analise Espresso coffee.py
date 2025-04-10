import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

st.set_page_config(page_title="Análise de Café", layout="wide")
st.title("Análise de Extração de Café")

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

st.markdown("### Preencha os dados com **vírgula** como separador decimal:")

# Tabela inicial
df_input = pd.DataFrame({
    "Tipo de café": labels,
    "Pó de café (g)": ["" for _ in labels],
    "Líquido extraído (g)": ["" for _ in labels],
    "TDS (%)": ["" for _ in labels]
})

# Interface de edição
df_editado = st.data_editor(
    df_input,
    use_container_width=True,
    num_rows="fixed",
    hide_index=True,
    key="tabela"
)

if st.button("Gerar gráfico"):
    try:
        # Substituir ',' por '.' e converter para float
        for col in ["Pó de café (g)", "Líquido extraído (g)", "TDS (%)"]:
            df_editado[col] = df_editado[col].str.replace(",", ".")
            df_editado[col] = df_editado[col].astype(float)

        extracao = (df_editado["Líquido extraído (g)"] * df_editado["TDS (%)"]) / df_editado["Pó de café (g)"]
        tds = df_editado["TDS (%)"].tolist()

        marcadores = ['x' if 'Conventional' in label else 'o' for label in labels]
        colors = plt.cm.get_cmap('tab20', len(labels))

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

    except ValueError:
        st.error("⚠️ Por favor, preencha todos os campos com números usando vírgula como separador decimal (ex: 10,25).")
    except ZeroDivisionError:
        st.error("⚠️ O valor de 'Pó de café (g)' não pode ser zero.")
    except Exception as e:
        st.error(f"❌ Erro inesperado: {e}")
