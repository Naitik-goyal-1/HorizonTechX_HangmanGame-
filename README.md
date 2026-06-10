# 🪢 Hangman – Text-Based Python Game

A simple, fully playable **Hangman** game that runs in any terminal.  
Guess the hidden word one letter at a time before the stick figure is completely drawn!

---

## 📁 Project Structure

```
hangman/
└── hangman.py   # All game logic in a single file
└── README.md    # You are here
```

---

## 🚀 How to Run

**Requirements:** Python 3.x (no external libraries needed)

```bash
python hangman.py
```

> On some systems use `python3 hangman.py`

---

## 🎮 How to Play

1. The game picks a **random word** from its built-in word bank.
2. You are shown how many letters the word contains (as underscores).
3. **Type one letter** and press Enter each turn.
4. A correct guess reveals every occurrence of that letter in the word.
5. A wrong guess adds a body part to the gallows and costs you **1 of your 6 lives**.
6. **Win** by guessing all letters before the figure is fully drawn.
7. **Lose** after 6 wrong guesses — the man is hanged!
8. After each round you can choose to **play again** or quit.

---

## 📋 Sample Session

```
=============================================
       W E L C O M E  T O  H A N G M A N
=============================================
  A 6-letter word has been chosen.
  Guess it before the man is hanged!

  +---+
  |   |
      |
      |
      |
      |
=========

  Word  :  _ _ _ _ _ _
  Wrong guesses : 0 / 6

  Guess a letter: p

  ✅  Nice! 'p' is in the word (1 time).

  Word  :  p _ _ _ _ _
  ...
```

---

## 🧠 Key Concepts Used

| Concept | Where it appears |
|---|---|
| `random` | `random.choice(WORDS)` picks the secret word |
| `while` loop | Main game loop + replay loop + input-validation loop |
| `if-else` | Deciding correct vs wrong guess, win vs loss checks |
| Strings | Masking the word, comparing guesses, building output |
| Lists / Sets | `WORDS` list stores the word bank; `guessed_letters` set tracks tries |

---

## 📝 Word Bank

The game currently includes **5 predefined words**:

```python
WORDS = ["python", "hangman", "guitar", "jungle", "rocket"]
```

To add more words, simply extend this list in `hangman.py`.

---

## ⚙️ Game Rules Summary

| Rule | Value |
|---|---|
| Maximum wrong guesses | **6** |
| Minimum word length | 6 letters |
| Input type | Single alphabetic character |
| Case sensitivity | **None** – all input is lowercased automatically |
| Repeated guess handling | Warned and re-prompted (doesn't cost a life) |

---

## 🔧 Customisation Tips

- **Add words:** Edit the `WORDS` list at the top of `hangman.py`.
- **Change difficulty:** Adjust `max_wrong` in `play_game()` (e.g., `4` for hard mode).
- **Themed word lists:** Replace `WORDS` with any list of strings (animals, countries, etc.).

---

## 📄 License

This project is released for educational purposes. Free to use and modify.
