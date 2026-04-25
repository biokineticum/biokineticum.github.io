import re

with open('education-en.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('<title>Edukacja i Szkolenia | Analiza Ruchu i Biomechanika – Biokineticum</title>', '<title>Education & Training | Motion Analysis and Biomechanics – Biokineticum</title>')
content = content.replace('content="Szkolenia i kursy z analizy biomechanicznej, oprogramowania Noitom Axis Studio oraz zaawansowanej fizjoterapii. Edukacja dla fizjoterapeutów i trenerów."', 'content="Training and courses in biomechanical analysis, Noitom Axis Studio software, and advanced physiotherapy. Education for physiotherapists and trainers."')
content = content.replace('content="Edukacja i Szkolenia | Analiza Ruchu i Biomechanika – Biokineticum"', 'content="Education & Training | Motion Analysis and Biomechanics – Biokineticum"')

content = content.replace('<h1>Oprogramowanie Edukacyjne</h1>', '<h1>Educational Software</h1>')
content = content.replace('<p>Narzędzia wspierające naukę biomechaniki i anatomii dla studentów oraz profesjonalistów.</p>', '<p>Tools supporting the learning of biomechanics and anatomy for students and professionals.</p>')
content = content.replace('<p>Kompleksowe rozwiązanie do nauki analizy ruchu. Nasza platforma pozwala na wizualizację sił, kątów i\n                    momentów sił w czasie rzeczywistym.</p>', '<p>A comprehensive solution for learning motion analysis. Our platform allows visualizing forces, angles, and torques in real time.</p>')
content = content.replace('<li>Interaktywne modele 3D</li>', '<li>Interactive 3D models</li>')
content = content.replace('<li>Symulacje chodu i biegu</li>', '<li>Walking and running simulations</li>')
content = content.replace('<li>Baza przypadków klinicznych</li>', '<li>Clinical case database</li>')
content = content.replace('Wypróbuj demo', 'Try demo')
content = content.replace('<h2>Dla kogo?</h2>', '<h2>For whom?</h2>')
content = content.replace('<h3>Uczelnie Wyższe</h3>', '<h3>Universities</h3>')
content = content.replace('<p>Idealne rozwiązanie dla kierunków fizjoterapii, wychowania fizycznego i biomechaniki.</p>', '<p>An ideal solution for physiotherapy, physical education, and biomechanics programs.</p>')
content = content.replace('<h3>Kliniki</h3>', '<h3>Clinics</h3>')
content = content.replace('<p>Edukacja pacjentów poprzez wizualizację ich problemów i postępów w <a\n                        href="contact-en.html">terapii</a>.</p>', '<p>Patient education through visualization of their problems and progress in <a href="contact-en.html">therapy</a>.</p>')
content = content.replace('<h3>Trenerzy</h3>', '<h3>Trainers</h3>')
content = content.replace('<p>Lepsze zrozumienie techniki ruchu zawodnika dzięki zaawansowanej <a href="index-en.html">analizie</a>.\n                </p>', '<p>Better understanding of athlete\'s movement technique thanks to advanced <a href="index-en.html">analysis</a>.</p>')

content = content.replace('<p>Technologia w służbie edukacji medycznej.</p>', '<p>Technology in the service of medical education.</p>')
content = content.replace('<h4>Menu</h4>', '<h4>Menu</h4>')
content = content.replace('<h4>Kontakt</h4>', '<h4>Contact</h4>')
content = content.replace('Wszelkie prawa zastrzeżone.', 'All rights reserved.')

with open('education-en.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Translated education-en.html")
