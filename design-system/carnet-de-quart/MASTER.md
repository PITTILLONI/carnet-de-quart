# Carnet de quart — design system

Surface : outil / app (mobile first). Pro Max mène l'UX, Taste fixe l'anti-slop.

## Idée
Les pavillons du code international deviennent l'identité : aplats marine, jaune, rouge, blanc.
Le pavillon P (« on appareille ») marque le bouton principal « Prendre le quart du jour ».
Live thing : le simulateur Allures (bateau orienté au hasard sous le vent) et le jeu Balises.

## Tokens
- Couleurs (clair) : page #EEF2F6, panneau #FFFFFF, panneau-2 #E1E8F0, encre #0B2545, encre-2 #3F546C, marine #0B2545, jaune #F5C400, rouge #C8102E, vert #00804A, ciel (dessins) #D6E4EE.
- Sombre : page #061426, panneau #0E2138, panneau-2 #17304E, encre #EAF0F6, encre-2 #A9BACC, marine #123A66.
- Typo : Archivo seule (axe largeur). Titres 800 en largeur 112–125 %, texte 400 à 100 %.
- Échelle : 14 / 16 / 20 / 28 / clamp(56px, 17vw, 112px). Espacements 4-8-12-16-24-32-48.
- Rayons : 12–14 px (panneaux), 20 px (champ marine).

## Règles
- Pas de mono, d'eyebrow, de filets, de dégradés, d'ombres au repos (sauf toast), ni d'emoji : icônes SVG.
- Cibles tactiles ≥ 44 px, texte ≥ 16 px, focus jaune 3 px, prefers-reduced-motion respecté.
- Mouvement : 150–320 ms, transform seulement (entrée des blocs, appui, feuille de quiz, toasts).

## Exceptions Taste (--allow)
- few-pictures, no-real-pictures, no-footage : aucune photo libre de droits du Sun Odyssey 40.3 n'existe dans les collections ouvertes. Montrer un autre modèle serait trompeur.
- still-page : app de révision ; Pro Max limite le mouvement à 1 ou 2 éléments par vue.
- covered-text : c'est la barre d'onglets fixe en bas, un motif d'app normal. Le contenu garde une marge pour passer dessous.
