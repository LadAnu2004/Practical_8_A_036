pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/your-username/your-repository.git'
            }
        }

        stage('Pull Docker Image') {
            steps {
                sh 'docker pull nginx'
            }
        }

        stage('Build Container') {
            steps {
                sh 'docker build -t myapp .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 8081:80 --name mycontainer myapp'
            }
        }
    }
}
