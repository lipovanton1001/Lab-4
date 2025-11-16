pipeline {
    agent any
    
    tools {
        ant 'Ant-1.10'
    }
    
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
                sh 'ant -Dignore.failing.tests=true jar'
                echo 'Build completed'
            }
        }
        
        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'ant test'
                echo 'Tests completed'
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline finished'
            junit allowEmptyResults: true, testResults: '**/build/test/results/TEST-*.xml'
        }
        success {
            echo 'Application testing successfully completed!'
        }
        failure {
            echo 'Ooops!!! Tests failed!'
        }
    }
}