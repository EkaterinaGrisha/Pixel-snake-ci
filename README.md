# Pixel Snake — polished student project

This project is a compact pixel-style Snake game with separation of game logic and GUI,
designed for easy unit testing and CI integration (GitLab CI/CD).

## Structure
- `src/game.py` — game logic (testable without graphical dependencies)
- `src/gui.py` — pygame-based GUI (visual, separate)
- `tests/` — unit tests for the model (`SnakeModel`)
- `assets/` — pixel sprites (head, body, food)
- `.gitlab-ci.yml` — pipeline configuration to run tests on each push
- `requirements.txt` — runtime dependencies (pygame, pillow)

## How to run locally
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run tests:
   ```bash
   python -m unittest discover -s tests -v
   ```
3. Run the game (needs display):
   ```bash
   python -m src.gui
   ```

## Notes for the report
- Logic is decoupled from GUI to allow CI to run tests without display or pygame.
- The pipeline uses official Python image and runs unit tests on each commit.
