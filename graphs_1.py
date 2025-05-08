import matplotlib.pyplot as plt
import numpy as np


yillar = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
sigir = [14415257, 14223109, 13994071, 14080155, 15943586, 17042506, 17688139, 17965482, 17850543, 16851956, 16421256]
manda = [117591, 122114, 133766, 142073, 161439, 178397, 184192, 192489, 185574, 171835, 161749]
buyukbas_toplam = [14532848, 14345223, 14127837, 14222228, 16105025, 17220903, 17872331, 18157971, 18036117, 17023791, 16583005]


fig, ax1 = plt.subplots(figsize=(12, 7))


kirmizi = '#e74c3c'
yesil = '#2ecc71'
mavi = '#3498db'


arka_plan_rengi = '#edeae5'


sigir_line, = ax1.plot(yillar, sigir, color=kirmizi, marker='o', markersize=7,
                      linestyle='-', linewidth=2, label="SIĞIR")


toplam_line, = ax1.plot(yillar, buyukbas_toplam, color=yesil, marker='o', markersize=7,
                        linestyle='-', linewidth=2, label="BÜYÜKBAŞ TOPLAM")


ax1.set_xlabel('YIL', fontsize=12, fontweight='bold')
ax1.set_ylabel('HAYVAN SAYISI', fontsize=12, fontweight='bold', color='black')
ax1.tick_params(axis='y', labelcolor='black')
ax1.grid(True, linestyle='--', alpha=0.7)


ax1.ticklabel_format(axis='y', style='plain')
ax1.set_yticks(np.arange(0, max(buyukbas_toplam) + 2000000, 2000000))
ax1.set_yticklabels([f'{int(x/1000000)}M' for x in np.arange(0, max(buyukbas_toplam) + 2000000, 2000000)])


ax2 = ax1.twinx()
manda_line, = ax2.plot(yillar, manda, color=mavi, marker='o', markersize=7,
                       linestyle='-', linewidth=2, label="MANDA")


ax2.set_ylabel('MANDA SAYISI', fontsize=12, fontweight='bold', color=mavi)
ax2.tick_params(axis='y', labelcolor=mavi)
ax2.ticklabel_format(style='plain')


plt.title('TOPLAM BÜYÜBAŞ HAYVAN SAYILARI(2013-2023)', fontsize=16, fontweight='bold')


plt.xticks(yillar, fontsize=10, rotation=45)


lines = [sigir_line, toplam_line, manda_line]
labels = ["SIĞIR ", "BÜYÜKBAŞ TOPLAM ", "MANDA "]


plt.figlegend(lines, labels, loc='upper center', bbox_to_anchor=(0.5, 0.05),
               ncol=3, frameon=True, fontsize=10)


plt.subplots_adjust(bottom=0.2)


plt.grid(True, linestyle='--', alpha=0.7)
fig.patch.set_facecolor(arka_plan_rengi)  
ax1.set_facecolor(arka_plan_rengi) 


plt.tight_layout()
plt.subplots_adjust(bottom=0.2)  
plt.savefig('buyukbas_hayvan_sayilari_duzeltilmis.png', dpi=300, bbox_inches='tight')
plt.show()