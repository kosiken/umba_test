pipeline {
    environment {
    imageRepo = 'kosiken/umbatest'
    commitSha = sh(returnStdout: true, script: "git log -1 --pretty=format:'%h'").trim()
    imageName = "${imageRepo}:${commitSha}"
  }
    agent any

    stages {
      stage('Clone Source') {
          steps {
            checkout scm
          }
      }
       stage('Build Image') {
          steps {
            sh ' docker build -t ${imageName} --target production .'
          }
      }
      stage('Deploy Application') {
          steps {
             sh 'docker stop umbatest || true && docker rm umbatest || true'
             sh 'docker run -d -p 3003:3003 --name umbatest --env-file ~/env/kosiken/umbatest.env ${imageName}'
          }
      }
        stage('Cleanup Build') {
          steps {
             sh 'docker system prune -a -f || true'
          }
      }
    }
}