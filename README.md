# Carnet de quart

App web gamifiée pour apprendre la voile (théorie et pratique) à bord d'un Jeanneau Sun Odyssey 40.3.

## Liens

| Quoi | Lien |
|---|---|
| App en ligne (GitHub Pages) | https://pittilloni.github.io/carnet-de-quart/ |
| Code source | https://github.com/PITTILLONI/carnet-de-quart |
| Version artifact Claude (privée, réservée au propriétaire) | https://claude.ai/artifact/Rpr4m7joJdQdR4EPg2eyD9 |
| Journal de suivi du projet | [SUIVI.md](SUIVI.md) |
| Décisions de design | [design-system/carnet-de-quart/MASTER.md](design-system/carnet-de-quart/MASTER.md) |

- **Théorie** : 10 modules (vocabulaire, allures, réglages, manœuvres, matelotage, balisage IALA région A, règles de barre et feux, météo, navigation et marées, sécurité), avec des quiz à répétition espacée.
- **Entraînements** : jeu des allures et amures, jeu des balises.
- **À bord** : 19 missions pratiques, une fiche de repères du bateau et un journal de bord.
- **Carnet** : XP, grades, série de jours, badges.

## Installer l'app sur ton téléphone

C'est une web app installable (PWA). Une fois ouverte une première fois, elle fonctionne **hors ligne**, en mer sans réseau.

- **iPhone (Safari)** : ouvre https://pittilloni.github.io/carnet-de-quart/, touche le bouton Partager, puis « Sur l'écran d'accueil ».
- **Android (Chrome)** : ouvre le lien, menu ⋮, puis « Installer l'application » (ou « Ajouter à l'écran d'accueil »).

La progression reste enregistrée sur le téléphone (localStorage). Elle ne se synchronise pas entre appareils. La page tient en un seul fichier, sans dépendance à part la police Archivo (Google Fonts). La progression est enregistrée dans le navigateur (localStorage).

- `carnet-de-quart.html` : **source à modifier**. C'est aussi la version publiée comme artifact Claude.
- `build.py` : génère `index.html` (la web app) à partir de la source. Lance `python3 build.py` après chaque modification.
- `index.html` : web app générée (en-tête HTML, manifeste, service worker).
- `manifest.webmanifest`, `sw.js`, `icons/` : installation et mode hors ligne. Change `VERSION` dans `sw.js` à chaque mise à jour.
- `design-system/carnet-de-quart/MASTER.md` : décisions de design.

## Sources

Le contenu a été vérifié sur des sources publiques, listées dans l'onglet Carnet de l'app : Wikipédia (fiche du Sun Odyssey 40.3), Météo-France (BMS), Environnement Canada (échelle de Beaufort), ministère de la Mer (196, VHF 16), RIPAM et IALA, Bateaux.com, Figaro Nautisme. Pour approfondir : le Cours des Glénans.

### Liens des sources

- [Sun Odyssey 40.3, Wikipédia](https://en.wikipedia.org/wiki/Sun_Odyssey_40.3)
- [BMS, Météo-France sur data.gouv.fr](https://www.data.gouv.fr/datasets/bulletin-meteorologique-special-annuel)
- [Échelle de Beaufort, Environnement Canada](https://www.canada.ca/fr/environnement-changement-climatique/services/renseignements-generaux-conditions-maritimes/description-previsions-meteo/tableau-echelle-beaufort.html)
- [Alerter les secours en mer, ministère de la Mer](https://www.mer.gouv.fr/comment-alerter-les-secours-en-mer)
- [Règles RIPAM et balisage IALA](https://ialacolreg.com/fr/colreg)
- [Cône noir du voilier au moteur, Bateaux.com](https://www.bateaux.com/article/42271/mais-que-signifie-ce-cone-noir-envoye-sur-ce-voilier)
- [Lire les penons, Bateaux.com](https://www.bateaux.com/article/33442/ecouter-ce-que-les-penons-ont-a-nous-dire-le-genois)
- [Effet de pas d'hélice, Bateaux.com](https://www.bateaux.com/article/27289/se-servir-de-l-effet-de-de-l-helice-reussir-manoeuvre-de-port)
- [Longueur de chaîne au mouillage, Figaro Nautisme](https://figaronautisme.meteoconsult.fr/actus-nautisme-bateaux/2026-10-28/93615-les-pieges-du-mouillage-quelle-longueur-de-chaine-est-vraiment-necessaire)
- [Premières manœuvres avec les Glénans, Figaro Nautisme](https://figaronautisme.meteoconsult.fr/actus-nautisme-bateaux/2020-07-08/55651-debuter-la-voile-avec-les-glenans-episode-2-comment-realiser-les-premieres-manoeuvres)
- [Balisage maritime, digischool](https://www.digischool.fr/articles/bateau/balisage-maritime-permis-bateau/)
