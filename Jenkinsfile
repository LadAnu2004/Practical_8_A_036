pipeline {
    agent any
    stages {
        stage('Docker Pull') {
            steps {
                // Must use 'sh' for Linux Jenkins
                sh 'docker pull nginx:latest'
            }
        }
        stage('Docker Run') {
            steps {
                script {
                    // This stops any old container so the build doesn't fail
                    sh 'docker rm -f my-web-container || true'
                    sh 'docker run -d --name my-web-container -p 8082:80 nginx:latest'
                }
            }
        }
    }
    post {
        success {
            echo '======================================'
            echo '      PIPELINE SUCCESSFUL!           '
            echo '======================================'
        }
    }
}
