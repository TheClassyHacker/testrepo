# Welcome to TheClassyHacker Starter Project
"""
This repository serves as a fun and functional starter template for TheClassyHacker projects. It includes:
- A colorful ASCII welcome banner (powered by colorama)
- A Markdown README file
- A requirements.txt file for easy setup
"""

# ascii_welcome.py
# A colorful, Windows-safe ASCII welcome message for TheClassyHacker
from colorama import init, Fore, Style

# Initialize colorama for cross-platform color support
init(autoreset=True)

def print_ascii_welcome():
    ascii_art = f"""
{Fore.CYAN}
 ___________.__           _________ .__                                ___ ___                __                 
 \\__    ___/|  |__   ____ \\_   ___ \\|  | _____    ______ _________.__./   |   \\_____    ____ |  | __ ___________ 
   |    |   |  |  \\_/ __ \\/    \\  \\/|  | \\__  \\  /  ___//  ___<   |  /    ~    \\__  \\ _/ ___\\|  |/ // __ \\_  __ \\
   |    |   |   Y  \\  ___/\\     \\___|  |__/ __ \\_\\___ \\ \\___ \\ \\___  \\    Y    // __ \\\\  \\___|    <\\  ___/|  | \\/
   |____|   |___|  /\\___  >\\______  /____(____  /____  >____  >/ ____|\\___|_  /(____  /\\___  >__|_ \\\\___  >__|   
                 \\/     \\/        \\/          \\/     \\/     \\/ \\/           \\/      \\/     \\/     \\/    \\/       
{Style.RESET_ALL}
    """

    message = f"{Fore.GREEN}\nTheClassyHacker welcomes you! Let's build, break, and secure the web.\n{Style.RESET_ALL}"

    print(ascii_art)
    print(message)

if __name__ == "__main__":
    print_ascii_welcome()




# README.md

# TheClassyHacker Starter Project
"""
Welcome to the official starter project for TheClassyHacker! This project includes:

- A colorful ASCII welcome banner
- Python script to display the banner
- A requirements file for quick setup

## Setup

1. Clone the repository.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the welcome script:

```bash
python ascii_welcome.py
```

## Why This Matters

Every great project starts with a great welcome. This template makes it easy to set the tone for your projects with flair and style, the classy way.

## License

MIT License
```

---

# requirements.txt

```
colorama
"""
