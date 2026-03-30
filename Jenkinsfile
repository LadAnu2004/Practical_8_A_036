pipeline {
    agent any
    stages {
        stage('Pull Docker Image') {
            steps {
                // Use 'sh' because your Jenkins is running in a Linux environment
                sh 'docker pull nginx'
            }
        }
        stage('Run Container') {
            steps {
                script {
                    // This stops any old version so the new one can start
                    // The '|| true' ensures it doesn't fail if the container doesn't exist
                    sh 'docker rm -f my-web-app || true'
                    sh 'docker run -d --name my-web-app -p 8082:80 nginx'
                }
            }
        }
    }
    post {
        success {
            echo '--------------------------------------'
            echo 'PIPELINE SUCCESSFUL!'
            echo '--------------------------------------'
        }
    }
}
