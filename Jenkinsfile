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
                    def testOutput =  sh 'python3 TestLoginAPI.py', returnStdout: true
                    env.TEST_OUTPUT = testOutput // Store the output in an environment variable
                    echo "Test Output:\n${testOutput}" // Print the output in the Jenkins console
                   
                }
            }
        }
    }

    post {
        success {
            // Send email with the test output
            emailext subject: 'Sign In API To Corporate Build Success - Test Results',
                      body: "Test Output:\n${TEST_OUTPUT}",
                      to: 'developer@friendycar.com',
                      mimeType: 'text/plain'
        }

        failure {
            // Send email with the test output when the build fails
            emailext subject: 'Sign In API To Corporate Build Failed - Test Results',
                      body: "Test Output:\n${TEST_OUTPUT}",
                      to: 'developer@friendycar.com',
                      mimeType: 'text/plain'
        }
    }

    
}
