pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'echo "Build stage completed"'
            }
        }
        
        stage('Test') {
            steps {
                echo 'Testing...'
                sh 'echo "Test stage completed"'
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                sh 'echo "Deploy stage completed"'
            }
        }
    }
}