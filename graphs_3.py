import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.ticker as ticker

BG_COLOR = '#edeae5'

yillar = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
toplam_et = [996.155, 1008.272, 1149.262, 1173.042, 1126.403, 1118.695, 1201.469, 1785.952, 1952.038, 2191.625, 2384.047]
nufus = [76.67, 77.70, 78.74, 79.81, 80.81, 82.00, 83.15, 83.61, 84.34, 85.28, 85.97]

data = pd.DataFrame({
    'Yıl': yillar,
    'Nüfus (Milyon)': nufus,
    'Et Üretimi (Bin Ton)': [et for et in toplam_et]
})

fig, ax = plt.subplots(figsize=(14, 12))
fig.set_facecolor(BG_COLOR)
ax.set_facecolor(BG_COLOR)

y_pos = np.arange(len(yillar))

nufus_bars = ax.barh(y_pos, [-n for n in nufus], height=0.7, color='skyblue', label='Nüfus (Milyon)', edgecolor='navy')

olcek_faktoru = max(nufus) / (max(toplam_et) / 1000) * 0.8
et_bars = ax.barh(y_pos, [(et/1000) * olcek_faktoru for et in toplam_et], height=0.7, 
                 color='salmon', label='Et Üretimi (Bin Ton)', edgecolor='darkred')

ax.set_yticks(y_pos)
ax.set_yticklabels(yillar)
ax.set_xticklabels([])

secax = ax.secondary_xaxis('top')
secax.set_xlabel('Et Üretimi (Bin Ton)', fontsize=12)
secax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{x / olcek_faktoru:.1f}' if x > 0 else ''))
secax.set_facecolor(BG_COLOR)

max_nufus = max(nufus) * 1.1
max_et = max([(et/1000) * olcek_faktoru for et in toplam_et]) * 1.1
ax.set_xlim(-max_nufus, max_et)

ax.grid(True, linestyle='--', alpha=0.7, axis='x', color='white')

for i, (n, e) in enumerate(zip(nufus, toplam_et)):
    ax.text(-n - 1, i, f"{n:.2f} ", va='center', ha='right', fontsize=9, color='navy')
    ax.text((e/1000) * olcek_faktoru + 0.5, i, f"{e:.2f} ", va='center', ha='left', fontsize=9, color='darkred')


ax.set_title('Nüfus ve Et Üretimi Piramidi (2013-2023)', fontsize=18, 
             fontweight='bold', color='darkblue', pad=20)
ax.set_xlabel('Nüfus (Milyon)', fontsize=12)
ax.set_ylabel('Yıl', fontsize=12)

ax.axvline(0, color='black', linestyle='-', alpha=0.5)

legend = ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.12), ncol=2, fontsize=12,
                  facecolor='white', edgecolor='black', framealpha=0.9)

kisi_basi_et = [et / (nuf * 1000000) * 10000000 for et, nuf in zip(toplam_et, nufus)]
nufus_degisim = (nufus[-1] - nufus[0]) / nufus[0] * 100
et_degisim = (toplam_et[-1] - toplam_et[0]) / toplam_et[0] * 100
kisi_basi_degisim = (kisi_basi_et[-1] - kisi_basi_et[0]) / kisi_basi_et[0] * 100

text_str = (f"10 Yıllık Değişim (2013-2023):\n"
           f"• Nüfus: %{nufus_degisim:.1f} artış\n"
           f"• Et Üretimi: %{et_degisim:.1f} artış\n"
           f"• Kişi Başı Et: %{kisi_basi_degisim:.1f} artış")

plt.figtext(0.80, 0.1, text_str, ha='center', va='center', fontsize=11,
           bbox=dict(boxstyle='round', facecolor='white', edgecolor='gray', alpha=0.9))

plt.tight_layout(rect=[0, 0.08, 1, 0.95])
plt.show()

plt.figure(figsize=(12, 6), facecolor=BG_COLOR)
ax2 = plt.gca()
ax2.set_facecolor(BG_COLOR)

plt.plot(yillar, kisi_basi_et, marker='o', linewidth=2, color='darkgreen', markersize=8)
plt.title('Kişi Başına Düşen Et Miktarı (2013-2023)', fontsize=16, fontweight='bold')
plt.xlabel('Yıl', fontsize=12)
plt.ylabel('kg/kişi', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7, color='white')
plt.xticks(yillar)

for i, v in enumerate(kisi_basi_et):
    plt.text(yillar[i], v + 3, f"{v:.2f} kg", ha='center', fontsize=9, color='darkgreen')

plt.tight_layout()
plt.show()
