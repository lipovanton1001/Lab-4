pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = "ubrouprou/lab-4"
        DOCKER_TAG = "${BUILD_NUMBER}"
        SRC_DIR = "src"
        TEST_DIR = "test"
        BUILD_DIR = "build"
        CLASSES_DIR = "${BUILD_DIR}/classes"
        JAR_DIR = "${BUILD_DIR}/jar"
        TEST_CLASSES_DIR = "${BUILD_DIR}/test/classes"
        TEST_RESULTS_DIR = "${BUILD_DIR}/test/results"
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
        
        stage('Clean') {
            steps {
                echo 'Cleaning previous build...'
                sh 'rm -rf ${BUILD_DIR}'
                echo 'Clean completed'
            }
        }
        
        stage('Compile') {
            steps {
                echo "Compiling... BUILD_NUMBER=${BUILD_NUMBER}"
                sh 'mkdir -p ${CLASSES_DIR}'
                sh 'javac -d ${CLASSES_DIR} ${SRC_DIR}/*.java'
                echo 'Compilation completed'
            }
        }
        
        stage('Create JAR') {
            steps {
                echo 'Creating JAR file...'
                sh 'mkdir -p ${JAR_DIR}'
                sh 'jar cvfe ${JAR_DIR}/Lab-4.jar Main -C ${CLASSES_DIR} .'
                echo 'JAR created successfully'
            }
        }
        
        stage('Compile Tests') {
            steps {
                echo 'Compiling tests...'
                sh 'mkdir -p ${TEST_CLASSES_DIR}'
                sh 'javac -cp ${CLASSES_DIR} -d ${TEST_CLASSES_DIR} ${TEST_DIR}/*.java'
                echo 'Test compilation completed'
            }
        }
        
        stage('Run Tests') {
            steps {
                echo 'Running JUnit tests...'
                sh 'mkdir -p ${TEST_RESULTS_DIR}'
                
                // Запуск JUnit через консоль (потрібен junit-platform-console-standalone)
                sh '''
                    java -jar lib/junit-platform-console-standalone.jar \
                        --class-path ${CLASSES_DIR}:${TEST_CLASSES_DIR} \
                        --scan-class-path \
                        --reports-dir ${TEST_RESULTS_DIR}
                '''
                
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
            steps {
                script {
                    echo "Pushing image to Docker Hub..."
                    withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        sh "echo \$DOCKER_PASS | docker login -u \$DOCKER_USER --password-stdin"
                        sh "docker push ${DOCKER_IMAGE}:${DOCKER_TAG}"
                        sh "docker push ${DOCKER_IMAGE}:latest"
                    }
                    echo "Image pushed successfully"
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