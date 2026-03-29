pipeline {
    agent any

    stages {
        stage('Clone Code') {
            steps {
                git branch: 'main', url: 'https://github.com/nikhil-1-2-3/pyhton-2-jenkins.git'
            }
        }

        stage('Run Python App') {
            steps {
                bat 'python app.py'
            }
        }
    }
}
