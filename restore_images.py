import re

for filename in ['noitom.html', 'noitom-en.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add hero image back
    if 'images/noitom_system.jpg' not in content:
        # Find the end of hero-content div and insert hero-image-container
        hero_img_html = """
            <div class="hero-image-container" style="margin-top: 3rem;">
                <img src="images/noitom_system.jpg" alt="Motion Capture System Perception Neuron" class="hero-image" style="border-radius: var(--radius-lg); width: 100%; max-width: 900px; display: block; margin: 0 auto; box-shadow: var(--shadow-lg);">
            </div>"""
        
        # We find the closing div of hero-content
        content = re.sub(
            r'(<div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">\s*<a[^>]+>.*?</a>\s*<a[^>]+>.*?</a>\s*</div>\s*</div>)',
            r'\1' + hero_img_html,
            content
        )

    # 2. Add card images to Section 3
    # Card 1 (Education / Animation) -> cmj_app.jpg
    # In PL:
    content = content.replace(
        '<div class="card">\n                    <p>Doskonały',
        '<div class="card">\n                    <img src="images/cmj_app.jpg" alt="Edukacja i Animacja" class="card-img-top" style="height: 200px; object-fit: cover; border-radius: var(--radius-md); margin-bottom: 1rem;">\n                    <p>Doskonały'
    )
    # In EN:
    content = content.replace(
        '<div class="card">\n                    <p>Excellent',
        '<div class="card">\n                    <img src="images/cmj_app.jpg" alt="Education and Animation" class="card-img-top" style="height: 200px; object-fit: cover; border-radius: var(--radius-md); margin-bottom: 1rem;">\n                    <p>Excellent'
    )

    # Card 2 (HTTP streaming) -> godot_strike.jpg
    # In PL:
    content = content.replace(
        '<div class="card">\n                    <p>Obsługuje HTTP streaming',
        '<div class="card">\n                    <img src="images/godot_strike.jpg" alt="HTTP Streaming i Real-Time" class="card-img-top" style="height: 200px; object-fit: cover; border-radius: var(--radius-md); margin-bottom: 1rem;">\n                    <p>Obsługuje HTTP streaming'
    )
    # In EN:
    content = content.replace(
        '<div class="card">\n                    <p>Supports HTTP streaming',
        '<div class="card">\n                    <img src="images/godot_strike.jpg" alt="HTTP Streaming and Real-Time" class="card-img-top" style="height: 200px; object-fit: cover; border-radius: var(--radius-md); margin-bottom: 1rem;">\n                    <p>Supports HTTP streaming'
    )

    # Card 3 (Data analysis) -> bvh_signal.jpg
    # In PL:
    content = content.replace(
        '<div class="card">\n                    <p>Możliwość zbierania danych',
        '<div class="card">\n                    <img src="images/bvh_signal.jpg" alt="Analiza Danych i BVH" class="card-img-top" style="height: 200px; object-fit: cover; border-radius: var(--radius-md); margin-bottom: 1rem;">\n                    <p>Możliwość zbierania danych'
    )
    # In EN:
    content = content.replace(
        '<div class="card">\n                    <p>Possibility of data collection',
        '<div class="card">\n                    <img src="images/bvh_signal.jpg" alt="Data Analysis and BVH" class="card-img-top" style="height: 200px; object-fit: cover; border-radius: var(--radius-md); margin-bottom: 1rem;">\n                    <p>Possibility of data collection'
    )

    # Card 4 doesn't have a specific image, so we leave it as text

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Images restored successfully.")
