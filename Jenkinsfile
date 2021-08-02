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
                SSH_CONFIG = 'application'
            }
            steps {
                echo 'deploying the application...'
                echo 'listing all of the files to copy'
                sh 'ls'
                sh 'zip -r packaged.zip api node_modules public src package.json yarn.lock'
                echo 'Testing whether I can access another computer'
                script {
                    sshPublisher(
                        continueOnError: false, failOnError: true,
                        publishers: [
                            sshPublisherDesc(
                                configName: "${SSH_CONFIG}",
                                transfers: [
                                    sshTransfer(
                                        //sourceFiles: 'packaged.zip',
                                        //remoteDirectory: '',
                                        execCommand: 'rm packaged.zip'
                                    ),
                                    //sshTransfer(
                                    //    sourceFiles: 'packaged.zip',
                                    //    remoteDirectory: '',
                                    //    //execCommand: 'ls'
                                    //)
                                ]
                            )
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