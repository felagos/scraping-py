## scraping-py

scraping-py is a Python project designed for web scraping tasks. It provides tools and scripts to extract data from websites efficiently and can be extended for various scraping needs.

### Project Structure

```
src/
  scraping_py/
    __init__.py
    main.py
```

### Available Scripts

The following scripts are declared in `pyproject.toml`:

- **scrape**: Runs the `main` function from `scraping_py.main`. Use:
  ```bash
  poetry run scrape
  ```

You can also run the main script directly:
```bash
poetry run python src/scraping_py/main.py
```

### Getting Started

1. **Install dependencies** (recommended: use [Poetry](https://python-poetry.org/)):
   ```bash
   poetry install
   ```

2. **Run the main script:**
   ```bash
   poetry run python src/scraping_py/main.py
   ```

### Features
- Modular code for scraping
- Easy to extend for new websites
- Poetry for dependency management

### Requirements
- Python 3.8+
- Poetry

### License
MIT
