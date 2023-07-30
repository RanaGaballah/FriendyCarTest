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
                    sh 'python3 TestLoginAPI.py'
                   
                }
            }
        }
    }

    post {
        success {
            // Send email with the test output
            emailext subject: 'Sign In API To Corporate Build Success - Test Results',
                      body: "Login was successful , DashBoard API passed successfully , Borrower API passed successfully.",
                      to: 'developer@friendycar.com',
                      mimeType: 'text/plain'
        }

        failure {
            // Send email with the test output when the build fails
            emailext subject: 'Sign In API To Corporate Build Failed - Test Results',
                      body: "Test Output:test faild",
                      to: 'developer@friendycar.com',
                      mimeType: 'text/plain'
        }
    }

    
}
