import threading
import webbrowser
import time
from pms import app  # replace 'app' with your Flask file name (without .py)

def open_browser():
    time.sleep(2)
    webbrowser.open_new("http://127.0.0.1:5000")

if __name__ == "__main__":
    threading.Thread(target=open_browser).start()
    app.run(port=5000, debug=False)
