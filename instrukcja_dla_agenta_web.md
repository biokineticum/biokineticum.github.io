# Instrukcja dla Agenta Webowego (Web Developer Agent)

## Kontekst Projektu
Pracujemy nad platformą **Biokineticum / BioKinEdu**, która oferuje innowacyjną usługę telerehabilitacji oraz bezpłatne oprogramowanie biomechaniczne Open Source. Naszym kluczowym narzędziem analitycznym jest program komputerowy zasilany sztuczną inteligencją (m.in. YOLOv8), który analizuje ruch i postawę pacjenta w czasie rzeczywistym.

## Kluczowe Funkcjonalności Oprogramowania
Nasz system telerehabilitacji działa w trybie bezpiecznych wideokonferencji i składa się z dwóch głównych modułów analitycznych:
1. **Analiza Ruchomości (Joint Kinematics / Angular Analysis)** - Śledzi kluczowe stawy pacjenta i oblicza ich kąty oraz prędkość w czasie rzeczywistym.
2. **Analiza Balansu (Balance)** - Śledzi środek ciężkości (COG) pacjenta na podstawie ułożenia bioder i generuje na żywo mapę wychyleń oraz wykresy prędkości i przemieszczenia.

## Architektura Komunikacyjna & Prywatność
Cały proces telerehabilitacji odbywa się z zachowaniem najwyższych standardów prywatności i bez konieczności utrzymywania własnych kosztownych serwerów wideokonferencji:
- **Komunikatory:** Łączymy się za pośrednictwem szyfrowanych połączeń (End-to-End Encryption) w zaufanym komunikatorze wybranym przez pacjenta (np. **Signal, Telegram, WhatsApp, Session, FaceTime, Google Meet, Jitsi**).
- **Płatności:** Oprócz standardowych przelewów bankowych, akceptujemy płatności w kryptowalutach (**Bitcoin, Monero, USDT**).
- **Zero LLM:** Nie używamy modeli językowych do przetwarzania danych wideo – analiza jest w 100% lokalna i numeryczna.
