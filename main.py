import subprocess
import random
from datetime import datetime

def update_log():
    with open('log.txt', 'a') as f:
        f.write(f'Automated commit at {datetime.now()}\n')

# def git_commit_and_push():
#     try:
#         # Add changes to the staging area
#         subprocess.run(['git', 'add', 'log.txt'], check=True)
        
#         # Commit the changes
#         commit_message = f"Automated commit at {datetime.now()}"
#         subprocess.run(['git', 'commit', '-m', commit_message], check=True)
        
#         # Push the changes to the repository
#         subprocess.run(['git', 'push'], check=True)

#         print("Changes committed and pushed successfully.")
#     except subprocess.CalledProcessError as e:
#         print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Pick a random number between 1 and 3
    num_loops = random.randint(1, 3)

    # Loop that many times to update the log
    for _ in range(num_loops):
        update_log()
        #git_commit_and_push()
