import os

filename = 'portfolio-en.html'
if not os.path.exists(filename):
    print("File not found")
else:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    replacements = [
        ('Repozytoria kodu, aplikacje internetowe i projekty amatorskie', 'Code repositories, web applications and amateur projects'),
        ('Oficjalne repozytorium kodu firmy Biokineticum, w którym udostępniamy wybrane skrypty i narzędzia z\n                    zakresu analizy ruchu, biomechaniki oraz oprogramowania wspierającego.', 'Official Biokineticum code repository, where we share selected scripts and tools in the field of motion analysis, biomechanics and supporting software.'),
        ('Zobacz GitHub', 'View GitHub'),
        ('Prywatne konto GitHub twórcy – projekty hobbystyczne, eksperymentalne algorytmy do przetwarzania\n                    danych biokinematycznych i inne aplikacje typu open-source.', 'Creator\'s private GitHub account – hobby projects, experimental algorithms for processing biokinematic data and other open-source applications.'),
        ('Amatorski trening i symulator Centralnych Zaburzeń Przetwarzania Słuchowego (APD). Aplikacja\n                    internetowa stworzona w celach demonstracyjnych i edukacyjnych.', 'Amateur training and simulator of Central Auditory Processing Disorder (CAPD). Web application created for demonstration and educational purposes.'),
        ('Przejdź do aplikacji', 'Go to app'),
        ('Aplikacja logopedyczna do ćwiczenia ułożenia języka, wykorzystująca technologię rozpoznawania obrazu.\n                    Narzędzie testowe do wsparcia terapii mowy i artykulacji.', 'Speech therapy application for practicing tongue placement, using image recognition technology. A test tool to support speech therapy and articulation.'),
        ('<li><a href="education-en.html">Edukacja</a></li>', '<li><a href="education-en.html">Education</a></li>'),
        ('<li><a href="contact-en.html">Kontakt</a></li>', '<li><a href="contact-en.html">Contact</a></li>'),
        ('<p>Diagnostyka fizjoterapeutyczna i trening oparty na dowodach naukowych i technologii pomiarowej.\n                    </p>', '<p>Physiotherapeutic diagnostics and training based on scientific evidence and measurement technology.</p>'),
    ]

    for old, new in replacements:
        content = content.replace(old, new)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

    print("Portfolio translated.")
