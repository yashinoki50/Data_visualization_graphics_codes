import matplotlib.pyplot as plt

etiketler = ['Sığır', 'Koyun', 'Keçi', 'Manda']
degerler = [1670606, 569066, 128386, 15386]
renkler = ['#FF6B6B', '#4D96FF', '#7DFF6A', '#FFD93D']

fig, ax = plt.subplots(figsize=(8, 6))
fig.patch.set_facecolor('#edeae5')  
ax.set_facecolor('#edeae5')        

wedges, texts, autotexts = ax.pie(
    degerler,
    labels=None, 
    autopct=lambda pct: f"{pct:.1f}%",
    startangle=90,
    colors=renkler,
    pctdistance=0.8,
    wedgeprops={'edgecolor': 'white'}
)

for text in autotexts:
    text.set_color('black')
    text.set_fontweight('bold')
    text.set_fontsize(8)

legend = ax.legend(
    wedges,
    [f"{etiketler[i]}: {degerler[i]:,} ton" for i in range(len(etiketler))],
    title="Et Türleri",
    loc='center left',
    bbox_to_anchor=(1, 0.5),
    fontsize=8.5
)

legend.get_frame().set_facecolor('#edeae5')
legend.get_frame().set_edgecolor('gray')

plt.title("2023 Yılı Et Üretimi Dağılımı", 
          fontsize=14, fontweight='bold', color='darkblue')

plt.tight_layout()
plt.savefig("et_uretimi_pasta_legend.png", dpi=300, facecolor='#edeae5')
plt.show()