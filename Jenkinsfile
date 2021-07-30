pipeline {
    agent any
    environment {
        NEW_VERSION = '1.3.0'
    }
    stages {
        stage('build') {
            steps {
                echo 'building the application...'
            }
        }
        stage('test') {
            steps {
                echo 'testing the application...'
                withPythonEnv('python3') {
                    sh 'pip install flask pytest'
                    sh 'pytest api/test_api.py'
                }
            }
        }

        stage('deploy') {
            steps {
                echo 'deploying the application...'
            }
        }
    }
    post {
        always {
            echo 'build finished'
        }
        success {
            echo 'build succeeded'
        }
        failure {
            echo 'build failed'
        }
    }
}