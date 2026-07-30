# Instrukcja dla Agenta Webowego (Web Developer Agent)

## Kontekst Projektu
Pracujemy nad platformą **BioKinEdu**, która oferuje innowacyjną usługę telerehabilitacji. Naszym głównym produktem jest zaawansowany program komputerowy zasilany sztuczną inteligencją (YOLOv8), który analizuje ruch i postawę pacjenta w czasie rzeczywistym.

## Kluczowe Funkcjonalności Oprogramowania
Nasz system telerehabilitacji działa w trybie wideokonferencji i składa się z dwóch głównych modułów analitycznych:
1. **Analiza Ruchomości (Joint Kinematics / Angular Analysis)** - Śledzi kluczowe stawy pacjenta i oblicza ich kąty oraz prędkość w czasie rzeczywistym.
2. **Analiza Balansu (Balance)** - Śledzi środek ciężkości (COG) pacjenta na podstawie ułożenia bioder i generuje na żywo mapę wychyleń oraz wykresy prędkości i przemieszczenia.

## Architektura Komunikacyjna
Cały proces telerehabilitacji odbywa się z zachowaniem najwyższych standardów prywatności:
- **Protokół:** Wykorzystujemy otwarty i zdecentralizowany protokół **Matrix** (po federacji).
- **Serwer:** Konferencje odbywają się na naszym prywatnym, w pełni szyfrowanym serwerze (Synapse) pod adresem: `matrix.biokineticum.com`.
- **Aplikacja kliencka:** Do prowadzenia rozmów wykorzystywana jest aplikacja **Element** (oficjalny, bezpieczny klient sieci Matrix). Nasz program przechwytuje obraz bezpośrednio z okna aplikacji Element uruchomionej u specjalisty.

## Twoje Zadanie
Jako Agent odpowiedzialny za rozwój strony internetowej (Web Developer), twoim zadaniem jest stworzenie lub rozbudowa serwisu internetowego, który będzie wizytówką tej usługi. 
Strona powinna jasno komunikować pacjentom i specjalistom:
- Że usługa opiera się na **prywatnych, szyfrowanych wideokonferencjach (Matrix/Element)**.
- Że podczas e-wizyty, specjalista korzysta z **analizy AI na żywo**, oceniając ruchomość stawów i balans bez potrzeby instalowania dodatkowych czujników przez pacjenta.
- Najwyższy priorytet kładziony jest na **nowoczesny, profesjonalny i godny zaufania design (Rich Aesthetics, Premium Design)** z wykorzystaniem płynnych animacji, eleganckiej palety barw i przemyślanego układu (UI/UX).

Przy projektowaniu witryny lub aplikacji webowej, pamiętaj o wytycznych dotyczących nowoczesnego designu (np. glassmorphism, dark/light modes) oraz SEO, aby platforma była atrakcyjna dla użytkowników szukających zaawansowanych usług telerehabilitacyjnych.
