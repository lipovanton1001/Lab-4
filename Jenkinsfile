pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                bat 'echo "Build stage completed"'
            }
        }
        
        stage('Test') {
            steps {
                echo 'Testing...'
                bat 'echo "Test stage completed"'
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                bat 'echo "Deploy stage completed"'
            }
        }
    }
}