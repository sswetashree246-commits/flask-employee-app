pipeline {
    agent any

    stages {

        stage('Check Python') {
            steps {
                bat '"C:\\Users\\sswet\\AppData\\Local\\Python\\bin\\python.exe" --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\sswet\\AppData\\Local\\Python\\bin\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"C:\\Users\\sswet\\AppData\\Local\\Python\\bin\\python.exe" -m pytest'
            }
        }

        stage('SonarQube Analysis') {
         steps {
             withSonarQubeEnv('SonarQube') {
                bat 'sonar-scanner -Dsonar.projectKey=flask-employee-app -Dsonar.sources=.'
              }
            }
        }
    }
}