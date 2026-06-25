import seaborn as sns
import matplotlib.pyplot as plt

__all__ = [
    "AZUL_OI", "LARANJA_OI", "VERDE_OI", "AMARELO_OI", "CIANO_OI",
    "VERMELHO_OI", "ROXO_OI", "PRETO_OI",
    "PALETA_OI_2", "PALETA_OI_5", "PALETA_OI_8",
    "HATCHES", "FUNDO", "CINZA_GRID", "CINZA_TEXT",
    "plt", "sns",
    "_estilizar", "_hachura_barras", "salvar_ou_mostrar",
]

# ── Paleta Okabe-Ito ───────────────────────────────────────────────────────
# Desenvolvida por Okabe & Ito (2008) para publicações científicas.
# Distinguível por daltônicos e em impressão P&B.
# Referência: https://jfly.uni-koeln.de/color/
AZUL_OI     = "#0072B2"
LARANJA_OI  = "#E69F00"
VERDE_OI    = "#009E73"
AMARELO_OI  = "#F0E442"
CIANO_OI    = "#56B4E9"
VERMELHO_OI = "#D55E00"
ROXO_OI     = "#CC79A7"
PRETO_OI    = "#000000"

PALETA_OI_2 = [AZUL_OI, VERMELHO_OI]
PALETA_OI_5 = [CIANO_OI, AZUL_OI, VERDE_OI, LARANJA_OI, VERMELHO_OI]
PALETA_OI_8 = [AZUL_OI, LARANJA_OI, VERDE_OI, AMARELO_OI,
               CIANO_OI, VERMELHO_OI, ROXO_OI, PRETO_OI]

# Hachuras para diferenciação extra independente de cor
HATCHES = ["", "///", "...", "xxx", "---"]

# ── Cores de layout ────────────────────────────────────────────────────────
FUNDO      = "#FFFFFF"
CINZA_GRID = "#DDDDDD"
CINZA_TEXT = "#1A1A1A"

# ── Tema global ────────────────────────────────────────────────────────────
sns.set_theme(style="whitegrid", font="DejaVu Sans")
plt.rcParams.update({
    "figure.facecolor":  FUNDO,
    "axes.facecolor":    FUNDO,
    "axes.edgecolor":    CINZA_GRID,
    "axes.labelcolor":   CINZA_TEXT,
    "axes.titlecolor":   CINZA_TEXT,
    "axes.titlesize":    13,
    "axes.titleweight":  "bold",
    "axes.labelsize":    11,
    "xtick.color":       CINZA_TEXT,
    "ytick.color":       CINZA_TEXT,
    "xtick.labelsize":   10,
    "ytick.labelsize":   10,
    "grid.color":        CINZA_GRID,
    "grid.linewidth":    0.6,
    "text.color":        CINZA_TEXT,
    "figure.dpi":        130,
    "savefig.dpi":       300,
    "savefig.facecolor": FUNDO,
    "savefig.bbox":      "tight",
    "lines.linewidth":   2.0,
    "patch.linewidth":   0.8,
})


def _estilizar(ax, titulo, xlabel, ylabel, despine_left=False, tight=True):
    ax.set_title(titulo, pad=14, loc="left", fontsize=13,
                 fontweight="bold", color=CINZA_TEXT)
    ax.set_xlabel(xlabel, labelpad=8)
    ax.set_ylabel(ylabel, labelpad=8)
    ax.tick_params(length=0)
    sns.despine(ax=ax, left=despine_left)
    if tight:
        ax.figure.tight_layout()


def _hachura_barras(ax, hatches=HATCHES):
    """Aplica hachura + borda escura em cada barra — legível em P&B."""
    for i, patch in enumerate(ax.patches):
        patch.set_hatch(hatches[i % len(hatches)])
        patch.set_edgecolor(CINZA_TEXT)
        patch.set_linewidth(0.7)


def salvar_ou_mostrar(fig, nome=None):
    if nome:
        fig.savefig(nome, bbox_inches="tight", facecolor=FUNDO)
    plt.show()
    plt.close(fig)
