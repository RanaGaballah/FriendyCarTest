pipeline {
    agent any

    stages {
        stage('Generate requests') {
            steps {
                script {
                    
                    sh 'pip install requests'
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
