# Odroid N2+ GPIO Info Add-on

Deze add-on geeft een overzicht van alle GPIO pins (lijnen) op de Odroid N2+ (Home Assistant Blue). De informatie wordt bij het starten eenmalig verzameld en naar de add-on log geschreven, vergelijkbaar met de output van het `gpioinfo` commando in Linux.

## Wat doet deze add-on?

- **GPIO chip detectie:** Alle GPIO chips op het systeem worden uitgelezen (bijv. `gpiochip0`, `gpiochip1`, ...).
- **Lijnenoverzicht:** Per chip worden alle lijnen gelijst met hun offset, naam (indien beschikbaar), huidige gebruiker (of "unused"), de richting (input of output) en of de lijn active-high of active-low is geconfigureerd.
- **Alle output in de log:** De resultaten verschijnen in de Home Assistant add-on log. U kunt deze bekijken via Supervisor -> Add-ons -> Odroid N2+ GPIO Info -> Log.

Deze add-on is read-only en **verandert geen enkele GPIO-stand**; hij rapporteert alleen de huidige configuratie.

## Installatie

1. Kopieer de bestanden `config.json`, `Dockerfile`, `run.py` en `README.md` naar een map `odroid_gpio_info` in uw lokale add-ons folder (bij Home Assistant OS of Supervised installaties is dit meestal de `addons` share).
2. Voeg de nieuwe add-on toe via het Home Assistant Supervisor panel:
   - Ga naar **Instellingen** > **Add-ons** > **Add-on store**.
   - Klik rechtsboven op de menu-knop en kies **Opslagplaats toevoegen**.
   - Voeg het pad naar uw lokale add-on repository toe (of gebruik de optie **beheer lokale add-ons** indien beschikbaar om de add-on te laden).
3. Zoek de **Odroid N2+ GPIO Info** add-on in de lijst en installeer deze.
4. Start de add-on handmatig op (de add-on start niet automatisch bij boot, aangezien `boot` op manual staat).

## Gebruik

Open na het starten het Logboek van de add-on om de output te zien. U zou een lijst van GPIO chips en lijnen moeten zien. Bijvoorbeeld:

