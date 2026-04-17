import os
import re

# List of 12 Polish articles and their English filenames
articles = {
    "artykul-biomechanika-kopniecia.html": "article-biomechanics-kicking-en.html",
    "artykul-biomechanika-boksu.html": "article-biomechanics-boxing-en.html",
    "artykul-biomechanika-karate.html": "article-biomechanics-karate-en.html",
    "artykul-masa-efektywna-boks.html": "article-effective-mass-boxing-en.html",
    "artykul-lstm-sztuczna-inteligencja.html": "article-lstm-artificial-intelligence-en.html",
    "artykul-wplyw-celu-taekwondo.html": "article-target-effect-taekwondo-en.html",
    "artykul-tradycja-vs-sport.html": "article-tradition-vs-sport-en.html",
    "artykul-machine-learning-stres.html": "article-machine-learning-stress-en.html",
    "artykul-kontuzje-karate.html": "article-karate-injuries-en.html",
    "artykul-vr-unikanie-kolizji.html": "article-vr-collision-avoidance-en.html",
    "artykul-terapia-taekwondo-niepelnosprawnosc.html": "article-taekwondo-therapy-disability-en.html",
    "artykul-percepcja-bolu-muay-thai.html": "article-pain-perception-muay-thai-en.html"
}

# 1. Update the 12 Polish Articles
for pl_file, en_file in articles.items():
    if os.path.exists(pl_file):
        with open(pl_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Add hreflang
        if f'hreflang="en" href="https://biokineticum.com/{en_file}"' not in content:
            head_canonical_pattern = r'<link rel="canonical" href="[^"]+" />'
            hreflangs = f'<link rel="canonical" href="https://biokineticum.com/{pl_file}" />\n    <link rel="alternate" hreflang="pl" href="https://biokineticum.com/{pl_file}" />\n    <link rel="alternate" hreflang="en" href="https://biokineticum.com/{en_file}" />'
            content = re.sub(head_canonical_pattern + r'\s*<link rel="alternate" hreflang="pl" href="[^"]+" />', hreflangs, content)

        # Add Read in English switch
        if 'Read in English' not in content:
            h1_pattern = r'(<h1>.*?</h1>)'
            switcher = f'<div style="text-align: right; margin-bottom: 0.5rem;"><a href="{en_file}" style="color: var(--accent-light); font-weight: bold; text-decoration: none;">[ Read in English ]</a></div>\n                '
            # We insert it right before the H1
            content = re.sub(h1_pattern, switcher + r'\1', content)
            
        with open(pl_file, 'w', encoding='utf-8') as f:
            f.write(content)

# 2. Translate publikacje.html to publications-en.html
with open('publikacje.html', 'r', encoding='utf-8') as f:
    hub_content = f.read()

# Fix hreflang in the en copy
hub_content = hub_content.replace('href="https://biokineticum.com/publikacje.html" />\n    <link rel="alternate" hreflang="en" href="https://biokineticum.com/publications-en.html"', 
                                  'href="https://biokineticum.com/publications-en.html" />\n    <link rel="alternate" hreflang="en" href="https://biokineticum.com/publications-en.html"')
hub_content = hub_content.replace('<link rel="alternate" hreflang="pl" href="https://biokineticum.com/publikacje.html" />', 
                                  '<link rel="alternate" hreflang="pl" href="https://biokineticum.com/publikacje.html" />\n    <link rel="alternate" hreflang="x-default" href="https://biokineticum.com/publications-en.html" />')
hub_content = hub_content.replace('<meta property="og:url" content="https://biokineticum.com/publikacje.html">', 
                                  '<meta property="og:url" content="https://biokineticum.com/publications-en.html">')

# Modify language switcher for EN hub
hub_content = hub_content.replace('<strong>PL</strong> | <a href="publications-en.html" style="color: var(--accent-light); text-decoration: none;">EN</a>',
                                  '<a href="publikacje.html" style="color: var(--accent-light); text-decoration: none;">PL</a> | <strong>EN</strong>')

# Link translations for the navigation
hub_content = hub_content.replace('href="publikacje.html" class="active">Publikacje', 'href="publications-en.html" class="active">Publications')

# Texts translation
en_texts = {
    "<title>Baza Wiedzy i Publikacje Naukowe | dr Dariusz Mosler</title>": "<title>Knowledge Base & Scientific Publications | Dr. Dariusz Mosler</title>",
    "Baza wiedzy i publikacje naukowe dr. Dariusza Moslera. Poznaj najnowsze badania z zakresu biomechaniki, fizjoterapii i analizy ruchu w przystępnej formie.": "Knowledge base and scientific publications by Dr. Dariusz Mosler. Discover the latest research in biomechanics, physiotherapy, and motion analysis.",
    "Baza wiedzy i publikacje naukowe dr. Dariusza Moslera. Poznaj najnowsze badania z zakresu biomechaniki i fizjoterapii w przystępnej formie.": "Knowledge base and scientific publications by Dr. Dariusz Mosler. Discover the latest research in biomechanics and physiotherapy.",
    "<h1>Baza Wiedzy i Publikacje Naukowe</h1>": "<h1>Knowledge Base & Scientific Publications</h1>",
    "Współczesna fizjoterapia i sport opierają się na twardych dowodach (EBP - Evidence Based Practice).\n                    Na tym blogu przekładam skomplikowane badania biomechaniczne i analityczne na zrozumiały język\n                    praktyki fizjoterapeutycznej i sportowej. Odkryj, jak liczby i dane wpływają na ludzki ruch.": "Modern physiotherapy and sports are rooted in Evidence Based Practice (EBP).\n                    On this blog, I translate complex biomechanical and analytical research into accessible knowledge for physiotherapy and sports practice. Discover how data and numbers impact human movement.",
    "Zbiór artykułów popularnonaukowych tłumaczących skomplikowane badania biomechaniczne na język praktyki fizjoterapeutycznej i sportowej.": "A collection of science articles explaining complex biomechanical research for physiotherapy and sports practice.",
    "Opublikowano:": "Published:",
    "Czytaj pełną analizę &rarr;": "Read full analysis &rarr;",
    "Poznaj wyniki pomiarów &rarr;": "View measurement results &rarr;",
    "Październik 2023": "October 2023",
    "Kwiecień 2026": "April 2026"
}

for pl_text, en_text in en_texts.items():
    hub_content = hub_content.replace(pl_text, en_text)

# Translate titles and excerpts for 12 articles
title_translations = [
    ("Jak praca rąk i tułowia wpływa na siłę kopnięcia? Badania biomechaniczne w Taekwon-do", "How Does Arm and Trunk Movement Affect Kicking Force? Biomechanical Research in Taekwon-do"),
    ("Czy wiesz, że silne kopnięcie okrężne zależy w dużej mierze od tego, co robią Twoje ręce i tułów? Przebadaliśmy w laboratorium 13 elitarnych zawodników, aby zrozumieć, co optymalizuje transfer energii do stopy uderzającej.", "Did you know that a powerful roundhouse kick heavily depends on your arms and trunk? We examined 13 elite athletes in the lab to understand what optimizes energy transfer to the kicking foot."),
    ("Prawy prosty czy lewy prosty? Co decyduje o sile nokautującego ciosu w boksie.", "Jab or Cross? What Determines the Power of a Knockout Punch in Boxing."),
    ("Większa szybkość nie zawsze oznacza większą siłę uderzenia. Zobacz wyniki najnowszych badań biomechanicznych nad różnicami między uderzeniem z ręki przedniej (jab) a tylnej (cross).", "Greater speed does not always mean greater impact force. See the results of the latest biomechanical research on the differences between a jab and a cross."),
    ("Kopanie w powietrze czy w tarczę? Dlaczego tradycyjny trening karate wymaga zmian.", "Kicking in the Air vs. Striking a Target? Why Traditional Karate Training Needs to Evolve."),
    ("W tradycyjnym karate spędzamy setki godzin na wykonywaniu technik w powietrze. Moje najnowsze badania z wykorzystaniem czujników EMG pokazują jednak, że ludzkie ciało zachowuje się zupełnie inaczej, gdy musi uderzyć w fizyczny cel.", "In traditional karate, hundreds of hours are spent executing techniques into the air. However, my latest research using EMG sensors shows that the human body behaves completely differently when striking a physical target."),
    ("Masa efektywna w boksie. Dlaczego duża waga nie gwarantuje nokautu?", "Effective Mass in Boxing. Why Heavy Weight Doesn't Guarantee a Knockout?"),
    ("Czym jest 'masa efektywna' i dlaczego podczas ciosu wykorzystujesz zaledwie 3% wagi swojego ciała? Analiza biomechaniczna transferu masy w ciosach bokserskich.", "What is 'effective mass' and why do you utilize only 3% of your body weight during a punch? Biomechanical analysis of mass transfer in boxing punches."),
    ("Sztuczna Inteligencja w sportach walki. Jak sieci neuronowe przewidują siłę ciosu?", "Artificial Intelligence in Combat Sports. How Neural Networks Predict Punching Force?"),
    ("Czy można zmierzyć siłę kopnięcia bez drogich platform dynamometrycznych? Wyniki naszych najnowszych badań pokazują, że modele uczenia maszynowego (LSTM) potrafią z ogromną dokładnością obliczyć siłę uderzenia na podstawie ruchu samego ciała.", "Is it possible to measure kicking force without expensive force plates? The results of our latest studies show that machine learning models (LSTM) can calculate impact force with huge accuracy based solely on body movement."),
    ("Czy obecność celu wpływa na szybkość Twojego kopnięcia? Badania biomechaniczne Taekwon-do", "Does the Presence of a Target Affect Your Kicking Speed? Biomechanical Research in Taekwon-do"),
    ("Większość treningów sportów walki opiera się na technikach wykonywanych w powietrze. Moje najnowsze badania udowadniają jednak, że Twoje ciało porusza się najszybciej dopiero wtedy, gdy napotka fizyczny opór w postaci tarczy.", "Most martial arts training relies on techniques performed in the air. However, my latest research proves that your body moves fastest only when it encounters physical resistance in the form of a target pad."),
    ("Tradycja kontra sport. Która wersja kopnięcia okrężnego jest szybsza?", "Tradition vs. Sport. Which Version of the Roundhouse Kick is Faster?"),
    ("Różne zawody wymagają różnego wykonania technik. Wzięliśmy pod lupę 180 kopnięć okrężnych wykonanych przez mistrzów Taekwon-do, aby sprawdzić różnice biomechaniczne między wykonaniem tradycyjnym a sportowym.", "Different competitions require different executions of techniques. We analyzed 180 roundhouse kicks performed by Taekwon-do masters to check the biomechanical differences between the traditional and sports execution."),
    ("Algorytmy na tropie stresu. Co determinuje lęk u młodych mężczyzn?", "Algorithms Tracking Stress. What Determines Anxiety in Young Men?"),
    ("Sztuczna inteligencja pomaga nam analizować nie tylko ruch, ale i ludzką psychikę. Zobacz, jak wykorzystaliśmy algorytmy uczenia maszynowego (Machine Learning) do zbadania poziomu lęku i stresu w sytuacjach kryzysowych.", "Artificial intelligence helps us analyze not only movement but also the human psyche. See how we utilized machine learning algorithms to investigate anxiety and stress levels in crisis situations."),
    ("Cena pełnego kontaktu. Analiza kontuzji w Karate Kyokushin.", "The Price of Full Contact. Injury Analysis in Kyokushin Karate."),
    ("Karate Kyokushin uchodzi za jeden z najtwardszych sportów walki na świecie. Przeanalizowaliśmy historię urazów 61 elitarnych zawodników, aby sprawdzić, co najczęściej ulega uszkodzeniu na macie i jak skutecznie temu zapobiegać.", "Kyokushin Karate is considered one of the toughest combat sports in the world. We analyzed the injury histories of 61 elite competitors to see what gets damaged most often on the mat and how to effectively prevent it."),
    ("Wirtualna Rzeczywistość (VR) w fizjoterapii. Jak technologia chroni przed urazami?", "Virtual Reality (VR) in Physiotherapy. How Technology Protects Against Injuries?"),
    ("Gogle VR to nie tylko rozrywka dla graczy. Zobacz, jak wykorzystaliśmy wirtualną rzeczywistość do badania reakcji obronnych i zapobiegania groźnym upadkom m.in. u osób starszych.", "VR headsets aren't just entertainment for gamers. Discover how we utilized virtual reality to study defense reactions and prevent dangerous falls, especially among the elderly."),
    ("Taekwondo jako terapia. Jak sztuki walki redukują agresję?", "Taekwondo as Therapy. How Martial Arts Reduce Aggression?"),
    ("Sporty walki często kojarzą się z agresją. Nasza analiza udowadnia jednak, że adaptacja zasad Para Taekwondo może stanowić potężne narzędzie w terapii behawioralnej osób z niepełnosprawnością intelektualną.", "Combat sports are often associated with aggression. However, our analysis proves that adapting Para Taekwondo rules can be a powerful tool in behavioral therapy for individuals with intellectual disabilities."),
    ("Czy do bólu można się przyzwyczaić? Percepcja bólu w Muay Thai.", "Can You Get Used to Pain? Pain Perception in Muay Thai."),
    ("Tajski boks to jeden z najbrutalniejszych sportów uderzanych. Zbadaliśmy próg bólu u zawodowców i amatorów, aby sprawdzić, czy lata przyjmowania ciosów potrafią \"przeprogramować\" układ nerwowy.", "Thai boxing is one of the most brutal striking sports. We tested the pain thresholds of professionals and amateurs to see if years of taking hits can \"reprogram\" the nervous system.")
]

for pl_title, en_title in title_translations:
    hub_content = hub_content.replace(pl_title, en_title)

# Update href links for all articles
for pl_file, en_file in articles.items():
    hub_content = hub_content.replace(f'href="{pl_file}"', f'href="{en_file}"')

with open('publications-en.html', 'w', encoding='utf-8') as f:
    f.write(hub_content)

print("Patching complete!")
