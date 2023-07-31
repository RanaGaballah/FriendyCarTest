pipeline {
    agent any

    stages {
        stage('New Environment') {
            steps {
                sh 'python3 -m venv myenv'
                sh '. myenv/bin/activate'
            }
        }

        stage('Install dependencies') {
            steps {
                // Install the Python dependencies from the requirements.txt file
                sh 'pip install -r requirements.txt'
                
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
