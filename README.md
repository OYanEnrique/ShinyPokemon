# ShinyPokemon
A Python simulator that mimics hatching a Pokémon egg, featuring a random chance for it to be a Shiny, with unique IVs and a random Poké Ball.

# 🥚 Pokémon Daycare & Shiny Simulator 🌟

This is a simple command-line simulator written in Python that recreates the experience of receiving an egg from a Pokémon Daycare and hatching it, featuring the exciting chance of the Pokémon being a *Shiny*.

This project was created as a fun exercise to practice using the `random` and `time` modules in Python, as well as conditional logic and string formatting.

## How It Works

The program simulates the following steps, using dramatic pauses to build anticipation:

1.  **Receiving the Egg:** The program informs you that you have received an Egg from the Daycare.
2.  **Pokémon Lottery:** A starter Pokémon is randomly selected from a list of over 25 options.
3.  **The "Shiny" Logic:**
    * Two values are randomly generated from 1 to 512: the player's "Trainer Shiny Value" (TSV) and the egg's "Pokémon Shiny Value" (PSV).
    * If these two numbers are **exactly the same** (`TSV == PSV`), the Pokémon that hatches will be Shiny! This simulates a probability of **1 in 512**.
    * When a Shiny Pokémon hatches, the notification message is displayed in **yellow** in the terminal.
4.  **Random Attributes:**
    * IVs (Individual Values) for Attack, Defense, and Speed are randomly generated (from 0-15).
    * The type of Poké Ball the Pokémon was "caught" in is also randomly selected from a large list.
5.  **The Hatching:** After a pause, the program announces which Pokémon has hatched and reveals if it's Shiny, its IVs, and its Poké Ball.

## How to Use

The program is designed to be an automatic simulation. You do not need to enter any commands after running it.

1.  Make sure you have Python installed on your system.
2.  Save the code as `ShinyPokémon.py`.
3.  Open your terminal or command prompt.
4.  Run the script with the following command:

    ```sh
    python ShinyPokemon.py
    ```
5.  Now, just wait and hope for a Shiny!

## Technologies Used

* **Python 3**
* `random` module (for the `randint` and `choice` functions)
* `time` module (for the `sleep` function)
