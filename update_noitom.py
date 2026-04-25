import re

content_pl = """
    <main>
        <!-- 1. Hero Section -->
        <section class="hero" style="background: radial-gradient(circle at top center, rgba(30, 30, 30, 0.8) 0%, transparent 100%);">
            <div class="container">
                <div class="hero-content">
                    <h1>Perception Neuron 3 + Polskie Oprogramowanie Analityczne</h1>
                    <p style="font-size: 1.25rem; max-width: 800px; margin: 0 auto 2rem;">Oficjalny Partner Noitom w Polsce | Profesjonalny motion capture + real-time streaming + własne aplikacje</p>
                    <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
                        <a href="contact.html" class="btn btn-primary">Zapytaj o ofertę</a>
                        <a href="contact.html" class="btn btn-outline">Umów bezpłatne demo online</a>
                    </div>
                </div>
            </div>
        </section>

        <!-- 2. Case Study -->
        <section class="container" style="padding: 4rem 2rem;">
            <div class="section-title">
                <h2>Zwalidowane naukowo</h2>
            </div>
            <div class="card" style="max-width: 800px; margin: 0 auto; text-align: center;">
                <p>Pod moim nadzorem w 2026 roku powstała praca magisterska na Uniwersytecie Jana Długosza w Częstochowie pt. „Joint Tracking and Angle Analysis Software with Real-Time Feedback for Physical Therapy”.</p>
                <p>Opracowany system markerless został zwalidowany przy użyciu Perception Neuron 3 jako narzędzia referencyjnego. Wyniki walidacji wykazały bardzo wysokie korelacje – r od 0,6 do ponad 0,9.</p>
                <p style="margin-bottom: 0;"><strong>Potwierdziło to wysoką dokładność i niezawodność rozwiązania w warunkach rzeczywistych.</strong></p>
            </div>
        </section>

        <!-- 3. Główne korzyści -->
        <section class="container" style="padding: 2rem 2rem 4rem;">
            <div class="section-title">
                <h2>Co daje Ci Perception Neuron 3?</h2>
            </div>
            <div class="grid-3">
                <div class="card">
                    <p>Doskonały do edukacji fizjoterapii i biomechaniki – idealny do nauczania analizy ruchu.</p>
                    <p style="margin-top: -1rem;">Świetny do motion capture w animacji i produkcji gier.</p>
                </div>
                <div class="card">
                    <p>Obsługuje HTTP streaming – pozwala tworzyć własne aplikacje w czasie rzeczywistym.</p>
                    <a href="portfolio.html" class="btn btn-outline" style="width: 100%; margin-top: auto;">Zobacz przykład real-time HTTP streaming</a>
                </div>
                <div class="card">
                    <p>Możliwość zbierania danych i późniejszej zaawansowanej analizy.</p>
                    <a href="portfolio.html" class="btn btn-outline" style="width: 100%; margin-top: auto;">Przykład analizy danych z kopnięć</a>
                </div>
                <div class="card">
                    <p>Pełna integracja z moim polskim oprogramowaniem analitycznym.</p>
                    <a href="https://github.com/biokineticum" target="_blank" rel="noopener noreferrer" class="btn btn-primary" style="width: 100%; margin-top: auto;">Zobacz przykładową nakładkę na GitHub</a>
                </div>
            </div>
        </section>

        <!-- 4. Dlaczego Perception Neuron 3? & 5. Moja przewaga -->
        <section class="container" style="padding: 4rem 2rem; background: var(--bg-surface); border-radius: var(--radius-lg); border: 1px solid var(--border-color);">
            <div class="split-layout" style="padding: 0;">
                <div>
                    <h2>Dlaczego właśnie ten system?</h2>
                    <ul class="features-list">
                        <li>Najmniejszy i najbardziej przenośny profesjonalny system motion capture</li>
                        <li>Wysoka odporność na zakłócenia</li>
                        <li>Przystępna cena przy zachowaniu bardzo dobrej jakości</li>
                        <li>Szerokie możliwości zastosowania</li>
                    </ul>
                </div>
                <div>
                    <h2>Dlaczego warto kupić u mnie?</h2>
                    <ul class="features-list">
                        <li>Własne polskie oprogramowanie analityczne stworzone specjalnie pod Perception Neuron 3</li>
                        <li>Pełne wsparcie techniczne w języku polskim</li>
                        <li>Szkolenia i wdrożenie</li>
                        <li>Możliwość tworzenia dedykowanych rozwiązań pod Twoje potrzeby</li>
                    </ul>
                </div>
            </div>
        </section>

        <!-- 6. Dla kogo? -->
        <section class="container" style="padding: 4rem 2rem;">
            <div class="section-title">
                <h2>Dla kogo jest ten system?</h2>
            </div>
            <div class="grid-3" style="grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));">
                <div class="card text-center" style="justify-content: center;"><h3 style="margin-bottom: 0;">Fizjoterapeuci i gabinety rehabilitacyjne</h3></div>
                <div class="card text-center" style="justify-content: center;"><h3 style="margin-bottom: 0;">Uczelnie i edukacja biomechaniczna</h3></div>
                <div class="card text-center" style="justify-content: center;"><h3 style="margin-bottom: 0;">Trenerzy i kluby sportowe</h3></div>
                <div class="card text-center" style="justify-content: center;"><h3 style="margin-bottom: 0;">Studia animacji i produkcji gier</h3></div>
                <div class="card text-center" style="justify-content: center;"><h3 style="margin-bottom: 0;">Badacze i laboratoria</h3></div>
            </div>
        </section>

        <!-- 7. Oferta -->
        <section class="container" style="padding: 2rem 2rem 4rem;">
            <div class="section-title">
                <h2>Wybierz pakiet</h2>
            </div>
            <div class="grid-3">
                <div class="card pricing-card text-center">
                    <h3>Pakiet Start</h3>
                    <p style="margin-bottom: 0;">Sprzęt + oprogramowanie</p>
                </div>
                <div class="card pricing-card featured text-center">
                    <h3>Pakiet Sport/Pro</h3>
                    <p style="margin-bottom: 0;">Sprzęt + oprogramowanie + szkolenie + analizy</p>
                </div>
                <div class="card pricing-card text-center">
                    <h3>Pakiet Partnerski</h3>
                    <p style="margin-bottom: 0;">Dla przyszłych dystrybutorów (pełne wsparcie + marża)</p>
                </div>
            </div>
        </section>

        <!-- 8. Zostań Partnerem -->
        <section class="container text-center" style="padding: 4rem 2rem;">
            <h2>Zostań oficjalnym partnerem Noitom w Polsce</h2>
            <p style="max-width: 600px; margin: 1rem auto;">Jestem w bezpośrednim kontakcie z CEO firmy Noitom i buduję oficjalną dystrybucję w Polsce. Jeśli chcesz dołączyć jako partner lub dystrybutor – skontaktuj się ze mną.</p>
        </section>

        <!-- 9. Finalne CTA -->
        <div class="text-center" style="margin-bottom: 4rem;">
            <a href="contact.html" class="btn btn-primary" style="font-size: 1.25rem; padding: 1rem 2rem;">Zapytaj o cenę i dostępność</a>
        </div>
    </main>
"""

