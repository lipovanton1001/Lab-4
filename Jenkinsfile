pipeline {
    agent any
    
    tools {
        ant 'Ant_1.10'
    }
    
    environment {
        DOCKER_IMAGE = "lipovanton1001/lab-4"
        DOCKER_TAG = "${BUILD_NUMBER}"
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
        
        stage('Build with Ant') {
            steps {
                echo "Building... BUILD_NUMBER=${BUILD_NUMBER}"
                sh 'ant jar'
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
        
        stage('Build Docker Image') {
            steps {
                script {
                    echo "Building Docker image: ${DOCKER_IMAGE}:${DOCKER_TAG}"
                    sh "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
                    sh "docker tag ${DOCKER_IMAGE}:${DOCKER_TAG} ${DOCKER_IMAGE}:latest"
                    echo "Docker image built successfully"
                }
            }
        }
        
        stage('Push to Docker Hub') {
            }
            steps {
                script {
                    echo "Pushing image to Docker Hub..."
                    withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        sh "echo \$DOCKER_PASS | docker login -u \$DOCKER_USER --password-stdin"
                        sh "docker push ${DOCKER_IMAGE}:${DOCKER_TAG}"
                        sh "docker push ${DOCKER_IMAGE}:${DOCKER_IMAGE}:latest"
                    }
                }
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