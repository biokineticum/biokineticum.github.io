import os

# 1. Fix about.html and about-en.html
for filename in ['about.html', 'about-en.html']:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if '<link rel="alternate" hreflang="en"' not in content:
            content = content.replace(
                '<link rel="alternate" hreflang="pl" href="https://biokineticum.com/about.html" />',
                '<link rel="alternate" hreflang="pl" href="https://biokineticum.com/about.html" />\n    <link rel="alternate" hreflang="en" href="https://biokineticum.com/about-en.html" />'
            )
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed hreflang in {filename}")

# 2. Fix portfolio.html and portfolio-en.html
schema_code = """
    <!-- Schema -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "LocalBusiness",
      "name": "Biokineticum",
      "description": "Profesjonalna analiza biomechaniczna, fizjoterapia online oraz dystrybucja systemów motion capture Noitom Perception Neuron w Polsce",
      "url": "https://biokineticum.com",
      "telephone": "+48-502-123-662",
      "email": "biokineticum@proton.me",
      "address": {
        "@type": "PostalAddress",
        "addressCountry": "PL",
        "addressRegion": "Małopolskie",
        "addressLocality": "Jawiszowice"
      },
      "founder": {
        "@type": "Person",
        "name": "dr hab. Dariusz Mosler"
      },
      "priceRange": "$$"
    }
    </script>
"""

for filename in ['portfolio.html', 'portfolio-en.html']:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'application/ld+json' not in content:
            content = content.replace(
                '<!-- Google tag (gtag.js) -->',
                schema_code + '\n    <!-- Google tag (gtag.js) -->'
            )
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Added Schema to {filename}")

