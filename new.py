import matplotlib.pyplot as plt

initial_chromosomes = [
    ['Tehran', 'Isfahan', 'Tabriz', 'Shiraz', 'Mashhad'],
    ['Tabriz', 'Mashhad', 'Yazd', 'Tehran', 'Shiraz'],
    ['Isfahan', 'Shiraz', 'Mashhad', 'Tabriz', 'Tehran'],
    ['Shiraz', 'Tehran', 'Isfahan', 'Yazd', 'Mashhad'],
]

generation_1 = [
    ['Tehran', 'Isfahan', 'Yazd', 'Shiraz', 'Mashhad'], 
    ['Tabriz', 'Mashhad', 'Tehran', 'Shiraz', 'Yazd'],  
    ['Isfahan', 'Shiraz', 'Mashhad', 'Yazd', 'Tehran'], 
    ['Shiraz', 'Tehran', 'Tabriz', 'Isfahan', 'Mashhad'], 
]

generation_2 = [
    ['Tehran', 'Isfahan', 'Yazd', 'Mashhad', 'Shiraz'], 
    ['Mashhad', 'Tehran', 'Shiraz', 'Yazd', 'Tabriz'], 
    ['Shiraz', 'Mashhad', 'Yazd', 'Tehran', 'Isfahan'],
    ['Tehran', 'Tabriz', 'Isfahan', 'Mashhad', 'Shiraz'], 
]

generation_3 = [
    ['Mashhad', 'Isfahan', 'Yazd', 'Tehran', 'Shiraz'],  
    ['Tehran', 'Mashhad', 'Shiraz', 'Tabriz', 'Yazd'], 
    ['Isfahan', 'Mashhad', 'Tehran', 'Yazd', 'Shiraz'],  
    ['Shiraz', 'Mashhad', 'Tabriz', 'Tehran', 'Isfahan'],
]


fig, ax = plt.subplots(figsize=(12, 10))
ax.axis('off')

all_generations = [initial_chromosomes, generation_1, generation_2, generation_3]
labels = ["Initial Population", "Generation 1", "Generation 2", "Generation 3"]

for gen_idx, generation in enumerate(all_generations):
    for i, chrom in enumerate(generation):
        x_start = 0.5
        y_pos = 9 - (gen_idx * 2) - i 
        for j, city in enumerate(chrom):
            ax.text(x_start + j, y_pos, city, fontsize=10, ha="center", va="center",
                    bbox=dict(boxstyle="circle,pad=0.3", edgecolor="black", facecolor="lightblue"))

            if j < len(chrom) - 1:
                ax.plot([x_start + j + 0.2, x_start + j + 0.8], [y_pos, y_pos], color="gray", lw=1.5)

    ax.text(-1, 9 - (gen_idx * 2), labels[gen_idx], fontsize=12, fontweight="bold", va="center")

plt.title("Evolution of Chromosomes for TSP", fontsize=16, fontweight="bold")
plt.show()