content_en = """
    <main>
        <!-- 1. Hero Section -->
        <section class="hero" style="background: radial-gradient(circle at top center, rgba(30, 30, 30, 0.8) 0%, transparent 100%);">
            <div class="container">
                <div class="hero-content">
                    <h1>Perception Neuron 3 + Polish Analytical Software</h1>
                    <p style="font-size: 1.25rem; max-width: 800px; margin: 0 auto 2rem;">Official Noitom Partner in Poland | Professional motion capture + real-time streaming + custom applications</p>
                    <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
                        <a href="contact-en.html" class="btn btn-primary">Ask for an offer</a>
                        <a href="contact-en.html" class="btn btn-outline">Book a free online demo</a>
                    </div>
                </div>
            </div>
        </section>

        <!-- 2. Case Study -->
        <section class="container" style="padding: 4rem 2rem;">
            <div class="section-title">
                <h2>Scientifically Validated</h2>
            </div>
            <div class="card" style="max-width: 800px; margin: 0 auto; text-align: center;">
                <p>Under my supervision, a master's thesis was created in 2026 at the Jan Długosz University in Częstochowa entitled "Joint Tracking and Angle Analysis Software with Real-Time Feedback for Physical Therapy".</p>
                <p>The developed markerless system was validated using Perception Neuron 3 as a reference tool. The validation results showed very high correlations - r from 0.6 to over 0.9.</p>
                <p style="margin-bottom: 0;"><strong>This confirmed the high accuracy and reliability of the solution in real-world conditions.</strong></p>
            </div>
        </section>

        <!-- 3. Główne korzyści -->
        <section class="container" style="padding: 2rem 2rem 4rem;">
            <div class="section-title">
                <h2>What does Perception Neuron 3 give you?</h2>
            </div>
            <div class="grid-3">
                <div class="card">
                    <p>Excellent for physiotherapy and biomechanics education - ideal for teaching motion analysis.</p>
                    <p style="margin-top: -1rem;">Great for motion capture in animation and game production.</p>
                </div>
                <div class="card">
                    <p>Supports HTTP streaming - allows you to create your own real-time applications.</p>
                    <a href="portfolio-en.html" class="btn btn-outline" style="width: 100%; margin-top: auto;">See real-time HTTP streaming example</a>
                </div>
                <div class="card">
                    <p>Possibility of data collection and subsequent advanced analysis.</p>
                    <a href="portfolio-en.html" class="btn btn-outline" style="width: 100%; margin-top: auto;">Example of kick data analysis</a>
                </div>
                <div class="card">
                    <p>Full integration with my Polish analytical software.</p>
                    <a href="https://github.com/biokineticum" target="_blank" rel="noopener noreferrer" class="btn btn-primary" style="width: 100%; margin-top: auto;">See example overlay on GitHub</a>
                </div>
            </div>
        </section>

        <!-- 4. Dlaczego Perception Neuron 3? & 5. Moja przewaga -->
        <section class="container" style="padding: 4rem 2rem; background: var(--bg-surface); border-radius: var(--radius-lg); border: 1px solid var(--border-color);">
            <div class="split-layout" style="padding: 0;">
                <div>
                    <h2>Why this system?</h2>
                    <ul class="features-list">
                        <li>The smallest and most portable professional motion capture system</li>
                        <li>High immunity to interference</li>
                        <li>Affordable price while maintaining very good quality</li>
                        <li>Wide range of applications</li>
                    </ul>
                </div>
                <div>
                    <h2>Why buy from me?</h2>
                    <ul class="features-list">
                        <li>Own Polish analytical software created specifically for Perception Neuron 3</li>
                        <li>Full technical support in English / Polish</li>
                        <li>Training and implementation</li>
                        <li>Ability to create dedicated solutions for your needs</li>
                    </ul>
                </div>
            </div>
        </section>

        <!-- 6. Dla kogo? -->
        <section class="container" style="padding: 4rem 2rem;">
            <div class="section-title">
                <h2>Who is this system for?</h2>
            </div>
            <div class="grid-3" style="grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));">
                <div class="card text-center" style="justify-content: center;"><h3 style="margin-bottom: 0;">Physiotherapists and rehabilitation clinics</h3></div>
                <div class="card text-center" style="justify-content: center;"><h3 style="margin-bottom: 0;">Universities and biomechanical education</h3></div>
                <div class="card text-center" style="justify-content: center;"><h3 style="margin-bottom: 0;">Coaches and sports clubs</h3></div>
                <div class="card text-center" style="justify-content: center;"><h3 style="margin-bottom: 0;">Animation and game production studios</h3></div>
                <div class="card text-center" style="justify-content: center;"><h3 style="margin-bottom: 0;">Researchers and laboratories</h3></div>
            </div>
        </section>

        <!-- 7. Oferta -->
        <section class="container" style="padding: 2rem 2rem 4rem;">
            <div class="section-title">
                <h2>Choose a package</h2>
            </div>
            <div class="grid-3">
                <div class="card pricing-card text-center">
                    <h3>Start Package</h3>
                    <p style="margin-bottom: 0;">Hardware + software</p>
                </div>
                <div class="card pricing-card featured text-center">
                    <h3>Sport/Pro Package</h3>
                    <p style="margin-bottom: 0;">Hardware + software + training + analysis</p>
                </div>
                <div class="card pricing-card text-center">
                    <h3>Partner Package</h3>
                    <p style="margin-bottom: 0;">For future distributors (full support + margin)</p>
                </div>
            </div>
        </section>

        <!-- 8. Zostań Partnerem -->
        <section class="container text-center" style="padding: 4rem 2rem;">
            <h2>Become an official Noitom partner in Poland</h2>
            <p style="max-width: 600px; margin: 1rem auto;">I am in direct contact with the CEO of Noitom and am building the official distribution in Poland. If you want to join as a partner or distributor - contact me.</p>
        </section>

        <!-- 9. Finalne CTA -->
        <div class="text-center" style="margin-bottom: 4rem;">
            <a href="contact-en.html" class="btn btn-primary" style="font-size: 1.25rem; padding: 1rem 2rem;">Ask for price and availability</a>
        </div>
    </main>
"""

def replace_content(filename, new_content):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find where to replace: between </header> and the AdSense div
    # Regex will match anything between </header> and <div class="container" style="text-align: center; margin: 2rem auto;">
    
    start_str = '</header>'
    end_str = '<div class="container" style="text-align: center; margin: 2rem auto;">'
    
    start_idx = content.find(start_str)
    end_idx = content.find(end_str)
    
    if start_idx != -1 and end_idx != -1:
        start_idx += len(start_str)
        final_content = content[:start_idx] + "\n" + new_content + "\n    " + content[end_idx:]
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(final_content)
        print(f"Updated {filename}")
    else:
        print(f"Could not find replacement boundaries in {filename}")

replace_content('noitom.html', content_pl)
replace_content('noitom-en.html', content_en)

