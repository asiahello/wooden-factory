# wooden-factory

Chat-GPT prompt:

Chcę przeprowadzić szkolenie dla 3 technologów drewna, którzy ze mną współpracują 
i chcieliby nauczyć się programować w pythonie. 

Na początek chcę im pokazać jak działa git, repozytorium, branche, commity, pull requesty i konflikty. 
Mam taki pomysł, żeby zrobić repozytorium wooden-factory i tam zamieścić kilka programów: 
- wybór płyty na podstawie typu mebla, 
- wybór wierteł na podstawie typu otworu, 
- wybór okuć na podstawie typu elementu 
- pakowanie elementów w paczki bazując na maksymalnej wadze paczki. 

Fabryka ma produkować mebelki składające się z elemetów: horizontale, verticale i back. 
Każdy element powinien mieć swój wymiar w mm (grubość płyty zawsze 18mm) i dane o materiałach 
potrzebnych do jego wyprodukowania: jaka płyta, jakie okucia i gdzie te okucia powinny się znaleźć. 

Musimy umieć policzyć wagę elementu (płyty + okuć), musimy umieć stwierdzić w ile paczek spakuje się mebel 
(pomińmy ułożenie elementów w paczkach, niech limituje nas sama waga). Meble powinny mieć na początek główną zasadę, 
że mają otwarcia 50x50cm. 

Chcę żeby były dwa typy mebla: hotty i vetty - te typy określają sposób w jaki jest budowany mebel. 
Gdy chcę zrobić szafkę hotty o wymiarach 100cm szerokości i 200cm wysokości, 
to szafka powinna składać się z 5 horizontali o wymiarze 100cm i 12 verticalach o wymiarze 50cm. 
Gdy chcę szafkę o tych samych wymiarach ale w typie vetty, 
powinna się utworzyć taka z 3 dużymi verticalami o wysokości 200cm i 10 horizontalami o szerokości 50cm. 

Poproszę o przykładowy projekt w pythonie na taki program - na razie bez bazy danych, czysty python + testy w pytest. 

Przy budowie szafki nie uwzględniajmy na razie pleców. 
Aha, i przydałby się jakiś sposób podejrzenia wygenerowanej szafki (wizualny).

# contributors:
- baju
- -krzys