import numpy as np
import matplotlib.pyplot as plt

# --- パラメータ設定 ---
# 論文の図1に合わせて結合定数を設定
e_sq = 1.0  # e^2 = 1.0 なので e = 1

# --- 計算式の定義 ---

def lambda_sq_factor(T, e_sq):
    """λ^2 * (μ - μ_c) を計算する関数"""
    # 式(5.9c)から (μ - μ_c) を除いた部分
    # λ^2 * (μ - μ_c) = (1 - e^2 * ln(πT)) / (12 * π * e^2 * T)
    
    log_term = np.log(np.pi * T)
    numerator = 1 - e_sq * log_term
    denominator = 12 * np.pi * e_sq * T
    return numerator / denominator

# --- プロット用のデータ生成 ---
# 温度Tの範囲を設定します。
# 低温での発散の様子がわかるように、0に近い値から始めます。
T = np.linspace(0.001, 0.8, 500)

# 各温度で λ^2 * (μ - μ_c) を計算
y_values = lambda_sq_factor(T, e_sq)

# --- グラフの描画 ---
plt.figure(figsize=(8, 6))
plt.plot(T, y_values, label=r'$\lambda^2 (\mu - \mu_c)$ vs. $T$', lw=2.5)

# グラフの装飾
plt.xlabel(r'Temperature $T$', fontsize=14)
plt.ylabel(r'Scaled Penetration Depth Squared: $\lambda^2 (\mu - \mu_c)$', fontsize=14)
plt.title(r'Temperature Dependence of Penetration Depth (5D Theory, $e=1$)', fontsize=16)
plt.grid(True, linestyle='--', alpha=0.7)
plt.ylim(0, 250) # y軸の表示範囲を調整して発散の様子を見やすくする
plt.legend(fontsize=12)
plt.show()