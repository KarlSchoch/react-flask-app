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
                // Need to install the pyenv-pipeline plug-in
                withPythonEnv('python3') {
                    sh 'pip install flask pytest'
                    sh 'pytest api/test_api.py'
                }
            }
        }
        stage('deploy') {
            steps {
                echo 'deploying the application...'
                echo 'listing all of the files to copy'
                sh 'ls'
                echo 'Testing whether I can access another computer'
                sh "ssh ec2-user@ec2-3-23-101-33.us-east-2.compute.amazonaws.com ls"
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