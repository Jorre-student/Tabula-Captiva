![Logo](https://github.com/Jorre-student/Tabula-Captiva/blob/main/readme/logo%20tabula.png?raw=true)
Tabula Captiva is een immersive storytelling experience die je meeneemt in het leven van geïnterneerden, mensen met psychische problemen die opgesloten worden zonder strafrechtelijke veroordeling, in de gevangenis van de Begijnenstraat.


In een nagebouwde cel ontdek je hun verhalen via interactieve meubels uit de gevangenis zelf. Door aanraking activeren ze soundscapes en dynamische lichteffecten, aangestuurd via Python op een Raspberry Pi, waarbij Pygame wordt gebruikt voor de audio.

[Bekijk onze Aftermovie](https://www.youtube.com)
## Materials
- Technologie
    - ...
- Ruimte
    - grenen geschaafd 22mm x 45mm:
        - 16x 2,40m
        - 6x 2,70m
        - 7x 3,00m
    - 12 x bouten
    - 8 x scharnieren
    - kartonnen panelen
    - 2 zwarte theaterdoeken
    - dozen voor de knoppen
- Decoratie
    - Kleding (sokken, broek, trui)
    - Bed + matras + Bed overtrek + laken
    - Houten stoel
    - Bureau
    - Wc + Wastafel zelf te maken
    - 2 Posters


## Code
### Doel van het script

Het doel van bijgevoegde code is het aansturen van fysieke knoppen die elk een specifiek audiobestand afspelen en tegelijkertijd een bijbehorende lamp inschakelen via MQTT. Na het afspelen wordt de lamp automatisch weer uitgeschakeld op basis van een vooraf ingestelde tijdsduur.



### Benodigdheden

- Raspberry Pi met GPIO-ondersteuning
- 7 fysieke knoppen aangesloten op GPIO-pinnen: [17, 6, 14, 23, 25, 21, 22]
- geluid via HDMI of audio-uitgang
- werkende Zigbee2MQTT broker
- Zigbee-lampen met namen zoals "lamp1", "lamp2", etc.




### Externe Libaries
 RPI.GPIO → uitlezen van knoppen via GPIO-pinnen 

pygame → afspelen van mp3-geluidsfragmenten

paho.mqtt.client → communicatie met de Zigbee2MQTT broker (aansturen van lampen via MQTT)



### Belangrijk!

pygame & paho.mqtt dienen zelf via de terminal geïnstalleerd te worden en staan niet standaard op de Raspberry Pi. 

Installeer benodigde paketten met volgende code in de terminal:
```bash
pip install pygame paho-mqtt
```



### Belangrijke onderdelen in het script

GPIO button setup  → gaat over fysieke knoppen – werkt niet bij verkeerde pin-aansluitingen


audio_files + durations  → elke knop speelt een specifiek mp3-bestand af gedurende een vastgelegde tijdsduur


MQTT COMMUNICATIE → stuurt aan/uit-signalen naar lampen via MQTT


PYGAME DEVICE INIT → fout in audiodevice → geen geluid 


opmerking: er kan ook gebruik gemaakt worden van de aanwezige audio-uitgang in de Raspberry Pi (beperkte geluidskwaliteit), in dat  geval kan dit deeltje code weggelaten worden


WHILE TRUE lus → dit is de hoofdloop die knoppen detecteert en acties uitvoert





### Mogelijke valkuilen

AUDIODEVICE → als het audiodevice niet bestaat of fout ingesteld is, wordt er geen geluid afgespeeld      controleer je audiodevice via de terminal met: aplay -L


MQTT BROKER CONFIGURATIE → het IP-adres in de code (broker_address) moet overeenkomen met jouw eigen Zigbee2MQTT broker      gebruik een vast IP of hostname om verbindingsproblemen te voorkomen


LAMPNAMEN (MQTT) → de MQTT-onderwerpen gebruiken "lamp1", "lamp2", enz.      zorg dat deze overeenkomen met de friendly names in Zigbee2MQTT


GPIO PIN-CONFIGURATIE → de knop-pinnen in de code moeten overeenkomen met je fysieke aansluitingen      verkeerde pin = geen reactie!


AUDIO-DUUR KOMT NIET OVEREEN → de tijdsduur (durations) moet overeenkomen met de echte lengte van elk mp3-bestand     controleer de lengte van het audiobestand via de terminal met: ffprobe bestandnaam.mp3


## Cel nabouwen

### Frame
Voor onze cel hebben we grenen geschaafd 22mm x 45mm gebruikt, dit is stabiel genoeg, als het iets is dat je wat langer wilt laten staan kan je best een stevigere lat kopen.

#### Afmetingen nodig voor installatie:
15 x 2,10m
6 x 250m
8 x 150m
2 x 100m

#### Afmetingen en hoeveelheid van elk hout als je het in de houtshop gaat kopen.
16 x 2,40m
6 x 2,70m
7 x 3,00m
=> Nadien af te zagen om naar de juiste lengtes te brengen
=> Het overtollige hout word gebruikt om de schuine kantjes te maken in de hoeken, voor extra stabiliteit. Zie schets hieronder.

 <img src="https://github.com/Jorre-student/Tabula-Captiva/blob/main/readme/afmetingencel.png?raw=true" alt="cel schets" width="80%"/>

### Monteren 
Nadat alles gezaagd is naar de juiste lengte kan je het in elkaar gaan puzzelen. Zoals op de schets hierboven we bouwen per muur, hierdoor zal elke hoek 2 latten hebben die gebruikt zullen worden om nadien het makkelijker in elkaar te krijgen.

Je kan best eerste alles goed leggen om vervolgens alles in elkaar te vijzen. => Hiervoor heb je verschillende vijzen nodig:
Je hebt vijzen nodig om het gewone frame te maken, deze mogen elke lengte zijn maar best meer als 6cm zodat het zeker stevig vast zit.
Ook heb je vijzen nodig voor de schuine latjes, deze moeten klein genoeg zijn zodat ze er niet langs de andere kant uitkomen. Aan te raden is een vijs van 3-3,5cm.

Als dit allemaal in elkaar zit heb je het belangrijkste werk gedaan, vervolgens zet je de hele cel eens op en kan je deze vastzetten met enkele klemmen zodat hij blijft rechtstaan.

<img src="https://github.com/Jorre-student/Tabula-Captiva/blob/main/readme/cel2.jpeg?raw=true" alt="cel frame" width="40%"/>
  
Hier kan je ervoor kiezen om elk frame in 2 te zagen en enkele scharnieren te plaatsen zodat het gemakkelijker verplaatst of je kan het in zijn geheel laten. Vervolgens boor je in elke dubbele lat (dus op alle hoeken) een gat van 8mm, dit doe je 3 keer per hoek. Hierna kan je er bouten in steken zodat de cel op zichzelf kan blijven staan zonder de klemmen.

### Muren & verbindingen
Als muren hebben we karton gebruikt, dit zorgde ervoor dat de installatie snel en gemakkelijk verder in elkaar kon worden gezet. Optimaal gebruik je hier iets steviger voor, maar karton vastmaken met nagels of vijzen kan perfect werken en het juiste gevoel geven.

Hieronder zie je een digitale tekening van hoe de ruimte verbonden is aan alle knoppen en waar er allemaal verbindingen moeten zijn. De grote oranje bol is het verzamel punt van alle kabels, dit is waar ook de computer staat en de besturing voor als er iets misloopt.

De lampen zelf hingen niet op de groene bollen, maar in het midden van de ruimte aan de 2 bovenste latten die diende voor stevigheid.

<img src="https://github.com/Jorre-student/Tabula-Captiva/blob/main/readme/plattegrond%20cel.png?raw=true" alt="cel frame" width="80%"/>
Op verschillende plekken in de cel zijn er gaten, hierdoor steek je telkens de kabels. Deze gaten maak je best onderaan de muur, zodat ze het minst opvallen.
Wanneer je de lampen opgehangen hebt aan de twee balken op het dak kan je het dak erop vastmaken, dit hebben wij ook met karton gedaan en met een doek langs de voorkant voor wat meer privacy, aangezien we geen deur hadden. Dit valt zelf te kiezen.

### Decoratie
Als laatste kan je de meubels en alle decoratie die je verzameld hebt in de installatie zetten, deze moeten een beetje gevangenis uitstraling hebben. Ook de verschillende accesoires zoals handdoek, eten, bedlinnen, kleding, ... kunnen leuk zijn om het verder aan te kleden.

Ook de buttons kunnen dan geplaatst worden op de verschillende plaatsen.

## Buttons
In de cel heb je verschillende buttons waarop je kan klikken, deze triggeren de lampen en het geluid. Maar omdat deze niet los gelegd kunnen worden hebben we eerst een doos gemaakt waar deze in kunnen worden gestoken.
In totaal hebben we 2 dozen gemaakt:

- 1 doos dient om echt in de installatie te zetten die ook door iedereen gezien kan worden. Deze werden gemaakt aan de hand van dit sjabloon: ‘dozen groot’

<img src="https://github.com/Jorre-student/Tabula-Captiva/blob/main/readme/Doos%201.png?raw=true" alt="cel frame" width="40%"/>

- De andere dozen waren voor aan de buitenkant van de installatie te hangen sjabloon: ‘dozen klein’
<img src="https://github.com/Jorre-student/Tabula-Captiva/blob/main/readme/Doos%202.png?raw=true" alt="cel frame" width="40%"/>

Deze kun je dan aan de buitenkant vastmaken zodat de knop in de muur kan worden bevestigd.

## Kartonnen meubels
### Stap 1:
Bestanden tekenen in Sketchup (in 3D), nadien uitvouwen in illustrator bestanden
<p> 
    <img src="https://github.com/Jorre-student/Tabula-Captiva/blob/main/readme/wc1.png?raw=true" alt="cel frame" width="40%"/>
    <img src="https://github.com/Jorre-student/Tabula-Captiva/blob/main/readme/Wastafel1.png?raw=true" alt="cel frame" width="40%"/>
</p>   

### Stap 2:
De snijplotter is niet groot genoeg, dus moeten de stukken uiteengehaald worden. Hierbij moeten dustflaps toegevoegd worden om nadien de delen terug aan elkaar te lijmen.

#### Bestanden voor de wc:
<img src="https://github.com/Jorre-student/Tabula-Captiva/blob/main/readme/Bestanden%20WC.png?raw=true" alt="cel frame" width="40%"/>
    
#### Bestanden voor de wastafel
<img src="https://github.com/Jorre-student/Tabula-Captiva/blob/main/readme/Bestanden%20Wastafel.png?raw=true" alt="cel frame" width="40%"/>

### Stap 3:
In illustrator rillijnen (rode kleur) & snijlijnen (zwarte kleur) toevoegen. De rillijnen gaan in de map met Crease, de snijlijnen in Thru-cut.
<img src="https://github.com/Jorre-student/Tabula-Captiva/blob/main/readme/stap3%20meubels.png?raw=true" alt="cel frame" width="20%"/>

### Stap 4:
Maak een printklare PDF 
### Stap 5:
Stel de snijplotter in en snij de bestanden uit 
### Stap 6:
Lijm alle delen aan elkaar en werk af met een zilveren spray
<p> 
<img src="https://github.com/Jorre-student/Tabula-Captiva/blob/main/readme/eindresultaat%20wc.png?raw=true" alt="cel frame" width="40%"/>
<img src="https://github.com/Jorre-student/Tabula-Captiva/blob/main/readme/eindresultaat%20wastafel.png?raw=true" alt="cel frame" width="40%"/>
</p>   

## Prikbord
Software: Blender

### Stap 1: 
Voeg een kubus toe.
Schaal de kubus plat en rechthoekig, zodat het de vorm krijgt van een prikbord.
Geef de kubus een kurk-materiaal, zodat het lijkt op een echt prikbord.

### Stap 2: 
Voeg een plat vlak toe voor elk briefje.
Schaal het vlak tot papierformaat.
Voeg tekst toe op het papier:
Gebruik een afbeelding met tekst als materiaal.
Of voeg een tekstobject toe en leg het op het vlak.

### Stap 3:
Maak meerdere versies van een briefje, elk met andere tekst.
Zet per moment in de tijdlijn aan welk briefje zichtbaar is.
Laat de tekst zo veranderen tijdens de animatie.

### Stap 4: 
Animeer elk briefje zodat ze in de frame vliegen en daarna terug vallen.

### Stap 5:
Plaats een camera voor het prikbord.
Voeg één of meer lampen toe om alles goed te verlichten.
Gebruik eventueel achtergrondlicht voor een natuurlijke sfeer.

### Stap 6: 
Stel het aantal frames in voor de lengte van de animatie.
Kies een videoformaat voor de uitvoer.
Render de animatie en sla deze op als video.

### Video:
<iframe src="https://apbe-my.sharepoint.com/personal/s151295_ap_be/_layouts/15/embed.aspx?UniqueId=bc8ea0e8-d5ae-42a6-9534-6a3bd2e6f7ab&embed=%7B%22ust%22%3Atrue%2C%22hv%22%3A%22CopyEmbedCode%22%7D&referrer=StreamWebApp&referrerScenario=EmbedDialog.Create" width="640" height="360" frameborder="0" scrolling="no" allowfullscreen title="FinalVideoCCmp4.mp4"></iframe>


## Eindresultaat
Uiteindelijk zag onze cel er zo uit, met alle inhoud en de verschillende knoppen.

<img src="https://github.com/Jorre-student/Tabula-Captiva/blob/main/readme/eindresultaat.png?raw=true" alt="cel frame" width="80%"/>

## Belangrijke links

 - [Onze Website](https://tabula-captiva.onrender.com/)
 - [Github voor Onze Website](https://github.com/nienkeminnesma/2425_cc_groep3_installatiewebsite)
 - [Procesdocument](https://www.tabulacaptiva-proces.be/)
 - [Instagram](https://www.instagram.com/tabula_captiva/)
 - [Aftermovie](https://www.youtube.com)

