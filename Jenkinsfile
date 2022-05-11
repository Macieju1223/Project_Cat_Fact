pipeline {
    agent any

    stages {
        stage('Build dockerfile') {
            steps {
                sh "docker build . -t pcf_02"
                echo "build complete"
            }
        }
        stage('create docker network'){
            steps {
                sh "docker network create -d bridge project_cat_facts"
            }
        }
        stage('Dwonload mongo_db image'){
            steps {
                sh "docker pull mongo"
                echo "download complete"
            }
        }
        stage('Build mongo_db'){
            steps {
                sh "docker run -p 27017:27017 --name mongo_db --network project_cat_facts -d mongo"
            }

        }
        stage('build pcf_02 app'){
            steps{
                sh "docker run -d --network project_cat_facts --name pcf_02 pcf_02"
            }
        }
        stage('killing all'){
            steps{
                sh "docker kill pcf_02 mongo_db"
                sh "docker rm -f pcf_02 mongo"
                sh "docker container prune"
                sh "docker network rm project_cat_facts"
            }
        }
    }
}