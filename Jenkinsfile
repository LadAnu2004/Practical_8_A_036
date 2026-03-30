pipeline {
    agent any
    stages {
        stage('Pull Docker Image') {
            steps {
                // Use 'bat' for Windows
                bat 'docker pull nginx'
            }
        }
        stage('Run Container') {
            steps {
                script {
                    // This stops any old version so the new one can start
                    bat 'docker rm -f my-web-app || ver > nul'
                    bat 'docker run -d --name my-web-app -p 8082:80 nginx'
                }
            }
        }
    }
    post {
        success {
            echo 'PIPELINE SUCCESSFUL!'
        }
    }
}
