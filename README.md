
![Logo](https://github.com/Jorre-student/Tabula-Captiva/blob/main/readme/logo%20tabula.png?raw=true)

Tabula Captiva is een immersive storytelling experience die je meeneemt in het leven van geïnterneerden, mensen met psychische problemen die opgesloten worden zonder strafrechtelijke veroordeling, in de gevangenis van de Begijnenstraat.


In een nagebouwde cel ontdek je hun verhalen via interactieve meubels uit de gevangenis zelf. Door aanraking activeren ze soundscapes en dynamische lichteffecten, aangestuurd via Python op een Raspberry Pi, waarbij Pygame wordt gebruikt voor de audio.

[Bekijk onze Aftermovie](https://www.youtube.com)
## Materials
- Technologie
    - ...
- Ruimte
    - ...
- Decoratie
    - ...


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
Here i will explain how to build the jail

### Wooden Frame
This part will explain how to build the frame
<p>
  <img src="https://github.com/Jorre-student/Tabula-Captiva/blob/main/readme/cel1.jpeg?raw=true" alt="cel frame" width="22%"/>
  <img src="https://github.com/Jorre-student/Tabula-Captiva/blob/main/readme/cel2.jpeg?raw=true" alt="cel frame" width="22%"/>
  <img src="https://github.com/Jorre-student/Tabula-Captiva/blob/main/readme/cel3.jpeg?raw=true" alt="cel frame" width="22%"/>
</p>

#### Scharnieren
Text will come here
#### Hout
Text will come here
#### Walls
This part will explain how to build the frame
### Technology
This part will explain how to install the technology in the jail
#### Buttons
Text will come here
#### Lamps
Text will come here
#### Lights
Text will come here

### Decoration
This part will explain what decoration we used
#### onderdeel 1
Text will come here
## Belangrijke links

 - [Onze Website](https://tabula-captiva.onrender.com/)
 - [Github voor Onze Website](https://github.com/nienkeminnesma/2425_cc_groep3_installatiewebsite)
 - [Procesdocument](https://www.tabulacaptiva-proces.be/)
 - [Instagram](https://www.instagram.com/tabula_captiva/)
 - [Aftermovie](https://www.youtube.com)

