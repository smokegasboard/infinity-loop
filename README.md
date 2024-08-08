# infinity-loop
This Python script automatically opens and closes a specified application after a set interval. For good for infinity

**Description:**
This Python script automates the opening and closing of a specified application with a customizable delay.

**Installation:**
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/app-auto-open-close.git
   ```
2. Ensure you have Python installed.

**Usage:**

1. **Edit the script:**
   - Open the `app_auto_open_close.py` file in a text editor.
   - Replace `C:\Program Files\WinRAR\WinRAR.exe` with the desired application path.
   - Adjust the `delay` variable to set the desired time between opening and closing.
2. **Run the script:**
   ```bash
   python app_auto_open_close.py
   ```
3. **Stop the script:**
   Press `Ctrl+C` to terminate the script.

**Dependencies:**
* `os`
* `time`
* `subprocess`

**Note:**
* This script uses `subprocess` to manage the application process, which is generally more reliable than `taskkill`.
* Consider adding error handling and logging for more robust behavior.
* For advanced usage, explore command-line arguments or configuration files.

**License:**
MIT License

**Contributing:**
Feel free to contribute to this project by submitting issues or pull requests.

**Buy Me Coffee**
3KFthrrU1xKsYrAVVWZ8iqqmqzg6RQwMXB

