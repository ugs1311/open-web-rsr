pipeline {
    agent any

    options {
        skipDefaultCheckout()
    }

    stages {
        stage('Load Pipeline') {
            steps {
                script {
                    // Checkout the repository
                    checkout scm
                    
                    // Load and execute the main pipeline
                    def mainPipeline = load 'jenkins/Jenkinsfile'
                }
            }
        }
    }
} 