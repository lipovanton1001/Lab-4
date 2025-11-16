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
                echo 'Build stage completed'
            }
        }
        
        stage('Test') {
            steps {
                echo 'Running tests...'
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