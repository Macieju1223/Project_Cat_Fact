pipeline {
    agent any

    environment {
        DOCKER_HUB_PASSWORD = credentials('DOCKER_HUB_PASSWORD')
    }

    stages {
        stage('Wyczyszczenie działających aplikacji') {
            steps {
                sh 'docker-compose down || true'
            }
        }
        stage('Budowa obrazu Dockera') {
            steps {
                sh "docker build . -t pcf_02:${BUILD_NUMBER}"
            }
        }
        stage('Uruchomienie aplikacji') {
            steps {
                sh "docker-compose up"
            }
        }
        stage('Wrzucenie obrazu dockera do Docker Huba') {
            steps {
                sh "docker login -u murbaniaktkh -p ${DOCKER_HUB_PASSWORD}"
                sh "docker tag pcf_02:${BUILD_NUMBER} bmarkowskii/flask_app:${BUILD_NUMBER}"
                sh 'docker tag pcf_02:latest bmarkowskii/flask_app:latest'
                sh "docker push murbaniaktkh/jenkins_test:${BUILD_NUMBER}"
            }
        }
    }
}