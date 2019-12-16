#!/bin/bash
mv *.txt scpfilefolder/ 
sshpass -p "python" scp -r scpfilefolder/*.txt pythonuser@10.183.5.3:/home/pythonuser/scpfiles 
