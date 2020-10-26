#!/bin/bash

# git pull script

BRANCH="development"  #customize your branch name
cd ~/project/repos

REPO=(repo1 repo2 repo3 repo4 repo5 repo6 repo7 repo8 repo9 repo10 repo11) #Enter here your all repos name or microservice's repos

for i in "${REPO[@]}"
do 
	cd $i
	git checkout ${BRANCH} && \ git pull ${BRANCH}
	cd -
done









