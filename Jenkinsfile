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
        script {
            def scannerHome = tool 'SonarQubeScanner'

            withSonarQubeEnv('SonarQube') {
                bat "\"${scannerHome}\\bin\\sonar-scanner.bat\" -Dsonar.projectKey=flask-employee-app -Dsonar.sources=."
            }
        }
    }
}
}
}