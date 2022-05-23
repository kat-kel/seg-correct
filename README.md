# Seg-Correct

This tool is designed to help the [Gallic(orpor)a](https://github.com/Gallicorpora) project's contributors better detect segmentation issues with HTR documents pushed to the project's repositories. A log of these issues is automatically generated using [HTR United's](https://htr-united.github.io/) HTRVX tool, which Gallic(orpor)a implements through GitHub Actions.

HTR-United workflows for each Gallic(orpor)a repository:
- Manuscrits - [15e Siècle](https://github.com/Gallicorpora/HTR-MSS-15e-Siecle/actions/workflows/htr-united.yml)
- Incunables - [15e Siècle](https://github.com/Gallicorpora/HTR-incunable-15e-siecle/actions/workflows/htr-united.yml)
- Imprimés - [16e Siècle](https://github.com/Gallicorpora/HTR-imprime-16e-siecle/actions/workflows/htr-united.yml)
- Imprimés - [17e Siècle](https://github.com/Gallicorpora/HTR-imprime-17e-siecle/actions/workflows/htr-united.yml)
- Imprimés - [18e Siècle](https://github.com/Gallicorpora/HTR-imprime-18e-siecle/actions/workflows/htr-united.yml)

## Instructions (français)
### Conditions :
- avoir installé : [python v.3](https://www.python.org/downloads/)
- pour un répo du projet, avoir en local : (1) ses données XML (2) le log le plus récent de son workflow HTR-United téléchargé (voir les liens ci-dessus)


### Commandes d'installation en terminal (bash):
_Note : D'habitude, les commandes de terminal sont précédés par un `$`. Ignorez-le en copiant ces commandes._
1. Dans un terminal, déplacez-vous où vous voulez télécharger ce paquet.
2. Téléchargez ce paquet de GitHub : `$ git clone https://github.com/kat-kel/seg-correct.git`
3. Déplacez-vous dans le paquet téléchargé : `$ cd seg-correct`
4. Créez un environnement virtuel dans lequel vous allez installer le paquet : `$ python3 -m venv seg-venv`
5. Activez cet environment : `$ source seg-venv/bin/activate`
6. Depuis le répertoire `seg-correct/` et avec l'environnement virtuel activé, installez l'outil : `$ pip install .`

### Commandes d'utilisation en terminal (bash)
![demo](https://github.com/kat-kel/seg-correct/blob/main/demo.gif)
Gardez activé l'environnement virtuel de `seg-correct`, dans lequel est installé l'outil. Dans le terminal, vous pouvez se déplacer peu importe où vous voulez. Un bon endroit serait soit où vous avez en local les données XML du répo du projet soit où vous avez téléchargé le log du workflow HTR-United de ce répo.

0. Si besoin, réactivez l'environnement virtuel `seg-venv` depuis où il est installé, `seg-correct/`.
1. Lancer l'application : `$ seg-correct`
2. Répondez à ces questions.
3. Dis-lui où sur votre machine locale vous avez téléchargé le log du workflow HTR-United.
4. Dis-lui où sur votre machine locale sont stockées les données XML du répo dont le log parle.

L'application créera un ficher `corrections.txt` et vous dire où il se trouve sur votre machine. Vous pouvez consulter les corrections à faire aux fichiers XML du répo soit en ouvrant le fichier créé, soit en tappant dans le terminal `$ cat corrections.txt`
