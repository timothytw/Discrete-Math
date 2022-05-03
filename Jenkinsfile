timestamps {

node () {

	stage ('discrete-math - Checkout') {
		checkout([
			$class: 'GitSCM',
			branches: [[name: '${BRANCH}']],
			doGenerateSubmoduleConfigurations: false,
			extensions: [],
			submoduleCfg: [],
			userRemoteConfigs: [
				[credentialsId: '', url: 'https://github.com/timothytw/Discrete-Math.git']
			]
		]) 
	}
	stage ('discrete-math - Build') {
		sh """ 
			echo "The shell works!" 
		""" 
	}
}
}
