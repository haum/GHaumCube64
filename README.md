# GHaumCube64

Le GHaumCube64 est un jeu lumineux tridimentionnel sous forme de cube suspendu dans les airs.

État du projet : En cours

## Description générale

À l'heure actuelle, le projet est définit comme étant un cube de 64 (4×4×4) tåls (nom inventé pour désigner les éléments lumineux, munis chacun de trois leds multicolores adressables), orienté sur sa pointe et suspendu ; il y a aussi une manette de jeu à lui adjoindre. L'objectif est d'y programmer des jeux tels que morpion/snake/tron en 3D.

## Organisation des fichiers

```
<repo>
├── code
│   ├── cube <= Code du cube
│   └── remote <= Code de la télécommande/manette de jeu
│   └── Tal_test <= Code de test des LEDs
└── structure
    ├── placement
    │   ├── cube.blend <= disposition des tåls dans l'espace
    │   └── placement.scad <= disposition des tåls dans l'espace, d'un point de vue fabrication
    └── tal
        ├── tal.blend <= Modèle d'un tål complet
        ├── tal_bottom.stl.xz <= Export STL (compressé) de la partie basse
        ├── tal_top.stl.xz <= Export STL (compressé) de la partie haute
        └── Ball
            ├── support_led_Tal.FCStd <= Support LEDs FreeCAD file
            └── support_led_Tal.stl <= Export STL du support de LEDs
```
