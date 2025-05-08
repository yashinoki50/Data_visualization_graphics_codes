import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker


yillar = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
koyun = [29284247, 31140244, 31507934, 30983933, 33677636, 35194972, 37276050, 42126781, 45177690, 44687888, 42060470]
keci = [9225548, 10344936, 10416166, 10345299, 10634672, 10922427, 11205429, 11985845, 12341514, 11577862, 10302940]
kucukbas_toplam = [38509795, 41485180, 41924100, 41329232, 44312308, 46117399, 48481479, 54112626, 57519204, 56265750, 52363410]


plt.figure(figsize=(14, 8))


koyun_renk = '#e74c3c'  
keci_renk = '#3498db'   
toplam_renk = '#2ecc71' 


arka_plan_rengi = '#edeae5'


plt.scatter(yillar, koyun, color=koyun_renk, s=100, label='KOYUN', alpha=0.8)
plt.scatter(yillar, keci, color=keci_renk, s=100, label='KEÇİ', alpha=0.8)
plt.scatter(yillar, kucukbas_toplam, color=toplam_renk, s=100, label='KÜÇÜKBAŞ TOPLAM', alpha=0.8)


plt.plot(yillar, koyun, color=koyun_renk, linestyle='--', alpha=0.5)
plt.plot(yillar, keci, color=keci_renk, linestyle='--', alpha=0.5)
plt.plot(yillar, kucukbas_toplam, color=toplam_renk, linestyle='--', alpha=0.5)


plt.xlabel('YIL', fontsize=12, fontweight='bold')
plt.ylabel('HAYVAN SAYISI', fontsize=12, fontweight='bold')
plt.title('TOPLAM KÜÇÜKBAŞ HAYVAN SAYILARI (2013-2023)', fontsize=16, fontweight='bold')


plt.xticks(yillar, rotation=45, fontsize=10)


plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: f'{int(x/1000000)}M'))


plt.grid(True, linestyle='--', alpha=0.3)


for i, (y, k, kc, t) in enumerate(zip(yillar, koyun, keci, kucukbas_toplam)):
    if i % 2 == 0:
        plt.annotate(f'{k/1000000:.1f}M',
                    (y, k),
                    textcoords="offset points",
                    xytext=(0,10),
                    ha='center',
                    fontweight='bold',
                    color=koyun_renk,
                    fontsize=9)
        
        plt.annotate(f'{kc/1000000:.1f}M',
                    (y, kc),
                    textcoords="offset points",
                    xytext=(0,10),
                    ha='center',
                    fontweight='bold',
                    color=keci_renk,
                    fontsize=9)
        
        plt.annotate(f'{t/1000000:.1f}M',
                    (y, t),
                    textcoords="offset points",
                    xytext=(0,10),
                    ha='center',
                    fontweight='bold',
                    color=toplam_renk,
                    fontsize=9)


plt.legend(['KOYUN', 'KEÇİ', 'KÜÇÜKBAŞ TOPLAM'],
           loc='upper center',
           bbox_to_anchor=(0.5, -0.15),
           ncol=3,
           fontsize=10,
           frameon=True)


plt.gcf().patch.set_facecolor(arka_plan_rengi)
plt.gca().set_facecolor(arka_plan_rengi)


plt.subplots_adjust(bottom=0.2)


plt.tight_layout()
plt.savefig('kucukbas_hayvan_dagilim.png', dpi=300, bbox_inches='tight')
plt.show()