import sys
def blue(_str):
    return f"\033[0;33m{_str}\033[0m"
environment = sys.argv.pop(1)
if environment == "back":
    print(f"""
    This terminal will represent your 🐍  backend!
    
    1. Get inside the environment  {blue("$ pipenv shell")}
    2. Start the server by typing {blue("$ pipenv run start")}
    """)