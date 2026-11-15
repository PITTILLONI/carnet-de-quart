# Suivi du projet

Une entrée par session de travail, la plus récente en haut. On y note ce qui a été fait, les décisions prises, ce qui reste à faire et les liens utiles.

---

## 2026-11-15 (suite) — Web app installable et accessible

### Fait
- **Web app installable (PWA)** :
  - Manifeste `manifest.webmanifest`.
  - Icônes au pavillon P (192, 512, maskable, Apple 180).
  - Couleur de thème marine, mode plein écran (standalone).
- **Hors ligne** : service worker `sw.js`. L'app et la police sont mises en cache à la première ouverture ; la page passe d'abord par le réseau pour recevoir les mises à jour.
- **Build** : `build.py` génère `index.html` (web app) à partir de `carnet-de-quart.html` (source, aussi publiée comme artifact).
- **Accessibilité** :
  - Plus de titres à l'intérieur des boutons ; la hiérarchie des titres est corrigée dans les fiches.
  - Quand un quiz ou un jeu est ouvert, l'arrière-plan devient inactif (`inert`), Échap ferme, et le focus revient au bouton d'origine.
  - Audit axe-core 4.10 (WCAG 2.0 et 2.1 A/AA, bonnes pratiques) : **0 violation sur les 8 écrans** (accueil, théorie, module, à bord, carnet, quiz, allures, balises).
- README : mode d'emploi pour installer l'app sur iPhone et Android, rôle de chaque fichier.

### Décisions
- Lighthouse n'a pas pu tourner (npm n'a pas accès au réseau dans le bac à sable de Claude) : axe-core, le moteur d'accessibilité de Lighthouse, a été utilisé à la place.
- À chaque mise à jour : modifier `carnet-de-quart.html`, lancer `python3 build.py`, changer `VERSION` dans `sw.js`.

### À faire / idées
- Installer l'app sur un vrai iPhone et un vrai Android, puis tester le mode avion.
- Tester avec VoiceOver et TalkBack.

---

## 2026-11-15 — Création, refonte et mise en ligne

### Fait
- **Version 1** : app en un seul fichier HTML.
  - 10 modules de théorie, avec des quiz à répétition espacée (boîtes de 0 à 5).
  - Jeux : allures et amures, balises (région A).
  - 19 missions pratiques à bord, fiche de repères du bateau, journal de bord.
  - XP, 6 grades, série de jours, 13 badges.
- **Vérification du contenu** sur des sources publiques (liste dans le README). Corrections :
  - Tirant d'eau du 40.3 : 1,95 m en quille standard, 1,50 m en quille courte (et non « environ 2 m »).
  - Génois partiellement roulé : on **avance** le point de tire (et non on le recule).
  - Mouillage : 3 fois la profondeur au minimum par temps calme, 5 fois ou plus dès que le vent se lève.
  - Annonces : « Paré à virer ? » / « Paré ! » / « Virez ! », et la même chose pour l'empannage.
  - Cône noir pointe en bas porté à l'avant (règle 25 du RIPAM).
  - Précisions ajoutées : BMS côte dès force 7 et large dès force 8 ; 196 gratuit mais la VHF 16 reste prioritaire.
  - Retiré : tout ce qui n'était pas vérifiable.
- **Refonte du design** avec /design-combo (mobile first) :
  - Identité tirée des pavillons du code international ; le pavillon P marque le bouton principal.
  - Une seule police (Archivo), texte de 16 px minimum, cibles tactiles de 44 px minimum, mode clair et mode sombre.
  - Anti-slop : 0 erreur. Inspecteur en navigateur : 1 avertissement justifié (barre d'onglets fixe).
- **Mise en ligne** :
  - Dépôt GitHub créé, puis passé en public pour pouvoir activer GitHub Pages.
  - Site publié sur GitHub Pages.

### Décisions
- Ne rien inventer : chaque fait doit venir d'une source publique citée. Le Cours des Glénans reste la référence pour approfondir.
- Pas de photo : il n'existe pas de photo libre de droits d'un Sun Odyssey 40.3, et montrer un autre modèle serait trompeur.
- La progression est enregistrée dans le navigateur (localStorage). Elle ne se synchronise pas entre appareils.

### À faire / idées
- Tester sur un vrai téléphone (iPhone et Android).
- Remplir la fiche « Repères de ton bateau » avec les vrais chiffres : moteur, sens du pas d'hélice, tirant d'air.
- Comparer les formulations avec l'édition du Cours des Glénans que tu as.
- Éventuellement : synchroniser la progression entre appareils, ajouter des modules (feux de nuit détaillés, calcul de marée).

### Liens
- App : https://pittilloni.github.io/carnet-de-quart/
- Dépôt : https://github.com/PITTILLONI/carnet-de-quart
- Artifact (privé) : https://claude.ai/artifact/Rpr4m7joJdQdR4EPg2eyD9
