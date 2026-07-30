import os
import re

def inject_schema(filepath, schema_content):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove existing JSON-LD scripts to avoid duplicates
    content = re.sub(r'<script type="application/ld\+json">.*?</script>\s*', '', content, flags=re.DOTALL)
    
    # Inject before </head>
    if '</head>' in content:
        content = content.replace('</head>', f'{schema_content}\n</head>')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")
    else:
        print(f"Warning: </head> not found in {filepath}")

# 1. Homepage Schema (WebSite + Organization + Person)
homepage_schema = """    <!-- Schema: WebSite, Organization & Person -->
    <script type="application/ld+json">
    [
      {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": "Biokineticum",
        "url": "https://biokineticum.com/"
      },
      {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": "Biokineticum",
        "url": "https://biokineticum.com/",
        "logo": "https://biokineticum.com/images/logo.jpg",
        "email": "biokineticum@proton.me",
        "founder": {
          "@type": "Person",
          "name": "dr hab. Dariusz Mosler",
          "jobTitle": "Physiotherapist & Data Scientist",
          "sameAs": [
            "https://linkedin.com/in/dariusz-mosler-b3856768",
            "https://www.researchgate.net/profile/Dariusz-Mosler",
            "https://orcid.org/0000-0002-8794-2994"
          ]
        }
      }
    ]
    </script>"""

# 2. Telerehabilitation & Pricing Schema (Physician / Service / Person)
service_schema_pl = """    <!-- Schema: Physician & Service -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Physician",
      "name": "Biokineticum Telerehabilitacja",
      "image": "https://biokineticum.com/images/profile_hero.jpg",
      "logo": "https://biokineticum.com/images/logo.jpg",
      "description": "Telerehabilitacja, analiza ruchu (Machine Learning), prywatne konsultacje z płatnością w kryptowalutach.",
      "url": "https://biokineticum.com/telerehabilitacja.html",
      "medicalSpecialty": "Physiotherapy",
      "paymentAccepted": "Cryptocurrency, Bitcoin, Monero, Bank Transfer",
      "currenciesAccepted": "PLN, USD, EUR, BTC, XMR, USDT",
      "email": "biokineticum@proton.me",
      "areaServed": {
        "@type": "Country",
        "name": "Worldwide"
      },
      "founder": {
        "@type": "Person",
        "name": "dr hab. Dariusz Mosler",
        "jobTitle": "Physiotherapist & Data Scientist",
        "sameAs": [
          "https://linkedin.com/in/dariusz-mosler-b3856768",
          "https://www.researchgate.net/profile/Dariusz-Mosler",
          "https://orcid.org/0000-0002-8794-2994"
        ]
      },
      "hasOfferCatalog": {
        "@type": "OfferCatalog",
        "name": "Usługi Fizjoterapii",
        "itemListElement": [
          {
            "@type": "Offer",
            "itemOffered": {
              "@type": "Service",
              "name": "Konsultacja Telerehabilitacyjna",
              "description": "Wizyta online 45 min z wykorzystaniem analizy ruchu Machine Learning.",
              "provider": {
                "@type": "Person",
                "name": "dr hab. Dariusz Mosler"
              },
              "availableChannel": {
                "@type": "ServiceChannel",
                "serviceUrl": "https://matrix.org/",
                "availableLanguage": ["pl", "en"]
              }
            },
            "price": "100.00",
            "priceCurrency": "PLN"
          }
        ]
      }
    }
    </script>"""

service_schema_en = """    <!-- Schema: Physician & Service -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Physician",
      "name": "Biokineticum Telerehabilitation",
      "image": "https://biokineticum.com/images/profile_hero.jpg",
      "logo": "https://biokineticum.com/images/logo.jpg",
      "description": "Telerehabilitation, motion analysis (Machine Learning), private consultations with crypto payment.",
      "url": "https://biokineticum.com/telerehabilitation-en.html",
      "medicalSpecialty": "Physiotherapy",
      "paymentAccepted": "Cryptocurrency, Bitcoin, Monero, Bank Transfer",
      "currenciesAccepted": "PLN, USD, EUR, BTC, XMR, USDT",
      "email": "biokineticum@proton.me",
      "areaServed": {
        "@type": "Country",
        "name": "Worldwide"
      },
      "founder": {
        "@type": "Person",
        "name": "dr hab. Dariusz Mosler",
        "jobTitle": "Physiotherapist & Data Scientist",
        "sameAs": [
          "https://linkedin.com/in/dariusz-mosler-b3856768",
          "https://www.researchgate.net/profile/Dariusz-Mosler",
          "https://orcid.org/0000-0002-8794-2994"
        ]
      },
      "hasOfferCatalog": {
        "@type": "OfferCatalog",
        "name": "Physiotherapy Services",
        "itemListElement": [
          {
            "@type": "Offer",
            "itemOffered": {
              "@type": "Service",
              "name": "Telerehabilitation Consultation",
              "description": "45 min online visit using Machine Learning motion analysis.",
              "provider": {
                "@type": "Person",
                "name": "dr hab. Dariusz Mosler"
              },
              "availableChannel": {
                "@type": "ServiceChannel",
                "serviceUrl": "https://matrix.org/",
                "availableLanguage": ["pl", "en"]
              }
            },
            "price": "25.00",
            "priceCurrency": "USD"
          }
        ]
      }
    }
    </script>"""

person_schema = """    <!-- Schema: Person (Expert Profile) -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Person",
      "name": "dr hab. Dariusz Mosler",
      "jobTitle": "Physiotherapist & Data Scientist",
      "description": "Wykładowca, badacz MDPI, twórca Biokineticum. Łączy nauki o kulturze fizycznej z Data Science.",
      "email": "dariusz.mosler@gmail.com",
      "image": "https://biokineticum.com/images/profile_hero.jpg",
      "sameAs": [
        "https://linkedin.com/in/dariusz-mosler-b3856768",
        "https://www.researchgate.net/profile/Dariusz-Mosler",
        "https://orcid.org/0000-0002-8794-2994"
      ]
    }
    </script>"""

inject_schema('index.html', homepage_schema)
inject_schema('index-pl.html', homepage_schema)

inject_schema('telerehabilitacja.html', service_schema_pl)
inject_schema('cennik.html', service_schema_pl)

inject_schema('telerehabilitation-en.html', service_schema_en)
inject_schema('pricing-en.html', service_schema_en)

inject_schema('about.html', person_schema)
inject_schema('about-en.html', person_schema)

print("Advanced Schema injection complete.")
