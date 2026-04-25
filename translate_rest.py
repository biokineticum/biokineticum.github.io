import re
import os

replacements = {
    "noitom-en.html": [
        ('<title>Dystrybucja Noitom Polska | Motion Capture</title>', '<title>Noitom Distribution Poland | Motion Capture</title>'),
        ('content="Oficjalny dystrybutor systemów motion capture Noitom Perception Neuron w Polsce. Oprogramowanie i wsparcie techniczne."', 'content="Official distributor of Noitom Perception Neuron motion capture systems in Poland. Software and technical support."'),
        ('<h1>Noitom Polska</h1>', '<h1>Noitom Distribution</h1>'),
        ('<p>Dystrybucja systemów motion capture i zaawansowana analityka.</p>', '<p>Distribution of motion capture systems and advanced analytics.</p>'),
        ('<h2>Perception Neuron</h2>', '<h2>Perception Neuron</h2>'),
        ('<p>Oferujemy wsparcie w zakupie najtańszych na rynku systemów MoCap - Perception Neuron 3 oraz Studio.</p>', '<p>We offer support in purchasing the most affordable MoCap systems on the market - Perception Neuron 3 and Studio.</p>'),
        ('Zapytaj o ofertę', 'Ask for Offer'),
        ('<h2>Integracja z Axis Studio</h2>', '<h2>Axis Studio Integration</h2>'),
        ('<p>Tworzymy dedykowane oprogramowanie analizujące sygnał z Axis Studio na potrzeby sportu i medycyny.</p>', '<p>We create dedicated software analyzing the signal from Axis Studio for sports and medicine.</p>'),
        ('Zobacz portfolio', 'View Portfolio'),
        ('<h2>Dla kogo?</h2>', '<h2>For whom?</h2>'),
        ('<h3>Uczelnie Wyższe</h3>', '<h3>Universities</h3>'),
        ('<h3>Kliniki</h3>', '<h3>Clinics</h3>'),
        ('<h3>Trenerzy</h3>', '<h3>Trainers</h3>'),
        ('<p>Idealne rozwiązanie dla kierunków fizjoterapii, wychowania fizycznego i biomechaniki.</p>', '<p>An ideal solution for physiotherapy, physical education, and biomechanics programs.</p>'),
        ('<p>Edukacja pacjentów poprzez wizualizację ich problemów i postępów w <a\n                        href="contact-en.html">terapii</a>.</p>', '<p>Patient education through visualization of their problems and progress in <a href="contact-en.html">therapy</a>.</p>'),
        ('<p>Lepsze zrozumienie techniki ruchu zawodnika dzięki zaawansowanej <a href="index-en.html">analizie</a>.</p>', '<p>Better understanding of an athlete\'s movement technique thanks to advanced <a href="index-en.html">analysis</a>.</p>'),
        ('<h4>Menu</h4>', '<h4>Menu</h4>'),
        ('<h4>Kontakt</h4>', '<h4>Contact</h4>'),
        ('Wszelkie prawa zastrzeżone.', 'All rights reserved.'),
    ],
    "portfolio-en.html": [
        ('<title>Portfolio i Projekty | Biokineticum</title>', '<title>Portfolio & Projects | Biokineticum</title>'),
        ('content="Zobacz nasze dotychczasowe realizacje, projekty badawcze i stworzone oprogramowanie biomechaniczne."', 'content="See our previous implementations, research projects and custom biomechanical software."'),
        ('<h1>Nasze Realizacje</h1>', '<h1>Our Projects</h1>'),
        ('<p>Projekty badawcze, oprogramowanie i case studies.</p>', '<p>Research projects, software and case studies.</p>'),
        ('<h2>Wybrane Projekty</h2>', '<h2>Selected Projects</h2>'),
        ('<h3>Aplikacja BioKinEdu</h3>', '<h3>BioKinEdu Application</h3>'),
        ('<p>Platforma edukacyjna dla studentów fizjoterapii wykorzystująca interaktywne modele 3D do wizualizacji wektorów sił.</p>', '<p>Educational platform for physiotherapy students using interactive 3D models to visualize force vectors.</p>'),
        ('<h3>System Oceny Chodu</h3>', '<h3>Gait Analysis System</h3>'),
        ('<p>Integracja czujników IMU z autorskim oprogramowaniem w Pythonie do automatycznej oceny symetrii chodu.</p>', '<p>Integration of IMU sensors with proprietary Python software for automatic gait symmetry assessment.</p>'),
        ('<h3>Analizator Ciosów</h3>', '<h3>Punch Analyzer</h3>'),
        ('<p>Moduł stworzony dla klubów sztuk walki, wykorzystujący system Noitom do pomiaru kinetyki uderzeń.</p>', '<p>Module created for martial arts clubs, using the Noitom system to measure punch kinetics.</p>'),
        ('Dowiedz się więcej', 'Learn More'),
        ('<h4>Menu</h4>', '<h4>Menu</h4>'),
        ('<h4>Kontakt</h4>', '<h4>Contact</h4>'),
        ('Wszelkie prawa zastrzeżone.', 'All rights reserved.'),
    ],
    "contact-en.html": [
        ('<title>Kontakt | Biokineticum</title>', '<title>Contact | Biokineticum</title>'),
        ('content="Skontaktuj się z nami w sprawie konsultacji, analizy ruchu lub oprogramowania."', 'content="Contact us regarding consultations, motion analysis, or software."'),
        ('<h1>Skontaktuj się z nami</h1>', '<h1>Contact Us</h1>'),
        ('<p>Jesteśmy otwarci na współpracę naukową, komercyjną i technologiczną.</p>', '<p>We are open to scientific, commercial, and technological cooperation.</p>'),
        ('<h2>Dane Kontaktowe</h2>', '<h2>Contact Details</h2>'),
        ('<p><strong>Email:</strong> <a href="mailto:biokineticum@proton.me">biokineticum@proton.me</a></p>', '<p><strong>Email:</strong> <a href="mailto:biokineticum@proton.me">biokineticum@proton.me</a></p>'),
        ('<p><strong>Telefon:</strong> <a href="tel:+48502123662">+48 502 123 662</a></p>', '<p><strong>Phone:</strong> <a href="tel:+48502123662">+48 502 123 662</a></p>'),
        ('<p><strong>Lokalizacja:</strong> Jawiszowice, Polska</p>', '<p><strong>Location:</strong> Jawiszowice, Poland</p>'),
        ('<h2>Formularz Kontaktowy</h2>', '<h2>Contact Form</h2>'),
        ('<form action="#" method="POST" class="contact-form">', '<form action="#" method="POST" class="contact-form">'),
        ('<label for="name">Imię i nazwisko</label>', '<label for="name">Full Name</label>'),
        ('<label for="email">Adres Email</label>', '<label for="email">Email Address</label>'),
        ('<label for="subject">Temat</label>', '<label for="subject">Subject</label>'),
        ('<label for="message">Wiadomość</label>', '<label for="message">Message</label>'),
        ('Wyślij wiadomość', 'Send Message'),
        ('<h4>Menu</h4>', '<h4>Menu</h4>'),
        ('<h4>Kontakt</h4>', '<h4>Contact</h4>'),
        ('Wszelkie prawa zastrzeżone.', 'All rights reserved.'),
    ],
    "about-en.html": [
        ('<title>O mnie | dr hab. Dariusz Mosler – Biokineticum</title>', '<title>About Me | Dr. hab. Dariusz Mosler – Biokineticum</title>'),
        ('content="Poznaj dr hab. Dariusza Moslera - fizjoterapeutę i eksperta z zakresu biomechaniki i analizy ruchu."', 'content="Meet Dr. hab. Dariusz Mosler - physiotherapist and expert in biomechanics and motion analysis."'),
        ('<h1>O mnie</h1>', '<h1>About Me</h1>'),
        ('<p>Poznaj moją drogę naukową i zawodową.</p>', '<p>Discover my scientific and professional journey.</p>'),
        ('<h2>Doświadczenie i Edukacja</h2>', '<h2>Experience & Education</h2>'),
        ('<p>Jestem fizjoterapeutą oraz naukowcem z tytułem doktora habilitowanego nauk o kulturze fizycznej. Od lat łączę pracę akademicką z praktyką kliniczną.</p>', '<p>I am a physiotherapist and a scientist with a PhD (habilitation) in physical culture sciences. For years, I have been combining academic work with clinical practice.</p>'),
        ('<h3>Główne obszary zainteresowań:</h3>', '<h3>Main areas of interest:</h3>'),
        ('<li>Biomechanika sportu (szczególnie sztuki walki)</li>', '<li>Sports biomechanics (especially martial arts)</li>'),
        ('<li>Programowanie i analiza danych (Python, inercyjne systemy MoCap)</li>', '<li>Programming and data analysis (Python, inertial MoCap systems)</li>'),
        ('<li>Fizjoterapia oparta na dowodach (EBP)</li>', '<li>Evidence-Based Physiotherapy (EBP)</li>'),
        ('<h2>Misja Biokineticum</h2>', '<h2>The Biokineticum Mission</h2>'),
        ('<p>Moim celem jest dostarczenie pacjentom oraz sportowcom precyzyjnych, obiektywnych danych o ich ciele. Wierzę, że to, co można zmierzyć, można też skutecznie leczyć i poprawiać.</p>', '<p>My goal is to provide patients and athletes with precise, objective data about their bodies. I believe that what can be measured can also be effectively treated and improved.</p>'),
        ('Zobacz publikacje', 'View Publications'),
        ('<h4>Menu</h4>', '<h4>Menu</h4>'),
        ('<h4>Kontakt</h4>', '<h4>Contact</h4>'),
        ('Wszelkie prawa zastrzeżone.', 'All rights reserved.'),
    ]
}

for filename, rules in replacements.items():
    if not os.path.exists(filename):
        continue
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    for old, new in rules:
        content = content.replace(old, new)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Translated {filename}")
