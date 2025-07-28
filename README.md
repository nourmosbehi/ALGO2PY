# ALGO2PY </>

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Un convertisseur web intelligent pour transformer du pseudo-code algorithmique en Python et vice versa.

![Interface ALGO2PY](static/images/screenshot.png)

## Fonctionnalités ✨

- **Conversion bidirectionnelle** :
  - Pseudo-code algorithmique → Code Python
  - Code Python → Pseudo-code algorithmique
- **Prise en charge complète** :
  - Structures conditionnelles (`si...alors`, `sinon`)
  - Boucles (`pour`, `tant que`)
  - Variables et fonctions
  - Affichage console (`afficher`)
- **Interface intuitive** avec mise en forme syntaxique
- **Gestion d'erreurs** avancée

## 🚀 Installation et utilisation

### Prérequis
- Python 3.8 ou supérieur
- Pip (gestionnaire de paquets Python)

### 1. Clonage du dépôt
```bash
git clone https://github.com/nourmosbehi/ALGO2PY.git
cd ALGO2PY

# Création de l'environnement virtuel
python -m venv venv

# Activation (Linux/Mac)
source venv/bin/activate

# Activation (Windows)
.\venv\Scripts\activate

# Installation des dépendances
pip install -r requirements.txt

# Lancement de l'application
python app.py

🌐 http://localhost:5000

