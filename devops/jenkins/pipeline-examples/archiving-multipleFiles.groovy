pipeline {
    agent any
    
    stages {
        stage('Download') {
            steps {
                sh '''
                mkdir js
                echo "not a artifact file" > js/build.js
                echo "artifact file" > js/build.min.js
                mkdir css
                echo "not a artifact file" > css/build.css
                echo "artifact file" > css/build.min.css
                '''
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: '**/*.min.*', onlyIfSuccessful: true
        }
    }
}
'''
Link --> https://medium.com/@gustavo.guss/jenkins-archive-artifact-save-file-in-pipeline-ac6d8b569c2c
'''

