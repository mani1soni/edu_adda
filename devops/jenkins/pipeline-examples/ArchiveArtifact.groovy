pipeline{
    agent any
    stages{
        stage("download"){
            steps{
                sh 'echo "artifact file" > generatedfile.txt'
                
            }
        }    
    }
    post{
        always{
            archiveArtifacts artifacts: 'generatedfile.txt', onlyIfSuccessful: true
        }
    }
}
