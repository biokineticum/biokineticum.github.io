import re

with open('pricing-en.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('<title>Cennik | Biokineticum – dr hab. Dariusz Mosler</title>', '<title>Pricing | Biokineticum – Dr. hab. Dariusz Mosler</title>')
content = content.replace('content="Cennik usług fizjoterapeutycznych, analizy ruchu oraz rozwiązań sprzętowych dla sportowców. Sprawdź naszą ofertę."', 'content="Pricing for physiotherapy services, motion analysis, and hardware solutions for athletes. Check our offer."')
content = content.replace('content="Cennik | Biokineticum – dr hab. Dariusz Mosler"', 'content="Pricing | Biokineticum – Dr. hab. Dariusz Mosler"')

content = content.replace('<h1>Cennik Usług</h1>', '<h1>Pricing & Services</h1>')
content = content.replace('<p>Transparentne zasady i pakiety dostosowane do Twoich potrzeb.</p>', '<p>Transparent rules and packages tailored to your needs.</p>')
content = content.replace('<h2>Konsultacje i Terapia</h2>', '<h2>Consultations & Therapy</h2>')
content = content.replace('<h2>Analiza Biomechaniczna</h2>', '<h2>Biomechanical Analysis</h2>')
content = content.replace('<h2>Inne Usługi</h2>', '<h2>Other Services</h2>')

# Therapy
content = content.replace('<h3>Konsultacja Fizjoterapeutyczna</h3>', '<h3>Physiotherapy Consultation</h3>')
content = content.replace('<div class="price">150 PLN <span>/ wizyta</span></div>', '<div class="price">35 EUR <span>/ visit</span></div>')
content = content.replace('<li>Wywiad medyczny</li>', '<li>Medical Interview</li>')
content = content.replace('<li>Podstawowe testy funkcjonalne</li>', '<li>Basic functional tests</li>')
content = content.replace('<li>Plan terapii</li>', '<li>Therapy Plan</li>')
content = content.replace('<li>Zalecenia domowe</li>', '<li>Home Recommendations</li>')
content = content.replace('Umów wizytę', 'Book Visit')

# Analysis
content = content.replace('<h3>Pełna Analiza Ruchu</h3>', '<h3>Full Motion Analysis</h3>')
content = content.replace('<div class="price">350 PLN <span>/ sesja</span></div>', '<div class="price">80 EUR <span>/ session</span></div>')
content = content.replace('<li>Analiza wideo 2D/3D</li>', '<li>2D/3D Video Analysis</li>')
content = content.replace('<li>Ocena wzorców ruchowych</li>', '<li>Movement Pattern Assessment</li>')
content = content.replace('<li>Raport PDF z wynikami</li>', '<li>PDF Report with Results</li>')
content = content.replace('<li>Omówienie wyników</li>', '<li>Results Consultation</li>')
content = content.replace('<li>Plan korygujący</li>', '<li>Corrective Plan</li>')
content = content.replace('Wybierz pakiet', 'Choose Package')

# Other
content = content.replace('<h3>Pakiet Treningowy (Online)</h3>', '<h3>Online Training Package</h3>')
content = content.replace('<div class="price">950 PLN <span>/ 10 treningów</span></div>', '<div class="price">215 EUR <span>/ 10 visits</span></div>')
content = content.replace('<li>Opieka trenera</li>', '<li>Trainer Support</li>')
content = content.replace('<li>Cykliczne testy motoryczne</li>', '<li>Cyclical Motor Tests</li>')
content = content.replace('<li>Monitorowanie postępów</li>', '<li>Progress Monitoring</li>')
content = content.replace('Zapytaj o szczegóły', 'Ask for Details')

content = content.replace('<h4>Menu</h4>', '<h4>Menu</h4>')
content = content.replace('<h4>Kontakt</h4>', '<h4>Contact</h4>')
content = content.replace('Wszelkie prawa zastrzeżone.', 'All rights reserved.')

with open('pricing-en.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Translated pricing-en.html")
