import re

# ==========================================
# Translate index-en.html
# ==========================================
with open('index-en.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Meta tags
content = content.replace('<title>Biokineticum | Analiza Biomechaniczna i Fizjoterapia Online – dr hab. Dariusz Mosler</title>', '<title>Biokineticum | Biomechanical Analysis & Online Physiotherapy – Dr hab. Dariusz Mosler</title>')
content = content.replace('content="Profesjonalna analiza ruchu komputerowa, fizjoterapia online i oficjalny dystrybutor Noitom Perception Neuron w Polsce. Konsultacje zdalne już od 100 zł."', 'content="Professional motion analysis, online physiotherapy and official Noitom Perception Neuron distributor in Poland."')
content = content.replace('content="Biokineticum | Analiza Biomechaniczna i Fizjoterapia Online – dr hab. Dariusz Mosler"', 'content="Biokineticum | Biomechanical Analysis & Online Physiotherapy – Dr hab. Dariusz Mosler"')

# Hero section
content = content.replace('<h1>Analiza biomechaniczna i fizjoterapia</h1>', '<h1>Biomechanical Analysis & Physiotherapy</h1>')
content = content.replace('<p>Łączę <a href="pricing-en.html">praktykę fizjoterapeutyczną</a> z komputerową <a\n                        href="education-en.html">analizą ruchu</a>, aby dostarczać łatwe rozwiązania i\n                    skuteczniej pomagać pacjentom oraz sportowcom poprzez wykorzystanie <a href="noitom-en.html">narzędzi\n                        biomechanicznych</a>.</p>', '<p>I combine <a href="pricing-en.html">physiotherapy practice</a> with computer <a href="education-en.html">motion analysis</a> to provide easy solutions and effectively help patients and athletes using <a href="noitom-en.html">biomechanical tools</a>.</p>')
content = content.replace('Umów konsultację', 'Book Consultation')
content = content.replace('Zobacz ofertę', 'See Offers')

# About section
content = content.replace('<h2>dr n. o k.f. Dariusz Mosler</h2>', '<h2>Dr. hab. Dariusz Mosler, PhD</h2>')
content = content.replace('<p>Nazywam się Dariusz Mosler i jestem <a href="contact-en.html">fizjoterapeutą</a>. Posiadam tytuł doktora\n                    nauk o kulturze fizycznej\n                    i interesuję się w szczególności biomechaniką.</p>', '<p>My name is Dariusz Mosler and I am a physiotherapist. I hold a PhD in Physical Culture Sciences and I am particularly interested in biomechanics.</p>')
content = content.replace('<p>W mojej praktyce staram się wykorzystywać najnowsze osiągnięcia technologii, aby obiektywnie mierzyć\n                    i analizować ludzki ruch, co pozwala na precyzyjne dopasowanie terapii i treningu.</p>', '<p>In my practice, I strive to use the latest technological achievements to objectively measure and analyze human movement, allowing for precise adjustment of therapy and training.</p>')
content = content.replace('Dowiedz się więcej', 'Learn More')

# Services section
content = content.replace('<h2>Nasze Usługi</h2>', '<h2>Our Services</h2>')
content = content.replace('<p>Biomechaniczne podejście do zdrowia i sprawności fizycznej</p>', '<p>Biomechanical approach to health and physical fitness</p>')
content = content.replace('<h3>Fizjoterapia</h3>', '<h3>Physiotherapy</h3>')
content = content.replace('<p>Oferuję konsultacje fizjoterapeutyczne w trybie stacjonarnym oraz w formie wideokonferencji z\n                    wykorzystaniem diagnostyki komputerowej oraz zdale monitorowanie treningu i terapii.</p>', '<p>I offer physiotherapy consultations both in-person and via video conference, using computer diagnostics and remote monitoring of training and therapy.</p>')
content = content.replace('<h3>Analiza ruchu</h3>', '<h3>Motion Analysis</h3>')
content = content.replace('<p>Biomechaniczna ocena ruchu przy użyciu zaawansowanej komputerowej analizy obrazu wideo. Precyzyjne\n                    dane dla lepszych wyników. Analiza stacjonarna i zdalna.</p>', '<p>Biomechanical motion assessment using advanced computer video analysis. Precise data for better results. In-person and remote analysis.</p>')
content = content.replace('<h3>Testy motoryczne</h3>', '<h3>Motor Tests</h3>')
content = content.replace('<p>Ilościowa analiza danych pozwala na zbieranie twardych dowodów. Dowiedz się, jak wykonujesz\n                    ruch i monitoruj postępy - szybkość, siłę, zakresy ruchu.</p>', '<p>Quantitative data analysis allows gathering hard evidence. Learn how you move and monitor your progress - speed, strength, and range of motion.</p>')

# Partners section
content = content.replace('<h2>Partnerzy</h2>', '<h2>Our Partners</h2>')
content = content.replace('<p>Współpracujemy z najlepszymi w branży technologii sportowej i medycznej</p>', '<p>Collaborating with the best in sports technology and evidence-based medicine</p>')
content = content.replace('<h3>Victor – Garrido Sportech</h3>', '<h3>Victor – Garrido Sportech</h3>')
content = content.replace('<p>Victor i jego marka Garrido Sportech to pionierzy we wprowadzaniu sportu do obszaru medycyny opartej\n                    na faktach (evidence-based medicine). Ich innowacyjne rozwiązania technologiczne pozwalają na\n                    precyzyjną, ilościową analizę postępów sportowych.</p>', '<p>Victor and his brand, Garrido Sportech, are pioneers in bringing sports into the realm of evidence-based medicine. Their innovative technological solutions enable precise, quantitative analysis of athletic progress.</p>')
content = content.replace('<p>Co najważniejsze, technologia ta umożliwia zachowanie pełnej rzetelności naukowej bezpośrednio w\n                    codziennych warunkach treningowych, a nie tylko w zamkniętych laboratoriach. Dzięki niesamowitej\n                    przystępności, rozwiązania Garrido Sportech trafiają do szerokiego grona odbiorców – od amatorów po\n                    profesjonalistów – rewolucjonizując podejście do pomiaru wyników i optymalizacji treningu.</p>', '<p>Most importantly, this technology allows athletes and coaches to maintain strict scientific rigor directly in real-world training environments, rather than being limited to specialized laboratories. Highly accessible, Garrido Sportech\'s solutions reach a broad audience—from amateurs to professionals—revolutionizing the way performance is measured and training is optimized.</p>')
content = content.replace('Odwiedź stronę: www.garridosportech.cl', 'Visit website: www.garridosportech.cl')

# Footer
content = content.replace('<p>Diagnostyka fizjoterapeutyczna i trening oparty na dowodach naukowych i technologii pomiarowej.\n                    </p>', '<p>Physiotherapeutic diagnostics and training based on scientific evidence and measurement technology.</p>')
content = content.replace('<h4>Menu</h4>', '<h4>Menu</h4>')
content = content.replace('<h4>Kontakt</h4>', '<h4>Contact</h4>')
content = content.replace('Wszelkie prawa zastrzeżone.', 'All rights reserved.')

with open('index-en.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Translated index-en.html")
