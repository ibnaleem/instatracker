<br/>
<div align="center">
  <a href="https://github.com/ibnaleem/instatracker/releases">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Instagram_logo_2016.svg/2048px-Instagram_logo_2016.svg.png" alt="Logo" width="20%" height="20%">
  </a>
  
  <h2 align="center">InstaTracker</h3>

  <p align="center">
    📸 an Instagram tracker that logs any changes to an Instagram account (followers, following, posts, and bio)
    <br />
    <br />
    <a href="https://github.com/ibnaleem/instatracker/issues">Report Bugs</a>
  </p>
</div>

---------------------------------------
```
python3 main.py -h
usage: Instagram Tracker [-h] -u USERNAME

📸 an Instagram tracker that logs any changes to an Instagram account
(followers, following, posts, and bio)

options:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        The username of the account to track

🤝 Contribute: https://github.com/ibnaleem/instatracker
```
> [!IMPORTANT]
> You must login to *your* Instagram account in order to properly scrape someone else's Instagram account. This is due to Instagram blocking `HTTPS GET` requests from unauthenticated cookies. Your login information is never stored. See more [here](https://github.com/ibnaleem/instatracker/blob/main/main.py#L51C1-L56C136) and [here](https://github.com/instaloader/instaloader/blob/master/instaloader/instaloadercontext.py#L253C1-L338C43).

> [!TIP]
> You can always create/use an alt-account for the interative login.


## Installation
> [!TIP]
> [Install Python if you don't have it already](https://www.python.org/downloads/)
#### Clone this repository:
```
$ git clone https://github.com/ibnaleem/instatracker.git
```
#### Install dependencies:
```
$ pip install -r requirements.txt
```
#### Run the script
```
$ python3 main.py -u USERNAME
```
You will be prompted to login to an Instagram account. Enter your details for the script to start running.
## Automated Logging
InstaTracker not only displays all modifications an Instagram account makes directly to the terminal (e.g., *USERNAME has unfollowed 1 person*), but it also records these changes in a text file, including the date and time.
```
------2024-06-30 01:01:13.659694+00:00------
johndoe has 100
johndoe is following 100 people
johndoe has 0 posts
johndoe has the following bio: this is my biography
------2024-06-31 02:03:15.761715+00:00------
johndoe has lost 2 followers (100 followers --> 98 followers)
------2024-06-31 05:03:15.761715+00:00------
johndoe has gained 5 followers (98 followers --> 103 followers)
...
```
This script checks for any changes every 5 minutes because Instagram's firewall starts blocking requests that are sent too quickly. You can manually update this [here](https://github.com/ibnaleem/instatracker/blob/main/main.py#L61), but do not be surprised if the script stops working.

## Built With
- [Python](https://www.python.org/)
- [Instaloader](https://github.com/instaloader/instaloader)
- [Rich](https://github.com/Textualize/rich)
## LICENSE
This repository is under the [MIT License](https://github.com/ibnaleem/instatracker/blob/main/LICENSE)
## Created By
[Ibn Aleem](https://www.linkedin.com/in/shaffan-aleem-b7a852255/)

## Contributing
I welcome contributions from the community and appreciate the time and effort put into making [InstaTracker](https://github.com/ibnaleem/InstaTracker) better. To contribute, please follow the guidelines and steps outlined below:

> Note: **_Your pull request will be closed if you do not specify the changes you've made._**

### Fork the Repository
Start by [forking this repository](https://github.com/ibnaleem/InstaTracker/fork). You can do this by clicking on the ["Fork"](https://github.com/ibnaleem/InstaTracker/fork) button located at the top right corner of the GitHub page. This will create a personal copy of the repository under your own GitHub account.

### Clone the Repository
Next, clone the forked repository to your local machine using the following command:
```bash
$ git clone https://github.com/yourusername/instatracker.git
```
Navigate to the cloned directory:
```bash 
$ cd instatracker
```
### Create a New Branch
Before making any changes, it's recommended to create a new branch. This ensures that your changes won't interfere with other contributions and keeps the main branch clean. Use the following command to create and switch to a new branch:
```bash
$ git checkout -b branch-name
```
### Make the Desired Changes
Now, you can proceed to make your desired changes to the project. Whether it's fixing bugs, adding new features, improving documentation, or optimising code, your efforts will be instrumental in enhancing the project.

### Commit and Push Changes
Once you have made the necessary changes, commit your work using the following commands:
```bash
$ git add .
$ git commit -m "Your commit message"
```
Push the changes to your forked repository:
```bash
$ git push origin branch-name
```
### Submit a Pull Request
Head over to the [original repository](https://github.com/ibnaleem/instatracker) on GitHub and go to the ["Pull requests"](https://github.com/ibnaleem/instatracker/pulls) tab.
1. Click on the "New pull request" button.
2. Select your forked repository and the branch containing your changes.
3. Provide a clear and informative title for your pull request, and use the description box to explain the modifications you have made. **_Your pull request will be closed if you do not specify the changes you've made._**
4. Finally, click on the "Create pull request" button to submit your changes.

## [PGP Fingerprint](https://github.com/ibnaleem/ibnaleem/blob/main/public_key.asc)
```
2024 7EC0 23F2 769E 6618  1C0F 581B 4A2A 862B BADE
```
![GitHub Opensource](https://img.shields.io/badge/open%20source-yes-orange) ![GitHub Maintained](https://img.shields.io/badge/maintained-yes-yellow) ![Last Commit](https://img.shields.io/github/last-commit/ibnaleem/instatracker) ![Commit Activity](https://img.shields.io/github/commit-activity/w/ibnaleem/instatracker) ![Issues](https://img.shields.io/github/issues/ibnaleem/instatracker) ![Forks](https://img.shields.io/github/forks/ibnaleem/instatracker)
