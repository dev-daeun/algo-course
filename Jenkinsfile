pipeline {
  agent any
  stages {
    stage('staging') {
      steps {
        build(job: 'full-test', quietPeriod: 3)
      }
    }

  }
  environment {
    staging = 'staging'
  }
}