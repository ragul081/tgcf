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

    # Upgrade pip, setuptools, and wheel
    subprocess.run(["pip", "install", "--upgrade", "pip", "setuptools", "wheel"])

    # Install numpy with PEP 517
    subprocess.run(["pip", "install", "numpy==1.23.5", "--use-pep517"])

    # Install Poetry
    subprocess.run(["pip", "install", "poetry"])

    # Run Poetry install
    subprocess.run(["poetry", "install"])

    # Set environment variable
    with open(".env", "w") as env_file:
        env_file.write("PASSWORD=tgcf\n")

    # Start TGCF web interface
    subprocess.run(["tgcf-web"])

if __name__ == "__main__":
    deploy_tgcf()
