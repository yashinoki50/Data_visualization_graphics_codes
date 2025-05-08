import matplotlib.pyplot as plt

yillar = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]

yumurta = [16.497, 17.145, 16.726, 18.098, 19.281, 19.643, 19.898, 19.788, 19.297, 19.808, 20.637]  # milyar adet

kanatli_eti = [1758363, 1894669, 1909276, 1879018, 2136734, 2156671, 2138451, 2136263, 2245770, 2417995, 2328791]  # ton

fig, ax1 = plt.subplots(figsize=(14, 7))
fig.patch.set_facecolor('#edeae5')   
ax1.set_facecolor('#edeae5')       

color = 'tab:orange'
ax1.set_xlabel('Yıl', fontsize=12)
ax1.set_ylabel('Yumurta Üretimi (Milyar Adet)', color=color, fontsize=12)
ax1.plot(yillar, yumurta, marker='o', color=color, label='Yumurta Üretimi')
ax1.tick_params(axis='y', labelcolor=color)
ax1.ticklabel_format(style='plain', axis='y')  
ax1.set_xticks(yillar) 
ax1.set_xticklabels(yillar, rotation=45)


ax2 = ax1.twinx()
ax2.set_facecolor('#edeae5')  
color = 'tab:blue'
ax2.set_ylabel('Kanatlı Eti Üretimi (Ton)', color=color, fontsize=12)
ax2.plot(yillar, kanatli_eti, marker='s', linestyle='--', color=color, label='Kanatlı Eti Üretimi')
ax2.tick_params(axis='y', labelcolor=color)
ax2.ticklabel_format(style='plain', axis='y') 

plt.title('2013–2023 Yumurta ve Kanatlı Eti Üretimi', fontsize=16, fontweight='bold')
ax1.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('kanatli_uretim_grafik.png', dpi=300, facecolor='#edeae5') 
plt.show()