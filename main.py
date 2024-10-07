from datetime import datetime

def update_log():
    with open('log.txt', 'a') as f:
        f.write(f'Automated commit at {datetime.now()}\n')

if __name__ == "__main__":
    update_log()
