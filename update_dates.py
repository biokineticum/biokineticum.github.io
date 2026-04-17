import os
import re

files_and_years = {
    "artykul-wplyw-celu-taekwondo.html": "2021",
    "artykul-tradycja-vs-sport.html": "2022",
    "artykul-machine-learning-stres.html": "2020",
    "artykul-kontuzje-karate.html": "2019",
    "artykul-vr-unikanie-kolizji.html": "2017",
    "artykul-terapia-taekwondo-niepelnosprawnosc.html": "2018",
    "artykul-percepcja-bolu-muay-thai.html": "2024"
}

# 1. Update individual files
for filename, year in files_and_years.items():
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Replace the article meta:
        # <div class="article-meta">
        #      Opublikowano: 17 Kwiecień 2026 | Czas czytania: 4 min
        # </div>
        content = re.sub(r'Opublikowano:\s*17 Kwiecień 2026\s*\|', f'Opublikowano: {year} |', content)
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)

# 2. Update publikacje.html
pub_file = "publikacje.html"
if os.path.exists(pub_file):
    with open(pub_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Map the titles to years
    titles_to_years = {
        "Czy obecność celu wpływa na szybkość Twojego kopnięcia? Badania biomechaniczne Taekwon-do": "2021",
        "Tradycja kontra sport. Która wersja kopnięcia okrężnego jest szybsza?": "2022",
        "Algorytmy na tropie stresu. Co determinuje lęk u młodych mężczyzn?": "2020",
        "Cena pełnego kontaktu. Analiza kontuzji w Karate Kyokushin.": "2019",
        "Wirtualna Rzeczywistość (VR) w fizjoterapii. Jak technologia chroni przed urazami?": "2017",
        "Taekwondo jako terapia. Jak sztuki walki redukują agresję?": "2018",
        "Czy do bólu można się przyzwyczaić? Percepcja bólu w Muay Thai.": "2024"
    }

    for title, year in titles_to_years.items():
        # Match <span class="article-date">Opublikowano: 17 Kwiecień 2026</span>
        #      <h3 class="article-card-title">TITLE...
        pattern = r'(<span class="article-date">Opublikowano:)\s*17 Kwiecień 2026(</span>\s*<h3 class="article-card-title">)' + re.escape(title)
        content = re.sub(pattern, rf'\1 {year}\2{title}', content)

    with open(pub_file, "w", encoding="utf-8") as f:
        f.write(content)
    
print("Dates updated successfully.")
