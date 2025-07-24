# 🧠🍔 Agent Alimentaire IA – Application FastAPI

Un assistant intelligent de type chatbot, conçu avec **FastAPI**, **GPT-4**, et un fichier **JSON comme base de données**. L’application propose une interface web où les utilisateurs peuvent poser des questions sur les plats disponibles, les régimes alimentaires, les ingrédients, etc. L’agent IA répond dynamiquement aux questions, avec des suggestions de requêtes fréquentes pour faciliter l’interaction.

---

## 🔥 Fonctionnalités

- ✅ Interface web interactive avec suggestions de requêtes
- 🤖 Assistant conversationnel basé sur GPT-4.1
- 🍲 Données alimentaires stockées en JSON local
- 📦 Backend REST API avec FastAPI
- 🧠 Compréhension du langage naturel basée sur les données du menu


---

## 🚀 Démo en ligne

Tu peux exécuter le projet en local en suivant les étapes ci-dessous.

---

## 🧠 Exemples de requêtes utilisateur
- Quels plats contiennent du poulet ?
- Avez-vous des options végétariennes ?
- Quels sont vos plats les plus populaires ?
- Y a-t-il des plats sans gluten ?
- Quels plats ne contiennent pas de produits laitiers ?
- Puis-je voir tous les plats disponibles ?

---

## 📄 Points de terminaison API

| Méthode | Endpoint | Description                                              |
| ------- | -------- | -------------------------------------------------------- |
| GET     | `/`      | Renvoie l’interface HTML                                 |
| POST    | `/ask`   | Reçoit une question utilisateur et renvoie la réponse IA |
| GET     | `/foods` | (Optionnel) Renvoie les données JSON du menu             |


---

## 🧪 Technologies utilisées
- FastAPI – Framework web Python moderne
- Jinja2 – Moteur de templates HTML
- OpenAI GPT-4.1 – Compréhension du langage naturel
- HTML + JavaScript – Interface interactive
- JSON – Base de données légère simulée

---

## 📁 Structure du projet

