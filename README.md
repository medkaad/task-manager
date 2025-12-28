# 📝 Task Manager — Django + Vue + JWT + SB Admin 2 + Machine Learning

Task Manager est une application full-stack permettant de gérer des projets et leurs tâches.
Elle inclut un tableau de bord moderne, une authentification sécurisée, et une fonction intelligente
capable de prédire automatiquement la priorité d’une tâche grâce au Machine Learning.

---

## 🚀 Fonctionnalités principales

### 🎯 Gestion
- CRUD projets (create – read – update – delete)
- CRUD tâches
- Filtrage des tâches par projet
- Affichage détaillé d’un projet avec liste de tâches

### 🔐 Authentification JWT
- Login sécurisé (access + refresh token)
- Token stocké dans localStorage
- Route guard côté frontend (si pas connecté → redirection vers login)
- Logout propre

### 🎨 UI Dashboard moderne
- Vue 3 + Vite
- SB Admin 2 (Bootstrap UI)
- Sidebar – Topbar – Layout Dashboard
- Pages :
  - /login
  - /projects
  - /projects/:id (tâches)

### 🤖 Intelligence artificielle — priorité automatique
- API `/api/predict-priority/` basée sur Transformers
- Déduit priorité : `high`, `medium`, `low`
- Bouton "AI Suggest Priority" dans l'UI

---

## 🧱 Stack technique

| Type | Outils |
|------|--------|
| Backend | Django – Django REST Framework – SimpleJWT |
| Machine Learning | HuggingFace Transformers – Torch |
| Frontend | Vue 3 – Vite – Axios – SB Admin 2 |
| Infra | Docker – Docker Compose |

---

## 📦 Installation

### 🐳 Avec Docker (recommandé)

```bash
git clone https://github.com/medkaad/task-manager.git
cd task-manager
docker compose up --build
