pipeline {
    agent any
    stages {
        stage('Pull Docker Image') {
            steps {
                sh 'docker pull nginx'
            }
        }
        stage('Run Container') {
            steps {
                sh 'docker run -d -p 8082:80 nginx'
            }
        }
    }
}
