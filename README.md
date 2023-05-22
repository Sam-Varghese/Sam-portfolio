# Sam's Portfolio

---

This is my new portfolio website, made entirely in HTML. Previously I made a react site, but due to issues with AWS account, I had to give up on that. This website is deployed on GitHub itself. You may view the website through this link: https://sam-varghese.github.io/Sam-portfolio/

After making any changes, execute [Powershell Script](./githubActioner.ps1) to update the website, including time stamps, and push all the changes to cloud.

To edit the website, all you need to do is to update the respective json files, and execute [Python program](./website_builder.py). This will apply all the changes to the HTML file, and make it up to date.

Please note that all the code has been minified, so unfortunately editing the code directly might get difficult. Use the python program and powershell scripts. 

Website is [MIT Licensed](./LICENSE)