import numpy as np
import matplotlib.pyplot as plt

# --- パラメータ設定 ---
# 論文の図1に合わせて結合定数を設定
e_sq = 1.0  # e^2 = 1.0 なので e = 1

# --- 計算式の定義 ---

def magnetic_susceptibility(T, e_sq):
    """磁化率 χ_m を計算する関数"""
    # 式 (5.6) に対応
    r_0 = 4.0 * np.pi * T / 3.0
    numerator = - e_sq / r_0
    denominator = 1.0 + e_sq / r_0
    return numerator / denominator

def gl_parameter_sq(T, e_sq):
    """GLパラメータ κ^2 を計算する関数"""
    # 式 (5.11) に対応
    r_0 = 4.0 * np.pi * T / 3.0
    log_term = np.log(np.pi * T)
    numerator = 1 + e_sq / r_0
    denominator = 2 * e_sq * r_0
    return numerator / denominator

# --- プロット用のデータ生成 ---
# 温度Tの範囲を設定します。
# T=0ではlogが発散し、1 - e^2*log(pi*T) = 0 となる点でχ_mが発散するため、
# その少し手前までをプロット範囲とします。
# 発散点 T = exp(1/e^2) / pi ≈ 0.865
T = np.linspace(0.001, 0.85, 600) # 0に近い点から発散点の手前まで

# 各温度でχ_mとκ^2を計算
chi_m = magnetic_susceptibility(T, e_sq)
kappa_sq = gl_parameter_sq(T, e_sq)

# --- グラフの描画 ---
# 論文の図1と同様に、2つのグラフを縦に並べて描画
#fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 8), sharex=True)
fig, (ax1) = plt.subplots(1, 1, figsize=(6, 4), sharex=True)


# 上のプロット：磁化率 χ_m
ax1.plot(T, chi_m, lw=2)
ax1.set_ylabel(r'$\chi_m$', fontsize=14)
ax1.set_ylim(-2, 10) # 論文の見た目に合わせる
ax1.grid(True, linestyle='--', alpha=0.6)
ax1.set_title(r'Holographic Superconductor Properties ($e=1$)', fontsize=16)

# 下のプロット：GLパラメータ κ^2
# ax2.plot(T, kappa_sq, lw=2)
# Type I / Type II の境界線を描画
#ax2.axhline(y=0.5, color='orange', linestyle='-')
#ax2.set_xlabel(r'$T$', fontsize=14)
#ax2.set_ylabel(r'$\kappa^2$', fontsize=14)
#ax2.set_ylim(0, 1.2) # 論文の見た目に合わせる
#ax2.grid(True, linestyle='--', alpha=0.6)

# Type I/II のテキストを追加
#ax2.text(0.6, 0.8, 'Type II', fontsize=12)
#ax2.text(0.6, 0.3, 'Type I', fontsize=12)

# レイアウトを整えて表示
plt.tight_layout()
plt.show()