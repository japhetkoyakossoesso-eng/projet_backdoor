# 🔌 Backdoor Socket Python

Projet pédagogique implémentant une backdoor en Python avec terminal distant, téléchargement de fichiers et capture d'écran via sockets TCP.

## 📁 Structure

├── backdoor_client.py   # Client (machine cible)
└── backdoor_serveur.py  # Serveur (machine attaquante)


## ⚙️ Fonctionnement

- Le **serveur** attend une connexion et envoie des commandes shell
- Le **client** se connecte, exécute les commandes et renvoie les résultats
- Récupération automatique des infos système à la connexion
- Gestion du `cd` avec mise à jour du répertoire courant
- Téléchargement de fichiers depuis la machine cible
- Capture d'écran à distance
- Reconnexion automatique côté client
- Réception robuste des données via header 13 octets

## 🚀 Utilisation

**Lancer le serveur :**
```bash
python3 backdoor_serveur.py
```

**Lancer le client :**
```bash
python3 backdoor_client.py
```

## 📟 Commandes disponibles

| Commande | Description |
|---|---|
| `ls`, `pwd`, `whoami`... | Commandes shell classiques |
| `cd <dossier>` | Changer de répertoire |
| `dl <fichier>` | Télécharger un fichier depuis la cible |
| `capture <nom>` | Capturer l'écran de la cible (sauvegarde en .png) |
| `infos` | Afficher la plateforme et le répertoire courant |

## 🛠️ Stack

- Python 3
- `socket` — communication TCP
- `subprocess` — exécution de commandes shell
- `os` / `platform` — infos système et gestion des répertoires
- `pyscreenshot` — capture d'écran

## 📦 Installation des dépendances

```bash
pip3 install pyscreenshot pillow
```

## ⚠️ Avertissement

Projet réalisé à des fins **éducatives uniquement** dans le cadre d'un apprentissage en sécurité réseau.  
Ne pas utiliser sur des systèmes sans autorisation explicite.

## 👤 Auteur

**Japhet Koyakosso Esso**  
[GitHub](https://github.com/japhetkoyakossoesso-eng) · [LinkedIn](https://linkedin.com/in/japhet-koyakosso-esso-974a33313)