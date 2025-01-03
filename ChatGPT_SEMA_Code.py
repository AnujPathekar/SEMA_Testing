import os
import subprocess
import json
from pathlib import Path

def clone_repo(repo_url, clone_dir):
    """Clones the repository into a specified directory."""
    if not os.path.exists(clone_dir):
        subprocess.run(["git", "clone", repo_url, clone_dir], check=True)
    else:
        print(f"Repository already cloned in {clone_dir}")

def check_licenses(clone_dir):
    """Checks licenses of Python dependencies in the repository."""
    subprocess.run(["pip", "install", "pip-licenses"], check=True)
    os.chdir(clone_dir)
    result = subprocess.run(
        ["pip-licenses", "--format=json"], capture_output=True, text=True
    )
    licenses = json.loads(result.stdout)
    print("\nLicenses in the repository:")
    for license in licenses:
        print(f"Package: {license['Name']}, License: {license['License']}")

def scan_vulnerabilities(clone_dir):
    """Scans for vulnerabilities in Python dependencies using `safety`."""
    subprocess.run(["pip", "install", "safety"], check=True)
    requirements_file = Path(clone_dir) / "requirements.txt"

    if not requirements_file.exists():
        print("requirements.txt not found in the repository.")
        return

    result = subprocess.run(
        ["safety", "check", "--file", str(requirements_file), "--json"],
        capture_output=True,
        text=True,
    )
    vulnerabilities = json.loads(result.stdout)
    print("\nVulnerabilities found:")
    for vuln in vulnerabilities:
        print(
            f"Package: {vuln['name']}, Installed: {vuln['version']}, Vulnerable: {vuln['vulnerable_spec']}"
        )
        print(f"Advisory: {vuln['advisory']}")

if __name__ == "__main__":
    repo_url = "https://github.com/AnujPathekar/WebGoatSCC"
    clone_dir = "./WebGoatSCC"

    # Clone the repository
    print("Cloning repository...")
    clone_repo(repo_url, clone_dir)

    # Check licenses
    print("\nChecking licenses...")
    check_licenses(clone_dir)

    # Scan vulnerabilities
    print("\nScanning for vulnerabilities...")
    scan_vulnerabilities(clone_dir)
