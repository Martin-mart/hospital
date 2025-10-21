import os
import subprocess
import sys
import webbrowser
from threading import Timer

def open_browser():
    webbrowser.open_new("http://127.0.0.1:8000")

if __name__ == "__main__":
    # Only open browser for the main process, not Django's autoreloader
    if os.environ.get('RUN_MAIN') != 'true':
        Timer(2, open_browser).start()

    python_path = sys.executable
    manage_py = os.path.join(os.getcwd(), "manage.py")

    try:
        subprocess.run([python_path, manage_py, "runserver", "127.0.0.1:8000"], check=True)
    except Exception as e:
        print("Failed to start Django:", e)
        input("Press Enter to close...")
