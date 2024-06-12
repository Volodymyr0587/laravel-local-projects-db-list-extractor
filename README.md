# Laravel Database Finder

Laravel Database Finder is a PyQt6-based GUI application that helps you extract database paths from Laravel projects. It scans the specified folder for `.env` files and extracts the `DB_DATABASE` values, saving them to a CSV file.

## Features

- Easy-to-use graphical interface built with PyQt6.
- Scans a specified folder (including subfolders) for `.env` files.
- Extracts the `DB_DATABASE` values and saves them to a CSV file.
- Command-line accessible for quick execution.

## Requirements

- Python 3.8 or higher
- PyQt6
- `pyinstaller` for creating the executable

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/laravel-database-finder.git
    cd laravel-database-finder
    ```

2. **Set up a virtual environment**:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Install the package**:
    ```bash
    pip install .
    ```

5. **Create the executable**:
    ```bash
    pyinstaller --onefile --windowed laradb.py
    ```

6. **Add the executable to your PATH**:
    - On Windows: Add the `dist` directory to your system PATH.
    - On macOS/Linux: Add the `dist` directory to your PATH by modifying your shell profile file (e.g., `~/.bashrc`, `~/.bash_profile`, `~/.zshrc`, etc.) and adding:
      ```bash
      export PATH=$PATH:/path/to/your/dist_directory
      ```
    - Apply the changes:
      ```bash
      source ~/.bashrc  # or the relevant profile file
      ```

## Usage

### Graphical Interface

1. Run the application:
    ```bash
    python main.py
    ```

2. Use the GUI to:
    - Browse and select the folder containing your Laravel projects.
    - Specify the output CSV file path.
    - Click "Run" to extract the database paths.

### Command-Line Interface

1. Ensure the executable is in your PATH.
2. Run the application from the terminal:
    ```bash
    laradb
    ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
