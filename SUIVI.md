# Suivi du projet

Une entrée par session de travail, la plus récente en haut. On y note ce qui a été fait, les décisions prises, ce qui reste à faire et les liens utiles.

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
