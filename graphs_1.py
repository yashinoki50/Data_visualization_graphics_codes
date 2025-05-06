import matplotlib.pyplot as plt
import numpy as np

# Verileri tanımlayalım
yillar = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
sigir = [14415257, 14223109, 13994071, 14080155, 15943586, 17042506, 17688139, 17965482, 17850543, 16851956, 16421256]
manda = [117591, 122114, 133766, 142073, 161439, 178397, 184192, 192489, 185574, 171835, 161749]
buyukbas_toplam = [14532848, 14345223, 14127837, 14222228, 16105025, 17220903, 17872331, 18157971, 18036117, 17023791, 16583005]

# Figür ve eksen oluşturalım
fig, ax1 = plt.subplots(figsize=(12, 7))

# Renkleri tanımlayalım
kirmizi = '#e74c3c'
yesil = '#2ecc71'
mavi = '#3498db'

# İstediğiniz arka plan rengini tanımlayalım
arka_plan_rengi = '#edeae5'

# SOL EKSEN - Sığır ve Toplam için
# Sığır çizgisi
sigir_line, = ax1.plot(yillar, sigir, color=kirmizi, marker='o', markersize=7,
                      linestyle='-', linewidth=2, label="SIĞIR")

# Toplam çizgisi
toplam_line, = ax1.plot(yillar, buyukbas_toplam, color=yesil, marker='o', markersize=7,
                        linestyle='-', linewidth=2, label="BÜYÜKBAŞ TOPLAM")

# Sol eksen ayarları
ax1.set_xlabel('YIL', fontsize=12, fontweight='bold')
ax1.set_ylabel('HAYVAN SAYISI', fontsize=12, fontweight='bold', color='black')
ax1.tick_params(axis='y', labelcolor='black')
ax1.grid(True, linestyle='--', alpha=0.7)

# Sol eksen sayı formatını ayarlayalım
ax1.ticklabel_format(axis='y', style='plain')
ax1.set_yticks(np.arange(0, max(buyukbas_toplam) + 2000000, 2000000))
ax1.set_yticklabels([f'{int(x/1000000)}M' for x in np.arange(0, max(buyukbas_toplam) + 2000000, 2000000)])

# SAĞ EKSEN - Manda için
ax2 = ax1.twinx()
manda_line, = ax2.plot(yillar, manda, color=mavi, marker='o', markersize=7,
                       linestyle='-', linewidth=2, label="MANDA")

# Sağ eksen ayarları
ax2.set_ylabel('MANDA SAYISI', fontsize=12, fontweight='bold', color=mavi)
ax2.tick_params(axis='y', labelcolor=mavi)
ax2.ticklabel_format(style='plain')

# Grafik başlığı
plt.title('TÜRKİYE BÜYÜKBAŞ HAYVAN SAYILARI (2013-2023)', fontsize=16, fontweight='bold')

# X ekseni ayarları
plt.xticks(yillar, fontsize=10, rotation=45)

# LEJANDı DOĞRU ŞEKİLDE OLUŞTUR
lines = [sigir_line, toplam_line, manda_line]
labels = ["SIĞIR (KIRMIZI)", "BÜYÜKBAŞ TOPLAM (YEŞİL)", "MANDA (MAVİ)"]

# Lejandı grafiğin altına yerleştir
plt.figlegend(lines, labels, loc='upper center', bbox_to_anchor=(0.5, 0.05),
               ncol=3, frameon=True, fontsize=10)

# Alt kısma boşluk bırak (lejand için)
plt.subplots_adjust(bottom=0.2)

# Grafik stilini düzenle ve arka plan rengini değiştir
plt.grid(True, linestyle='--', alpha=0.7)
fig.patch.set_facecolor(arka_plan_rengi)  # Figür arka plan rengi
ax1.set_facecolor(arka_plan_rengi)  # Eksen arka plan rengi

# Grafiği kaydet ve göster
plt.tight_layout()
plt.subplots_adjust(bottom=0.2)  # Lejand için yer aç
plt.savefig('buyukbas_hayvan_sayilari_duzeltilmis.png', dpi=300, bbox_inches='tight')
plt.show()