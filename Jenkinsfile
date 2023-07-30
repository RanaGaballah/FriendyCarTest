pipeline {
    agent any

    stages {
        stage('Generate Requirements') {
            steps {
                script {
                    
                    sh 'pip freeze > requirements.txt'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Make sure you have the correct Python interpreter and pip installed in your Jenkins environment
                    sh 'python3 -m pip install --upgrade pip'
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run Python Script') {
            steps {
                script {
                    // Replace 'your_python_script.py' with the name of your Python script
                    sh 'python3 TestLoginAPI.py'
                }
            }
        }
    }

    
}
