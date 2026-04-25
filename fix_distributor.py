import re

def update_noitom_pl():
    with open('noitom.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace the Partner Package
    old_package = """<div class="card pricing-card text-center">
                    <h3>Pakiet Partnerski</h3>
                    <p style="margin-bottom: 0;">Dla przyszłych dystrybutorów (pełne wsparcie + marża)</p>
                </div>"""
    new_package = """<div class="card pricing-card text-center">
                    <h3>Pakiet Uczelniany</h3>
                    <p style="margin-bottom: 0;">Dla badaczy i uczelni (sprzęt + specjalistyczne oprogramowanie)</p>
                </div>"""
    content = content.replace(old_package, new_package)

    # Replace Section 8
    old_section_8 = """<!-- 8. Zostań Partnerem -->
        <section class="container text-center" style="padding: 4rem 2rem;">
            <h2>Zostań oficjalnym partnerem Noitom w Polsce</h2>
            <p style="max-width: 600px; margin: 1rem auto;">Jestem w bezpośrednim kontakcie z CEO firmy Noitom i buduję oficjalną dystrybucję w Polsce. Jeśli chcesz dołączyć jako partner lub dystrybutor – skontaktuj się ze mną.</p>
        </section>"""
    new_section_8 = """<!-- 8. Oficjalny Dystrybutor -->
        <section class="container text-center" style="padding: 4rem 2rem;">
            <h2>Oficjalna Dystrybucja Noitom w Polsce</h2>
            <p style="max-width: 600px; margin: 1rem auto;">Jestem w bezpośrednim kontakcie z centralą firmy Noitom i działam jako oficjalny dystrybutor tej marki w Polsce. Gwarantuję kompleksowe wsparcie przy zakupie, wdrożeniu i obsłudze sprzętu.</p>
        </section>"""
    content = content.replace(old_section_8, new_section_8)

    with open('noitom.html', 'w', encoding='utf-8') as f:
        f.write(content)

def update_noitom_en():
    with open('noitom-en.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace the Partner Package
    old_package = """<div class="card pricing-card text-center">
                    <h3>Partner Package</h3>
                    <p style="margin-bottom: 0;">For future distributors (full support + margin)</p>
                </div>"""
    new_package = """<div class="card pricing-card text-center">
                    <h3>University Package</h3>
                    <p style="margin-bottom: 0;">For researchers and universities (hardware + specialized software)</p>
                </div>"""
    content = content.replace(old_package, new_package)

    # Replace Section 8
    old_section_8 = """<!-- 8. Zostań Partnerem -->
        <section class="container text-center" style="padding: 4rem 2rem;">
            <h2>Become an official Noitom partner in Poland</h2>
            <p style="max-width: 600px; margin: 1rem auto;">I am in direct contact with the CEO of Noitom and am building the official distribution in Poland. If you want to join as a partner or distributor - contact me.</p>
        </section>"""
    new_section_8 = """<!-- 8. Oficjalny Dystrybutor -->
        <section class="container text-center" style="padding: 4rem 2rem;">
            <h2>Official Noitom Distribution in Poland</h2>
            <p style="max-width: 600px; margin: 1rem auto;">I am in direct contact with Noitom headquarters and operate as the official distributor of this brand in Poland. I guarantee comprehensive support with the purchase, implementation and operation of the equipment.</p>
        </section>"""
    content = content.replace(old_section_8, new_section_8)

    with open('noitom-en.html', 'w', encoding='utf-8') as f:
        f.write(content)

update_noitom_pl()
update_noitom_en()
print("Updated partner texts to official distributor texts.")
