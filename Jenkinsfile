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
                sh '/var/jenkins_home/tools/hudson.tasks.Ant_AntInstallation/Ant-1.10/bin/ant -Dignore.failing.tests=true jar'
                echo 'Build completed'
            }
        }
        
        stage('Test') {
            agent {
                docker {
                    image 'eclipse-temurin:11'
                    args '--user root'
                    reuseNode true
                }
            }
            steps {
                echo 'Running tests...'
                sh 'java -version'
                sh '/var/jenkins_home/tools/hudson.tasks.Ant_AntInstallation/Ant-1.10/bin/ant test'
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