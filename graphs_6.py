import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as ticker
import numpy as np
from matplotlib import rcParams

# Veriler
data = {
    'Yıl': [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    'Toplam Arılı Kovan (Adet)': [6641348, 7082732, 7748287, 7900364, 7991072, 8108424, 8128360, 8179418, 8733394, 8984676, 9224881],
    'Bal Üretimi (TON)': [94694, 103525, 108128, 105727, 114471, 107920, 109330, 104077, 96344, 118297, 114886],
    'Balmumu (TON)': [4241, 4053, 4756, 4440, 4488, 3987, 3791, 3765, 3766, 4165, 3971]
}

df = pd.DataFrame(data)

# Stil ayarları
rcParams['font.family'] = 'DejaVu Sans'
rcParams['axes.titleweight'] = 'bold'
rcParams['axes.labelweight'] = 'bold'
background_color = '#edeae5'  # Belirlediğiniz arka plan rengi

# Renk paleti
colors = ['#3498db', '#e74c3c', '#2ecc71']

# 3 ayrı grafik
fig, axs = plt.subplots(3, 1, figsize=(14, 15), facecolor=background_color)
plt.subplots_adjust(hspace=0.5, top=0.92)
fig.patch.set_facecolor(background_color)

# 1. Grafik: Arılı Kovan
axs[0].set_facecolor(background_color)
axs[0].fill_between(df['Yıl'], df['Toplam Arılı Kovan (Adet)'], 
                   color=colors[0], alpha=0.25)
line1 = axs[0].plot(df['Yıl'], df['Toplam Arılı Kovan (Adet)'], 
                   color=colors[0], linewidth=3, marker='o', markersize=8)[0]
axs[0].set_title('Toplam Arılı Kovan Sayısı (2013-2023)', fontsize=13, pad=12)
axs[0].yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{x/1e6:.1f} M'))
axs[0].grid(True, linestyle='--', alpha=0.4)

# Değer etiketleri (daha iyi konumlandırma)
for x, y in zip(df['Yıl'], df['Toplam Arılı Kovan (Adet)']):
    axs[0].text(x, y-300000, f'{y/1e6:.1f}M', ha='center', va='top', fontsize=9, 
               bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', boxstyle='round,pad=0.2'))

# 2. Grafik: Bal Üretimi
axs[1].set_facecolor(background_color)
axs[1].fill_between(df['Yıl'], df['Bal Üretimi (TON)'], 
                   color=colors[1], alpha=0.25)
line2 = axs[1].plot(df['Yıl'], df['Bal Üretimi (TON)'], 
                   color=colors[1], linewidth=3, marker='s', markersize=8)[0]
axs[1].set_title('Bal Üretimi (2013-2023)', fontsize=13, pad=12)
axs[1].grid(True, linestyle='--', alpha=0.4)

# Değer etiketleri
for x, y in zip(df['Yıl'], df['Bal Üretimi (TON)']):
    axs[1].text(x, y-2000, f'{y/1e3:.0f}K', ha='center', va='top', fontsize=9,
               bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', boxstyle='round,pad=0.2'))

# 3. Grafik: Balmumu
axs[2].set_facecolor(background_color)
axs[2].fill_between(df['Yıl'], df['Balmumu (TON)'], 
                   color=colors[2], alpha=0.25)
line3 = axs[2].plot(df['Yıl'], df['Balmumu (TON)'], 
                   color=colors[2], linewidth=3, marker='^', markersize=8)[0]
axs[2].set_title('Balmumu Üretimi (2013-2023)', fontsize=13, pad=12)
axs[2].set_xlabel('Yıl', fontsize=11, labelpad=10)
axs[2].grid(True, linestyle='--', alpha=0.4)

# Değer etiketleri
for x, y in zip(df['Yıl'], df['Balmumu (TON)']):
    axs[2].text(x, y-100, f'{y:.0f}', ha='center', va='top', fontsize=9,
               bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', boxstyle='round,pad=0.2'))

# Ortak ayarlar
for ax in axs:
    ax.set_xticks(df['Yıl'])
    ax.set_xticklabels(df['Yıl'], rotation=45)
    ax.set_xlim(2012.5, 2023.5)
    for spine in ax.spines.values():
        spine.set_color('#d5d5d5')

# Ana başlık
fig.suptitle('TÜRKİYE ARICILIK VERİLERİ (2013-2023)', 
             fontsize=16, y=0.995, weight='bold')

# Kaynak bilgisi
fig.text(0.1, 0.01, 'Kaynak: Türkiye İstatistik Kurumu (TÜİK) ', 
         ha='center', fontsize=10, color='#555555')

# Normalize edilmiş kombin grafik
plt.figure(figsize=(14, 8), facecolor=background_color)
ax = plt.gca()
ax.set_facecolor(background_color)

# Normalizasyon
for col, color, marker in zip(['Toplam Arılı Kovan (Adet)', 'Bal Üretimi (TON)', 'Balmumu (TON)'], 
                             colors, ['o', 's', '^']):
    normalized = df[col]/df[col].max()
    plt.plot(df['Yıl'], normalized, color=color, linewidth=3, 
             marker=marker, markersize=8, label=col.split(' (')[0])
    plt.fill_between(df['Yıl'], normalized, color=color, alpha=0.1)
    
    # Değer etiketleri (çakışmayı önlemek için farklı yükseklikler)
    offset = 0.02 if col == 'Toplam Arılı Kovan (Adet)' else -0.02 if col == 'Balmumu (TON)' else 0
    for x, y in zip(df['Yıl'], normalized):
        plt.text(x, y+offset, f'{y:.2f}', ha='center', va='bottom' if offset>=0 else 'top', 
                fontsize=9, color=color,
                bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', boxstyle='round,pad=0.2'))

plt.title('TÜRKİYE ARICILIK GÖSTERGELERİ - NORMALİZE KARŞILAŞTIRMA (2013-2023)', 
          fontsize=14, pad=20, weight='bold')
plt.xlabel('Yıl', fontsize=11, labelpad=10)
plt.ylabel('Normalize Edilmiş Değerler', fontsize=11, labelpad=10)
plt.grid(True, linestyle='--', alpha=0.4)
plt.xticks(df['Yıl'], rotation=45)
plt.legend(loc='upper left', frameon=False, fontsize=11)

# Eksen çerçevesi
for spine in ax.spines.values():
    spine.set_color('#d5d5d5')

plt.tight_layout()
plt.show()