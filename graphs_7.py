import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

yillar = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
koza_uretim = [121, 80, 115, 103, 102, 94, 90, 90, 76, 69, 78] 

colors = ["#1e90ff", "#00bfff", "#00ced1", "#20b2aa", "#3cb371"]
cmap = LinearSegmentedColormap.from_list("mavi_yesil", colors)
bar_colors = [cmap(i/max(koza_uretim)) for i in koza_uretim]

BG_COLOR = '#edeae5'  
plt.figure(figsize=(13, 7), facecolor=BG_COLOR)
ax = plt.gca()
ax.set_facecolor(BG_COLOR)

bars = plt.bar(yillar, koza_uretim, color=bar_colors,
              edgecolor='white', linewidth=1.2,
              width=0.7, alpha=0.9)

plt.plot(yillar, koza_uretim, color='#2f4f4f',
         marker='o', markersize=8, linewidth=2.5,
         linestyle='--', alpha=0.8, label='Üretim Trendi')

plt.title('İPEKBÖCEKÇİLİĞİ KOZA ÜRETİMİ (2013-2023)\n',
          fontsize=16, pad=20, fontweight='bold', color='#2f4f4f')
plt.xlabel('Yıl', fontsize=12, labelpad=12, color='#2f4f4f')
plt.ylabel('Üretim Miktarı (TON)', fontsize=12, labelpad=12, color='#2f4f4f')

plt.xticks(yillar, rotation=45, ha='right', fontsize=11)
plt.yticks(np.arange(0, 130, 20), fontsize=11)
plt.ylim(0, 125)
ax.tick_params(colors='#2f4f4f')

ax.yaxis.grid(True, linestyle=':', alpha=0.4, color='#a9a9a9')

for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height+1,
            f'{height}', ha='center', va='bottom',
            fontsize=10, color='#2f4f4f', fontweight='bold')

for spine in ax.spines.values():
    spine.set_color('#8fbc8f')
    spine.set_linewidth(1.5)

plt.tight_layout()
plt.subplots_adjust(bottom=0.15)

plt.savefig('ipek_uretim_son_hali.png',
            dpi=300, facecolor=BG_COLOR,
            bbox_inches='tight', edgecolor='none')
plt.show()