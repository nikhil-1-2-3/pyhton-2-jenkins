pipeline {
    agent any

    stages {
        stage('Clone Code') {
            steps {
                git branch: 'main', url: 'https://github.com/nikhil-1-2-3/pyhton-2-jenkins.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t python-app .'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat 'docker run python-app'
            }
        }
    }
}
