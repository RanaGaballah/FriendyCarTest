pipeline {
    agent any

    stages {
        stage('New Environment') {
            steps {
                sh 'python3 -m venv myenv'
                sh '. myenv/bin/activate'
            }
        }

        

        stage('Run Selenium Python script') {
            steps {
                // Execute your Python script here
                sh 'python3 Test LoginAPI.py'
            }
        }
    }
}
