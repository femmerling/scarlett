#!/usr/bin/env groovy

def PROJECT_NAME = "scarlett"
def GITHUB_REPO = "coralhq/scarlett"
def DOCKER_REPO = "coralteam/scarlett"
def BRANCHES = [
  "master": [
    dockerTag: "master"
  ]
]

milestone 0
def h,github,release
stage('init') {
  fileLoader.withGit('git@github.com:coralhq/prism-jenkins.git', 'v0.5.1') {
    h = fileLoader.load('src/helper')
    github = fileLoader.load('src/github')
    release = fileLoader.load('src/release')
  }
}

milestone 100
stage('tests') {
  node('docker') {
    github.workspace(scm, 'tests') {
      def container = "${PROJECT_NAME}_test_${h.getBuildId()}"
      def composeOpts = "-p ${PROJECT_NAME} -f docker/docker-compose.yml"
      def runOpts = "--name ${container}"

      try {
        sh "docker-compose ${composeOpts} build app"
        sh "docker-compose ${composeOpts} run ${runOpts} app test"
        sh "docker cp ${container}:/app/test-results ."
      } catch(Exception e) {
        throw e
      } finally {
        sh "docker-compose ${composeOpts} down || true"
      }
    }

    github.workspace(scm, 'test-report') {
      junit '**/xunit.xml'
      step([$class: 'CoberturaPublisher',
        autoUpdateHealth: true,
        autoUpdateStability: true,
        coberturaReportFile: '**/xcoverage.xml',
        failUnhealthy: true,
        failUnstable: false,
        packageCoverageTargets: '90.0, 0, 89.9',
        fileCoverageTargets: '90.0, 0, 89.9',
        classCoverageTargets: '90.0, 0, 89.9',
        methodCoverageTargets: '90.0, 0, 89.9',
        lineCoverageTargets: '90.0, 0, 89.9',
        conditionalCoverageTargets: '90.0, 0, 89.9',
        maxNumberOfBuilds: 0,
        onlyStable: false,
        sourceEncoding: 'ASCII',
        zoomCoverageChart: false])
    }
  }
}

if (env.BRANCH_NAME in BRANCHES) {
  def branch = BRANCHES[env.BRANCH_NAME]
  def image = "${DOCKER_REPO}:${branch.dockerTag}"

  milestone 200
  stage('docker-build') {
    node('docker') {
      checkout scm
      release.dockerBuild image,
        dockerFile: 'docker/Dockerfile',
        push: true,
        serviceName: PROJECT_NAME,
        serviceVersion: branch.dockerTag,
        githubRepo: GITHUB_REPO
    }
  }
}
