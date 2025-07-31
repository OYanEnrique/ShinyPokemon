# ShinyPokemon
A Python simulator that mimics hatching a Pokémon egg, featuring a random chance for it to be a Shiny, with unique IVs and a random Poké Ball.

# 🥚 Pokémon Daycare & Shiny Simulator 🌟

This is a simple command-line simulator written in Python that recreates the experience of receiving an egg from a Pokémon Daycare and hatching it, featuring the exciting chance of the Pokémon being a *Shiny*.

## How It Works

The program simulates the following steps, using dramatic pauses to build anticipation:

1.  **Receiving the Egg:** The program informs you that you have received an Egg from the Daycare.
2.  **Pokémon Lottery:** A starter Pokémon is randomly selected from a list of over 25 options.
3.  **The "Shiny" Logic:**
    * Two values are randomly generated from 1 to 512: the player's "Trainer Shiny Value" (TSV) and the egg's "Pokémon Shiny Value" (PSV).
    * If these two numbers are **exactly the same** (`TSV == PSV`), the Pokémon that hatches will be Shiny! This simulates a probability of **1 in 512**.
    * When a Shiny Pokémon hatches, the notification message is displayed in **yellow** in the terminal.
4.  **Random Attributes:**
    * **Nature Assignment:** Each hatched Pokémon is now assigned a random Nature from a list of 25 possible natures.
    * **Expanded IV System:** The script now generates five Individual Values (Attack, Special Attack, Defense, Special Defense, and Speed), each with a random value from 0 to 31.
5.  **IV Judge:** After hatching, a "Judge" evaluates the Pokémon's potential by summing its IVs and giving a rating, from "Ok stats" to "Amazing Stats".
6.  **The Hatching:** After a pause, the program announces which Pokémon has hatched and reveals all of its details: if it's Shiny, its Nature, its IVs, its Judge rating, and the Poké Ball it came in.

## How to Use

The program is designed to be an automatic simulation. You do not need to enter any commands after running it.

1.  Make sure you have Python installed on your system.
2.  Save the code as `ShinyPokemon.py`.
3.  Open your terminal or command prompt.
4.  Run the script with the following command:

    ```sh
    python ShinyPokemon.py
    ```
5.  Now, just wait and see what you get!

## Technologies Used

* **Python 3**
* `random` module (for the `randint` and `choice` functions)
* `time` module (for the `sleep` function)
