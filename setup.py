import subprocess

# List of required dependencies
dependencies = [
    "numpy",
    "pandas",
    "scikit-learn",
    "matplotlib",
]

# Function to install dependencies using pip
def install_dependencies():
    for dependency in dependencies:
        try:
            subprocess.check_call(["pip", "install", dependency])
            print(f"Successfully installed {dependency}")
        except subprocess.CalledProcessError:
            print(f"Failed to install {dependency}. Please install it manually.")

if __name__ == "__main__":
    print("Starting dependency installation...")
    install_dependencies()
    print("Dependency installation completed.")
