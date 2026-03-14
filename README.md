# 🚀 Tic-Tac-Toe at the End of the Universe

"Here I am, brain the size of a planet, and you ask me to play Tic-Tac-Toe."*
 Marvin, the Paranoid Android

A command-line Tic-Tac-Toe game built in Python, featuring **Marvin the Paranoid Android** as your opponent. You can challenge another Inhabitant of Sector ZZ9 Plural Z Alpha, or face Marvin himself — who will beat you, lose to you, or draw with you, and be thoroughly depressed about all three outcomes.

---

## 📋 Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation & Setup](#installation--setup)
  - [Windows](#windows)
  - [macOS](#macos)
  - [Linux](#linux)
- [How to Play](#how-to-play)
- [Meet Your Opponent](#meet-your-opponent)
- [The Answer to Life, the Universe, and Everything](#the-answer-to-life-the-universe-and-everything)
- [Project Structure](#project-structure)
- [Contributing](#contributing)

---

## ✨ Features

- **Two-player mode** — challenge another Inhabitant of Sector ZZ9 Plural Z Alpha
- **Play against Marvin** 🤖 — the Paranoid Android who will calculate your doom and still complain about it
- **Choose who goes first** — X always goes first, O always goes second
- **Smart AI** — Marvin will attempt to win, block your moves, or fall back on a random move (all equally joylessly)
- **Marvin's commentary** — a different depressed quote for greetings, moves, wins, losses, and draws
- **Score tracking** across multiple games
- **Secret Easter Egg** — type `42` during your turn to reset the board. Reach a score of 42 for a special surprise 🐟

---

## ⚙️ Requirements

- **Python 3.6+**
- No external dependencies — just the Python standard library (`random`, `time`)

---

## 🛠️ Installation & Setup

### Windows

1. **Install Python**

   Download and install Python from the official website:
   👉 https://www.python.org/downloads/windows/

   During installation, make sure to check **"Add Python to PATH"**.

2. **Verify Python is installed**

   Open **Command Prompt** (`Win + R`, type `cmd`, press Enter) and run:
   ```cmd
   python --version
   ```

3. **Clone the repository**

   ```cmd
   git clone https://github.com/alexhp84/tic-tac-toe.git
   cd tic-tac-toe
   ```

   > Don't have Git? Download it from https://git-scm.com/download/win  
   > Or click **Code → Download ZIP** on GitHub and extract it.

4. **Run the game**

   ```cmd
   python tic-tac-toe.py
   ```

---

### macOS

1. **Install Python**

   macOS may come with Python 2 pre-installed. Install Python 3 via [Homebrew](https://brew.sh/) (recommended):

   ```bash
   # Install Homebrew if you don't have it
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

   # Install Python 3
   brew install python
   ```

   Or download directly from https://www.python.org/downloads/macos/

2. **Verify Python is installed**

   Open **Terminal** and run:
   ```bash
   python3 --version
   ```

3. **Clone the repository**

   ```bash
   git clone https://github.com/alexhp84/tic-tac-toe.git
   cd tic-tac-toe
   ```

4. **Run the game**

   ```bash
   python3 tic-tac-toe.py
   ```

---

### Linux

1. **Install Python**

   Most Linux distributions include Python 3. If not, install it via your package manager:

   **Debian/Ubuntu:**
   ```bash
   sudo apt update && sudo apt install python3
   ```

   **Fedora/RHEL:**
   ```bash
   sudo dnf install python3
   ```

   **Arch Linux:**
   ```bash
   sudo pacman -S python
   ```

2. **Verify Python is installed**

   ```bash
   python3 --version
   ```

3. **Clone the repository**

   ```bash
   git clone https://github.com/alexhp84/tic-tac-toe.git
   cd tic-tac-toe
   ```

   > Need Git? `sudo apt install git` (Debian/Ubuntu) or `sudo dnf install git` (Fedora)

4. **Run the game**

   ```bash
   python3 tic-tac-toe.py
   ```

---

## 🎯 How to Play

1. Enter your name when prompted. (Marvin already knows it — he just doesn't care.)
2. Choose to play against **another human** (1) or **Marvin** (2).
3. Choose whether you go **first** (❌) or **second** (⭕).
4. On your turn, enter a number **1–9** corresponding to a square on the board:

```
 1 | 2 | 3
---|---|---
 4 | 5 | 6
---|---|---
 7 | 8 | 9
```

5. Get **three in a row** — horizontally, vertically, or diagonally — to win.
6. If all 9 squares fill up with no winner, it's a **tie** *("No one wins. Finally, a result that reflects the true nature of the universe.")*
7. After each game, you'll be asked if you want to play again. Scores are tracked across the session.

> **🔑 Special move:** Enter `42` on your turn to reset the current board without resetting the scores.

---

## 🤖 Meet Your Opponent

**Marvin** is the Paranoid Android with a Genuine People Personality™. He is equipped with:

- A **brain the size of a planet** (used here to play Tic-Tac-Toe)
- A first-move **winning strategy** — he'll take the win if it's there
- A **blocking strategy** — he'll stop you if you're about to win
- A **random fallback** — for when neither applies, which he finds equally pointless
- An **inexhaustible supply of despair**, delivered fresh each turn

---

## 🐟 The Answer to Life, the Universe, and Everything

If any score - yours, your opponent's, or the number of draws - reaches **42**, the game will pause to acknowledge this cosmically significant number.

---

## 📁 Project Structure

```
tic-tac-toe/
├── tic-tac-toe.py   # The whole game — Marvin, the board, the despair, all of it
└── main.py          # PyCharm default entry point (not required to play)
```

---

## 🤝 Contributing

Contributions are welcome — Marvin won't be grateful, but the rest of us will.

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name.`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to your branch: `git push origin feature/your-feature-name.`
5. Open a Pull Request

Ideas for contributions: difficulty levels, a GUI, single-player scoring mode, more Marvin quotes, or an improbability drive.

---

*"I'd say this project was a labour of love, but that would be a lie, and I'm far too depressed to lie."*
*— Marvin* 🤖
