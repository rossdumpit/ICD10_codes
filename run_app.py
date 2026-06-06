import threading
import webview
import uvicorn
from main import app

def run_server():
    uvicorn.run(app, host="127.0.0.1", port=8000)

if __name__ == "__main__":
    # start FastAPI in background thread
    t = threading.Thread(target=run_server, daemon=True)
    t.start()

    # open desktop window
    webview.create_window("ICD Search", "http://127.0.0.1:8000")
    webview.start(gui="qt")