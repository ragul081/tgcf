import os
import subprocess

def deploy_tgcf():
    # Create project directory
    os.makedirs("my-tgcf", exist_ok=True)
    os.chdir("my-tgcf")

    # Create virtual environment
    subprocess.run(["python3", "-m", "venv", ".venv"])
    
    # Activate virtual environment
    activate_venv = os.path.join(".venv", "bin", "activate")
    subprocess.run(["source", activate_venv], shell=True)

    # Install TGCF
    subprocess.run(["pip", "install", "tgcf"])

    # Check TGCF version
    subprocess.run(["tgcf", "--version"])

    # Set environment variable
    with open(".env", "w") as env_file:
        env_file.write("PASSWORD=tgcf\n")

    # Start TGCF web interface
    subprocess.run(["tgcf-web"])

if __name__ == "__main__":
    deploy_tgcf()


