# 🔌 Backdoor Socket Python

Projet pédagogique implémentant une backdoor simple en Python avec gestion d'un terminal distant via sockets TCP.

## 📁 Structure

├── backdoor_client.py   # Client (machine cible)
└── backdoor_serveur.py  # Serveur (machine attaquante)
└──terminal.py          # Terminal distant


## ⚙️ Fonctionnement

- Le **serveur** attend une connexion et envoie des commandes shell
- Le **client** se connecte, exécute les commandes et renvoie les résultats
- Gestion du `cd` avec mise à jour du répertoire courant
- Reconnexion automatique côté client

## 🚀 Utilisation

**Lancer le serveur :**
```bash
python backdoor_serveur.py
```

**Lancer le client :**
```bash
python backdoor_client.py
```

Puis saisir des commandes shell depuis le serveur (`ls`, `pwd`, `whoami`, etc.)

## 🛠️ Stack

- Python 3
- `socket` — communication TCP
- `subprocess` — exécution de commandes
- `os` — gestion du répertoire courant

## ⚠️ Avertissement

Projet réalisé à des fins **éducatives uniquement** dans le cadre d'un apprentissage en sécurité réseau.  
Ne pas utiliser sur des systèmes sans autorisation explicite.

## 👤 Auteur

**Japhet Koyakosso Esso**  
[GitHub](https://github.com/japhetkoyakossoesso-eng) · [LinkedIn](https://linkedin.com/in/japhet-koyakosso-esso-974a33313)