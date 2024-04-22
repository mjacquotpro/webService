# webService

## Description
`webService` est un projet éducatif pour l'apprentissage des concepts de services web. Ce projet, développé dans le cadre d'un cours, permet de gérer une base de données de films via une API RESTful créée avec Django REST Framework. Les utilisateurs peuvent effectuer des opérations CRUD (Créer, Lire, Mettre à jour, Supprimer) sur les films.

## Technologies Utilisées
- **Django REST Framework** : Utilisé pour construire l'API RESTful qui gère la base de données des films.
- **Python** : Version 3.12.x

## Fonctionnalités
- **CRUD sur les films** : L'API permet les opérations suivantes sur les films :
  - Création de films
  - Lecture de films
  - Mise à jour de films
  - Suppression de films

## Installation
Assurez-vous que Python version 3.12.x est installé sur votre machine. Vous pouvez télécharger Python à partir de [python.org](https://www.python.org/downloads/).

## Configuration
Aucune configuration spécifique ou variable d'environnement n'est nécessaire pour exécuter ce projet.

## Exécution du Projet
Pour lancer le projet localement, naviguez vers le dossier du projet et exécutez la commande suivante dans votre terminal :

```bash
cd webService/projetFilm
python manage.py runserver
```

## Utilisation
L'API est accessible via les méthodes HTTP : POST, GET, PUT et DELETE. Un fichier Postman est inclus avec le projet pour faciliter l'utilisation et la compréhension de l'API.
Un format xml et json sont disponible pour les methode get en mettant le format voulu dans le header de la request.

## Tests
Il n'y a actuellement aucun test implémenté pour ce projet.

## Déploiement
Aucune instruction spécifique pour le déploiement, le projet est destiné à être exécuté localement à des fins éducatives.

## Contribution
Ce projet ne recherche pas de contributions externes, car il s'agit d'un projet scolaire.

## Licence
Ce projet est sous la licence MIT, ce qui permet une grande liberté pour l'utilisation et la modification du code.

## Contact
Pour plus d'informations ou pour signaler un problème, veuillez contacter maximejacquotpro@gmail.com.
