pipeline {
    agent any
    
    options {
        timestamps()
    }
    
    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                echo "Building... BUILD_NUMBER=${BUILD_NUMBER}"
                echo 'Build completed'
            }
        }
        
        stage('Test') {
            agent {
                docker {
                    image 'openjdk:11'
                    args '--user root'
                }
            }
            steps {
                echo 'Running tests...'
                sh 'java -version'
                echo 'Tests completed'
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline finished'
        }
        success {
            echo 'Application testing successfully completed!'
        }
        failure {
            echo 'Ooops!!! Tests failed!'
        }
    }
}