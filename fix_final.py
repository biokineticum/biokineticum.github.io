import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('-en.html') or f == 'english.html']
for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Nav link replacement
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

# 2. Fix the contact form translation in contact-en.html
contact_en = 'contact-en.html'
if os.path.exists(contact_en):
    with open(contact_en, 'r', encoding='utf-8') as f:
        content = f.read()

    # Form placeholders and labels
    content = content.replace('Imię i Nazwisko</label>', 'Full Name</label>')
    content = content.replace('placeholder="Twoje imię"', 'placeholder="Your name"')
    content = content.replace('placeholder="twoj@email.com"', 'placeholder="your@email.com"')
    content = content.replace('<option value="wizyta">Wizyta fizjoterapeutyczna</option>', '<option value="wizyta">Physiotherapy visit</option>')
    content = content.replace('<option value="analiza">Analiza ruchu</option>', '<option value="analiza">Motion analysis</option>')
    content = content.replace('<option value="software">Oprogramowanie BioKinEdu</option>', '<option value="software">BioKinEdu Software</option>')
    content = content.replace('<option value="inne">Inne</option>', '<option value="inne">Other</option>')
    content = content.replace('placeholder="Treść wiadomości..."', 'placeholder="Message content..."')
    
    # Titles and texts
    content = content.replace('Skontaktuj się ze mną</h1>', 'Contact me</h1>')
    content = content.replace('<p>Lub napisz bezpośrednio:</p>', '<p>Or write directly:</p>')
    
    # Footer fixes
    content = content.replace('<li><a href="education-en.html">Edukacja</a></li>', '<li><a href="education-en.html">Education</a></li>')
    content = content.replace('<li><a href="contact-en.html">Kontakt</a></li>', '<li><a href="contact-en.html">Contact</a></li>')

    with open(contact_en, 'w', encoding='utf-8') as f:
        f.write(content)

            content = f.read()

        # Replace the href of the kick analysis button
        # In PL:
        content = content.replace(
            '<a href="portfolio.html" class="btn btn-outline" style="width: 100%; margin-top: auto;">Przykład analizy danych z kopnięć</a>',
            '<a href="https://www.youtube.com/shorts/FBLqCoVivfA" target="_blank" rel="noopener noreferrer" class="btn btn-outline" style="width: 100%; margin-top: auto;">Przykład analizy danych z kopnięć</a>'
        )
        # In EN:
        content = content.replace(
            '<a href="portfolio-en.html" class="btn btn-outline" style="width: 100%; margin-top: auto;">Example of kick data analysis</a>',
            '<a href="https://www.youtube.com/shorts/FBLqCoVivfA" target="_blank" rel="noopener noreferrer" class="btn btn-outline" style="width: 100%; margin-top: auto;">Example of kick data analysis</a>'
        )

            f.write(content)

print("Applied fixes successfully.")
