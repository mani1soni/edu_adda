pipeline{
    agent any
    stages{
        stage("master"){
            when{
                branch 'master'
            }
            steps{
                sh "python3 add.py"
            }
        }
        stage("manish"){
            when{
                branch 'manish'
            }
            steps{
                sh "python3 sub.py"
            }
        }
        stage("test"){
            when{
                branch 'test'
            }
            steps{
                echo "this is test br."
            }
        } 
        stage("test2"){
            when{
                branch 'test2'
            }
            steps{
                echo 'this is test2 branch'
            }
        } 
    
    }
}

