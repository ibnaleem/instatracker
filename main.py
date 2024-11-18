"""
Created by: https://github.com/ibnaleem
Contribute: https://github.com/ibnaleem/instatracker
"""

from rich.console import Console
from argparse import ArgumentParser
import datetime, instaloader, os, time
from instaloader.exceptions import AbortDownloadException

ascii_art = """
 ___           _       _____               _             
|_ _|_ __  ___| |_ __ |_   _| __ __ _  ___| | _____ _ __ 
 | || '_ \/ __| __/ _` || || '__/ _` |/ __| |/ / _ \ '__|
 | || | | \__ \ || (_| || || | | (_| | (__|   <  __/ |   
|___|_| |_|___/\__\__,_||_||_|  \__,_|\___|_|\_\___|_|   
"""

class InstaTracker:
    def __init__(self, username: str):
        self.__version__ = "v1.0.2"
        self.username: str = username
        self.instaloader = instaloader
        self.bot = self.instaloader.Instaloader()
        self.console = Console()

    @property
    def date(self):
        return datetime.datetime.now(datetime.UTC)

    def get_followers(self):
        profile = self.instaloader.Profile.from_username(self.bot.context, self.username)
        return profile.followers

    def get_following(self):
        profile = self.instaloader.Profile.from_username(self.bot.context, self.username)
        return profile.followees

    def get_posts(self):
        profile = self.instaloader.Profile.from_username(self.bot.context, self.username)
        return profile.mediacount

    def get_bio(self):
        profile = self.instaloader.Profile.from_username(self.bot.context, self.username)
        return profile.biography

    def write_to_file(self, data):
        with open(f"{self.username}_logs.txt", "a") as f:
            f.write(f"{data}\n")

    def get_followers_username(self):
        arr = []
        profile = self.instaloader.Profile.from_username(self.bot.context, self.username)
        for follower in profile.get_followers():
            arr.append(follower.username)

    def get_following_username(self):
        arr = []
        profile = self.instaloader.Profile.from_username(self.bot.context, self.username)
        for followee in profile.get_followees():
            arr.append(followee.username)
    def main(self, specific = None):
        os.system("clear" if not os.name == "nt" else "cls")
        print("Logging in...")

        # You must manually login to avoid any login errors. Below, replace the fields 'user'
        # and 'passwd' with your username and password. If you'd like, you can create a brand
        # new Instagram only for this script. Usernames and passwords are never logged.
        # If this script is throwing BadCredentials exception, use a different Instagram account.

        self.bot.login(user="YOUR INSTAGRAM USERNAME", passwd="YOUR INSTAGRAM PASSWORD") # this allows us to access & scrape Instagram.

        os.system("clear" if not os.name == "nt" else "cls")
        self.console.print(ascii_art, style="bold blue")
        self.console.print(self.__version__, style="bold blue", justify="center")
        self.console.print("⎯" * 50)
        self.console.print(f"[bold blue]:: Date                                  : {self.date}[/bold blue]")
        self.console.print(f"[bold blue]:: Username                              : {self.username}[/bold blue]")
        initial = {"followers": self.get_followers(), "following": self.get_following(), "posts": self.get_posts(), "bio": self.get_bio()}
        self.write_to_file(f"⎯⎯⎯⎯⎯⎯{self.date}⎯⎯⎯⎯⎯⎯\n{self.username} has {initial['followers']}\n{self.username} is following {initial['following']} people\n{self.username} has {initial['posts']} posts\n{self.username} has the following bio: {initial['bio']}")
        self.console.print(f"[bold blue]:: Followers                             : {initial['followers']}[/bold blue]")
        self.console.print(f"[bold blue]:: Following                             : {initial['following']}[/bold blue]")
        self.console.print(f"[bold blue]:: Posts                                 : {initial['posts']}[/bold blue]")
        self.console.print(f"[bold blue]:: Bio                                   : {initial['bio']}[/bold blue]")
        self.console.print("⎯" * 50)
        self.console.print(f"[bold green]:: Tracking started! I will log all changes to {self.username}_logs.txt and this terminal![/bold green]")

        while True:
            time.sleep(300)
            if self.get_followers() != initial["followers"]:
                if initial["followers"] > self.get_followers():
                    self.console.print(f"[bold red]⎯⎯⎯⎯⎯⎯{self.date}⎯⎯⎯⎯⎯⎯[/bold red]")
                    self.console.print(f"[bold red]:: {self.username} has lost {initial['followers'] - self.get_followers()} followers ({initial['followers']} followers ⎯> {self.get_followers()} followers)[/bold red]")
                    self.write_to_file(f"⎯⎯⎯⎯⎯⎯{self.date}⎯⎯⎯⎯⎯⎯\n{self.username} has lost {initial['followers'] - self.get_followers()} followers ({initial['followers']} followers ⎯> {self.get_followers()} followers)")
                else:
                    self.console.print(f"[bold red]⎯⎯⎯⎯⎯⎯{self.date}⎯⎯⎯⎯⎯⎯[/bold red]")
                    self.console.print(f"[bold green]:: {self.username} has gained {self.get_followers() - initial['followers']} followers ({initial['followers']} followers ⎯> {self.get_followers()} followers)[/bold green]")
                    self.write_to_file(f"⎯⎯⎯⎯⎯⎯{self.date}⎯⎯⎯⎯⎯⎯\n:: {self.username} has gained {self.get_followers() - initial['followers']} followers ({initial['followers']} followers ⎯> {self.get_followers()} followers)")
                initial["followers"] = self.get_followers()
            if self.get_following() != initial["following"]:
                if initial["following"] > self.get_following():
                    self.console.print(f"[bold red]⎯⎯⎯⎯⎯⎯{self.date}⎯⎯⎯⎯⎯⎯[/bold red]")
                    self.console.print(f"[bold red]:: {self.username} has unfollowed {initial['following'] - self.get_following()} people ({initial['following']} following ⎯> {self.get_following()} following)[/bold red]")
                    self.write_to_file(f"⎯⎯⎯⎯⎯⎯{self.date}⎯⎯⎯⎯⎯⎯\n:: {self.username} has unfollowed {initial['following'] - self.get_following()} people ({initial['following']} following ⎯> {self.get_following()} following)")
                else:
                    self.console.print(f"[bold red]⎯⎯⎯⎯⎯⎯{self.date}⎯⎯⎯⎯⎯⎯[/bold red]")
                    self.console.print(f"[bold green]{self.username} has followed {self.get_following() - initial['following']} people ({initial['following']} following ⎯> {self.get_following()} following)[/bold green]")
                    self.write_to_file(f"⎯⎯⎯⎯⎯⎯{self.date}⎯⎯⎯⎯⎯⎯\n:: {self.username} has followed {self.get_following() - initial['following']} people ({initial['following']} following ⎯> {self.get_following()} following)")
                initial["following"] = self.get_following()
            if self.get_posts() != initial["posts"]:
                if initial["posts"] > self.get_posts():
                    self.console.print(f"[bold red]⎯⎯⎯⎯⎯⎯{self.date}⎯⎯⎯⎯⎯⎯[/bold red]")
                    self.console.print(f"[bold red]{self.username} has deleted {initial['posts'] - self.get_posts()} posts ({initial['posts']} posts ⎯> {self.get_posts()} posts)[/bold red]")
                    self.write_to_file(f"⎯⎯⎯⎯⎯⎯{self.date}⎯⎯⎯⎯⎯⎯\n:: {self.username} has deleted {initial['posts'] - self.get_posts()} posts ({initial['posts']} posts ⎯> {self.get_posts()} posts)")
                else:
                    self.console.print(f"[bold red]⎯⎯⎯⎯⎯⎯{self.date}⎯⎯⎯⎯⎯⎯[/bold red]")
                    self.console.print(f"[bold green]{self.username} has posted {self.get_posts() - initial['posts']} posts ({initial['posts']} posts ⎯> {self.get_posts()} posts)[/bold green]")
                    self.write_to_file(f"⎯⎯⎯⎯⎯⎯{self.date}⎯⎯⎯⎯⎯⎯\n:: {self.username} has posted {self.get_posts() - initial['posts']} posts ({initial['posts']} posts ⎯> {self.get_posts()} posts)")
                initial["posts"] = self.get_posts()
            if self.get_bio() != initial["bio"]:
                self.console.print(f"[bold red]⎯⎯⎯⎯⎯⎯{self.date}⎯⎯⎯⎯⎯⎯[/bold red]")
                self.console.print(f"[bold green]:: {self.username} has updated their bio:[/bold green]")
                self.console.print(f"[bold red]:: Before: {initial['bio']}[/bold red]")
                self.console.print(f"[bold green]:: After: {self.get_bio()}[/bold green]")
                self.write_to_file(f"⎯⎯⎯⎯⎯⎯{self.date}⎯⎯⎯⎯⎯⎯\n{self.username} has updated their bio:\nBefore: {initial['bio']}\nAfter: {self.get_bio()}")
                initial["bio"] = self.get_bio()
if __name__ == "__main__":
    parser = ArgumentParser(prog="Instagram Tracker",
        description="📸 an Instagram tracker that logs any changes to an Instagram account (followers, following, posts, and bio)",
        epilog="🤝 Contribute: https://github.com/ibnaleem/instatracker")
    parser.add_argument("-u", "--username", help="The username of the account to track", required=True)
    args = parser.parse_args()
    tracker = InstaTracker(str(args.username))
    try:
        tracker.main()
    except Exception:
        tracker.console.print(f"[bold red]⎯⎯⎯⎯⎯⎯{tracker.date}⎯⎯⎯⎯⎯⎯\n:: Logged out of Instagram... Logging in again....[/bold red]")
        tracker.write_to_file(f"⎯⎯⎯⎯⎯⎯{tracker.date}⎯⎯⎯⎯⎯⎯\nLogged out of Instagram... Logging in again....")
        tracker.main()