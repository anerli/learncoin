#!/bin/bash
SCRIPT="ssh-keygen -R 10.90.73.217; cd ..; sudo git clone https://oauth2:glpat-tnmmb9yERsxK5KBrsVfp@git.ece.iastate.edu/lie/learncoin.git; ls; exit"
HOSTS=("coms-402-sd-23.class.las.iastate.edu" "coms-402-sd-24.class.las.iastate.edu" "coms-402-sd-25.class.las.iastate.edu" "coms-402-sd-26.class.las.iastate.edu" "coms-402-sd-27.class.las.iastate.edu")
USERNAME="gitlab"
for i in ${!HOSTS[*]} ; do
     echo ${HOSTS[i]}
     ssh -ttl ${USERNAME} ${HOSTS[i]} "${SCR}"
done
