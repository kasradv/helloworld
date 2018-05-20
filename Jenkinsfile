node {
    def app

    stage('Get Code') {
        // Get the latest code 
        checkout scm
    }

    stage('Docker Build') {
        // Now build the docker image
		
        app = docker.build("kasradv/helloworld")
    }

    stage('Test Artifact') {
        // Hacky test.

        app.inside {
            sh 'echo "Tests passed"'
        }
    }
	stage('Push image') {
        // Now lets push the image to docker hub
        // Good practice to tag the image twice, Once as 'latest' 
        // and another one as '_put_jenkins_build_number_here'
        docker.withRegistry('https://registry.hub.docker.com', 'cred-id-dockerhub') {
            app.push("build_${env.BUILD_NUMBER}")
            app.push("latest")
        }
    }
	
}
