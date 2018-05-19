node {
    def app

    stage('Get Code') {
        # Get the latest code 
        checkout scm
    }

    stage('Docker Build') {
        # Now build the docker image
		
        app = docker.build("dudu")
    }

    stage('Test Artifact') {
        # Hacky test.

        app.inside {
            sh 'echo "Tests passed"'
        }
    }

}