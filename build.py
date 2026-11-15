"""Génère index.html (web app GitHub Pages) à partir de carnet-de-quart.html (version artifact).
Usage : python3 build.py"""
src = open("carnet-de-quart.html", encoding="utf-8").read()
j = src.index("</style>") + len("</style>")
head = """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="Apprendre la voile : théorie, quiz, jeux et missions à bord d'un Sun Odyssey 40.3.">
<meta name="theme-color" content="#0B2545">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icons/icon-192.png" type="image/png">
<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Carnet">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
"""
base = "<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}[hidden]{display:none!important}</style>\n"
sw = """<script>if("serviceWorker" in navigator){addEventListener("load",()=>navigator.serviceWorker.register("sw.js").catch(()=>{}))}</script>\n"""
out = head + src[:j] + "\n" + base + "</head>\n<body>\n" + src[j:] + "\n" + sw + "</body>\n</html>\n"
open("index.html", "w", encoding="utf-8").write(out)
print("index.html généré")
