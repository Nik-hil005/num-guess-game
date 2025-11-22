**Development Process**

Below is a breakdown of how the project was developed step‑by‑step:

1. Setting Up the Base Game
    * Started with Python's built-in random module.
    * Created a function to generate a random number.
    * Implemented a loop to allow the user to guess multiple times.
    * Added input validation and feedback messages ("higher", "lower").

2. Adding Attempts Tracking
    * Introduced an attempts_left variable.
    * Decremented attempts with each guess.
    * Added a "Game Over" condition if attempts reach zero.

3. Creating Difficulty Levels
    * To improve gameplay and add variability:
    * Implemented a difficulty selection menu.
    * Difficulty determines the number range and attempts:
        |-- Easy: 1–50, 10 attempts
        |-- Medium: 1–50, 7 attempts
        |--  Hard: 1–100, 10 attempts
    * Refactored the code so difficulty configuration is returned dynamically.

4. Game Replay Feature
    * Added a loop to restart the game without restarting the program.
    * Ensured input validation for the replay prompt.

5. Code Cleanup & User Experience Enhancements
    * Improved prompts and output formatting.
    * Added emojis to enhance engagement.
    * Ensured all invalid inputs were handled gracefully.