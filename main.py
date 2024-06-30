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
        self.username: str = username
        self.bot = instaloader.Instaloader()
        self.console = Console()
        self.date = datetime.datetime.now(datetime.UTC)

    def get_followers(self):
        profile = instaloader.Profile.from_username(self.bot.context, self.username)
        return profile.followers

    def get_following(self):
        profile = instaloader.Profile.from_username(self.bot.context, self.username)
        return profile.followees

    def get_posts(self):
        profile = instaloader.Profile.from_username(self.bot.context, self.username)
        return profile.mediacount

    def get_bio(self):
        profile = instaloader.Profile.from_username(self.bot.context, self.username)
        return profile.biography

    def write_to_file(self, data):
        with open(f"{self.username}_logs.txt", "a") as f:
            f.write(data\n)
    def main(self):
        os.system("clear" if not os.name == "nt" else "cls")
        self.console.print(ascii_art, style="bold blue")
        bot_username = input("Enter your Instagram username: ")
        self.bot.interactive_login(bot_username)
        self.console.print(f"[bold green]Welcome to InstaTracker[/bold green]")
        self.console.print(f"[bold blue]Getting initial data for {self.username}...[/bold blue]")
        initial = {"followers": self.get_followers(), "following": self.get_following(), "posts": self.get_posts(), "bio": self.get_bio()}
        self.write_to_file(f"------{self.date}------\n{self.username} has {initial["followers"]}\n{self.username} is following {initial["following"]} people\n{self.username} has {initial["posts"]} posts\n{self.username} has the following bio: {initial["bio"]}")
        self.console.print(f"[bold blue]------{self.date}------[/bold blue]")
        self.console.print(f"[bold blue]{self.username} has {self.get_followers()} followers[/bold blue]")
        self.console.print(f"[bold blue]{self.username} is following {self.get_following()} people[/bold blue]")
        self.console.print(f"[bold blue]{self.username} has {self.get_posts()} posts[/bold blue]")
        self.console.print(f"[bold blue]{self.username} has the following bio: {self.get_bio()}[/bold blue]")
        self.console.print(f"[bold green]Tracking started! I will log all changes to {self.username}_logs.txt and this terminal![/bold green]")

        while True:
            try:
                time.sleep(300)
                if self.get_followers() != initial["followers"]:
                    if initial["followers"] > self.get_followers():
                        self.console.print(f"[bold red]------{self.date}------[/bold red]")
                        self.console.print(f"[bold red]{self.username} has lost {initial['followers'] - self.get_followers()} followers ({initial['followers']} followers --> {self.get_followers()} followers)[/bold red]")
                        self.write_to_file(f"------{self.date}------\n{self.username} has lost {initial['followers'] - self.get_followers()} followers ({initial['followers']} followers --> {self.get_followers()} followers)")
                    else:
                        self.console.print(f"[bold red]------{self.date}------[/bold red]")
                        self.console.print(f"[bold green]{self.username} has gained {self.get_followers() - initial['followers']} followers ({initial['followers']} followers --> {self.get_followers()} followers)[/bold green]")
                        self.write_to_file(f"------{self.date}------\n{self.username} has gained {self.get_followers() - initial['followers']} followers ({initial['followers']} followers --> {self.get_followers()} followers)")
                    initial["followers"] = self.get_followers()
                if self.get_following() != initial["following"]:
                    if initial["following"] > self.get_following():
                        self.console.print(f"[bold red]------{self.date}------[/bold red]")
                        self.console.print(f"[bold red]{self.username} has unfollowed {initial['following'] - self.get_following()} people ({initial['following']} following --> {self.get_following()} following)[/bold red]")
                        self.write_to_file(f"------{self.date}------\n{self.username} has unfollowed {initial['following'] - self.get_following()} people ({initial['following']} following --> {self.get_following()} following)")
                    else:
                        self.console.print(f"[bold red]------{self.date}------[/bold red]")
                        self.console.print(f"[bold green]{self.username} has followed {self.get_following() - initial['following']} people ({initial['following']} following --> {self.get_following()} following)[/bold green]")
                        self.write_to_file(f"------{self.date}------\n{self.username} has followed {self.get_following() - initial['following']} people ({initial['following']} following --> {self.get_following()} following)")
                    initial["following"] = self.get_following()
                if self.get_posts() != initial["posts"]:
                    if initial["posts"] > self.get_posts():
                        self.console.print(f"[bold red]------{self.date}------[/bold red]")
                        self.console.print(f"[bold red]{self.username} has deleted {initial['posts'] - self.get_posts()} posts ({initial['posts']} posts --> {self.get_posts()} posts)[/bold red]")
                        self.write_to_file(f"------{self.date}------\n{self.username} has deleted {initial['posts'] - self.get_posts()} posts ({initial['posts']} posts --> {self.get_posts()} posts)")
                    else:
                        self.console.print(f"[bold red]------{self.date}------[/bold red]")
                        self.console.print(f"[bold green]{self.username} has posted {self.get_posts() - initial['posts']} posts ({initial['posts']} posts --> {self.get_posts()} posts)[/bold green]")
                        self.write_to_file(f"------{self.date}------\n{self.username} has posted {self.get_posts() - initial['posts']} posts ({initial['posts']} posts --> {self.get_posts()} posts)")
                    initial["posts"] = self.get_posts()
                if self.get_bio() != initial["bio"]:
                    self.console.print(f"[bold red]------{self.date}------[/bold red]")
                    self.console.print(f"[bold green]{self.username} has updated their bio:[/bold green]")
                    self.console.print(f"[bold red] Before: {initial['bio']}[/bold red]")
                    self.console.print(f"[bold green] After: {self.get_bio()}[/bold green]")
                    self.write_to_file(f"------{self.date}------\n{self.username} has updated their bio:\nBefore: {initial['bio']}\nAfter: {self.get_bio()}")
                    initial["bio"] = self.get_bio()
            except AbortDownloadException:
                self.console.print(f"[bold red]------{self.date}------[/bold red]")
                self.console.print(f"[bold red]You've been logged out, tracking has been paused[/bold red]")
                self.write_to_file(f"------{self.date}------\nYou've been logged out, tracking has been paused")
                self.console.print("[bold red]Please login again...[/bold red]")
                self.bot.interactive_login(bot_username)
if __name__ == "__main__":
    parser = ArgumentParser(prog="Instagram Tracker",
        description="📸 an Instagram tracker that logs any changes to an Instagram account (followers, following, posts, and bio)",
        epilog="🤝 Contribute: https://github.com/ibnaleem/instatracker")
    parser.add_argument("-u", "--username", help="The username of the account to track", required=True)
    args = parser.parse_args()
    tracker = InstaTracker(str(args.username))
    tracker.main()
