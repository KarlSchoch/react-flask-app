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
                echo 'Zipping files'
                sh 'zip -r packaged.zip api node_modules public src package.json yarn.lock'
                script {
                    sshPublisher(
                        continueOnError: false, failOnError: true,
                        publishers: [
                            sshPublisherDesc(
                                configName: "${SSH_CONFIG}",
                                transfers: [
                                    // Remove previous files
                                    sshTransfer(
                                        execCommand: 'rm -R api public src node_modules | rm packaged.zip yarn.lock package.json package-lock.json'
                                    ),
                                    // Copy over packaged file and unzip it
                                    sshTransfer(
                                        sourceFiles: 'packaged.zip',
                                        remoteDirectory: '',
                                        execCommand: 'unzip packaged.zip'
                                    ),
                                    // Start flask application
                                    // Command to install python dependencies: python -m pip install -r api/requirements.txt
                                    sshTransfer(
                                        execCommand: 'python api/api.py'
                                    ),
                                    // Start Application
                                    sshTransfer(
                                        execCommand: 'npm install'
                                    ),
                                    sshTransfer(
                                        execCommand: 'yarn start'
                                    ),
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