python "./website_builder.py"

git add .

$commitMessage = Read-Host -Prompt "Kindly enter the commit message"

git commit -m "$commitMessage"
git push