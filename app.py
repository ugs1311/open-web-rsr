from flask import Flask, jsonify, request
import subprocess
import os
import time

app = Flask(__name__)

# Configuration (adjust these as needed)
OLLAMA_INSTALL_DIR = "/opt/ollama"  # Or wherever you prefer
OPEN_WEBUI_INSTALL_DIR = "/opt/open-webui" # Or wherever you prefer
OLLAMA_BINARY = os.path.join(OLLAMA_INSTALL_DIR, "ollama")
OPEN_WEBUI_SCRIPT = os.path.join(OPEN_WEBUI_INSTALL_DIR, "run.sh") # Or the appropriate startup script
OLLAMA_MODEL_NAME = "llama2" # Example model, replace as needed
OPEN_WEBUI_PORT = 7860  # Default port, change if needed


def install_ollama():
    """Installs Ollama."""
    try:
        if not os.path.exists(OLLAMA_INSTALL_DIR):
            os.makedirs(OLLAMA_INSTALL_DIR, exist_ok=True)  # Create the directory
            # Download and install (replace with actual installation commands for your OS)
            subprocess.run(["curl", "-fsSL", "https://ollama.ai/install.sh", "|", "sh"], shell=True, check=True, cwd=OLLAMA_INSTALL_DIR) # Example, adapt as needed.
            print("Ollama installed successfully.")
        else:
            print("Ollama already installed.")

        # Pull the model (if it doesn't exist)
        model_path = os.path.join(OLLAMA_INSTALL_DIR, "models", OLLAMA_MODEL_NAME) # Assumes default ollama model location
        if not os.path.exists(model_path):
            subprocess.run([OLLAMA_BINARY, "pull", OLLAMA_MODEL_NAME], check=True)
            print(f"Model {OLLAMA_MODEL_NAME} pulled.")
        else:
            print(f"Model {OLLAMA_MODEL_NAME} already exists.")

        return True
    except subprocess.CalledProcessError as e:
        print(f"Ollama installation failed: {e}")
        return False
    except Exception as e:
        print(f"An error occurred during Ollama installation: {e}")
        return False



def install_open_webui():
    """Installs Open WebUI (example - adapt as needed)."""
    try:
        if not os.path.exists(OPEN_WEBUI_INSTALL_DIR):
            os.makedirs(OPEN_WEBUI_INSTALL_DIR, exist_ok=True)
            # Example:  Replace with your Open WebUI installation steps (e.g., git clone)
            #  Example for git clone
            # subprocess.run(["git", "clone", "YOUR_OPEN_WEBUI_REPO_URL", OPEN_WEBUI_INSTALL_DIR], check=True) # Replace with your repo URL
            print("Open WebUI installation needs to be implemented (example git clone or other install methods).") # Reminder!
            return False # Indicate that this part is not yet fully implemented
            # ... (more installation steps like setting up virtual env, dependencies, etc.) ...
        else:
            print("Open WebUI already exists. Skipping installation.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Open WebUI installation failed: {e}")
        return False
    except Exception as e:
        print(f"An error occurred during Open WebUI installation: {e}")
        return False


def run_ollama():
    """Runs Ollama in the background."""
    try:
         # Check if Ollama is already running (you might need a better check)
        # ... (implementation needed) ...
        # Example using `pgrep` (Linux/macOS)
        # if subprocess.run(["pgrep", "-f", "ollama"], capture_output=True).returncode == 0:
        #     print("Ollama is already running.")
        #     return True

        subprocess.Popen([OLLAMA_BINARY], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)  # Run in background
        print("Ollama started.")
        time.sleep(2)  # Give it a little time to start
        return True
    except Exception as e:
        print(f"Error starting Ollama: {e}")
        return False


def run_open_webui():
    """Runs Open WebUI in the background."""
    try:
        # Check if Open WebUI is already running (you might need a better check)
        # ... (implementation needed) ...
        # Example using `pgrep` (Linux/macOS)
        # if subprocess.run(["pgrep", "-f", "run.sh"], capture_output=True).returncode == 0:
        #     print("Open WebUI is already running.")
        #     return True
        subprocess.Popen([OPEN_WEBUI_SCRIPT, "--port", str(OPEN_WEBUI_PORT)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, cwd=OPEN_WEBUI_INSTALL_DIR)  # Run in background, set port
        print("Open WebUI started.")
        return True
    except Exception as e:
        print(f"Error starting Open WebUI: {e}")
        return False


@app.route("/install")
def install():
    """Installs Ollama and Open WebUI."""
    if install_ollama() and install_open_webui(): # Install both
        return jsonify({"message": "Installation successful."}), 200
    else:
        return jsonify({"message": "Installation failed."}), 500


@app.route("/start")
def start():
    """Starts Ollama and Open WebUI."""
    if run_ollama() and run_open_webui(): # Start both
       return jsonify({"message": "Services started."}), 200
    else:
        return jsonify({"message": "Failed to start services."}), 500


@app.route("/status")
def status():
    """Checks the status of Ollama and Open WebUI (stub)."""
    # TODO: Implement actual status checks (e.g., check processes, ports, etc.)
    return jsonify({"message": "Status check not yet implemented."}), 200



if __name__ == "__main__":
    app.run(debug=True, port=5000) # Run Flask app
