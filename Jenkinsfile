pipeline {
    agent any

    stages {
        stage('Run Python script') {
            steps {
               
                sh 'python3 Test LoginAPI.py'
            }
        }
    }

    post {
       
        failure {
            // Send email with the test output when the build fails
            emailext subject: 'Sign In To Corporate Build Failed - Test Results',
                      body: "Test Output:",
                      to: 'developer@friendycar.com',
                      mimeType: 'text/plain'
        }
    }
}
