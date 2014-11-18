##Prerequisites
 - Have Python installed
 - Install the library [Twython](https://github.com/ryanmcgrath/twython)

##Instructions
Add both <b>post-commit</b> and <b>post-commit.py</b> to the .git/hooks folder of your current GitHub project.

##Setting up the Twitter Application
###Creating the Application
 - Log into your Twitter account
 - Go to https://apps.twitter.com/ and click Create New App
 - Set the Name to "GitHub Commit Messages"
 - Set the Description to "Post GitHub commit messages to Twitter"
 - Set the Website to "https://www.github.com"
 - Accept the Developer Agreement and Create your Twitter application

###Setting Permissions and Generating Keys
 - Navigate to the Permissions tab and set Access to "Read and Write"
     - May require you to add mobile phone number to Twitter account
 - Navigate to the Keys and Access Tokens tab to "Create my access token"
 - Copy the API KEY, API SECRET, OAUTH KEY, and OAUTH SECRET into the script
 
Demo Twitter Account: [jsuh_github](https://twitter.com/jsuh_github)