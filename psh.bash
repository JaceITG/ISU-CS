#!/bin/bash
url="https://github.com/scheisseosu/ISU-CS.git"

msg="$*"

git pull origin main
git add .
git commit -m "$msg"
git push $url
