import os
import subprocess

def deploy_tgcf():
    # Create project directory
    os.makedirs("my-tgcf", exist_ok=True)
    os.chdir("my-tgcf")

    # Create virtual environment
    subprocess.run(["python3", "-m", "venv", ".venv"])

    # Upgrade pip and setuptools
    subprocess.run([".venv/bin/pip", "install", "--upgrade", "pip", "setuptools", "wheel"])

    # Install compatible numpy version
    subprocess.run([".venv/bin/pip", "install", "numpy"])  # Adjusted version

    # Install Poetry
    subprocess.run([".venv/bin/pip", "install", "poetry"])

    # Run Poetry install
    subprocess.run([".venv/bin/poetry", "install"])

    # Set environment variable
    with open(".env", "w") as env_file:
        env_file.write("PASSWORD=tgcf\n")

    # Start TGCF web interface
    subprocess.run(["tgcf-web"])

if __name__ == "__main__":
    deploy_tgcf()
