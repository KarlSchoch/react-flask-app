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
            environment {
                EC2_ACCESS_KEY = credentials('application-server')
            }
            steps {
                echo 'deploying the application...'
                echo 'listing all of the files to copy'
                sh 'ls'
                echo 'Testing whether I can access another computer'
                //sh 'ssh -i ${EC2_ACCESS_KEY} ec2-user@ec2-3-23-101-33.us-east-2.compute.amazonaws.com ls'
                script {
                    sshPublisher(
                        continueOnError: false, failOnError: true,
                        publishers: [
                            transfers: [
                                sshTransfer(
                                    execCommand: "ls"
                                )
                            ]
                        ]
                    )
                }
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