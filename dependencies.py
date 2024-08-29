import os
import subprocess

# File paths
requirements_file = 'requirements1.txt'
fixed_requirements_file = 'fixed_requirements.txt'

def parse_requirements(requirements_file):
    with open(requirements_file, 'r') as file:
        lines = file.readlines()
    return lines

def fix_requirements(lines):
    fixed_lines = []
    for line in lines:
        line = line.strip()
        if '@ file://' in line or '@' in line:  # Check for local paths or "@" installs
            package_name = line.split('@')[0].strip()
            print(f"Fixing package: {package_name}")

            # Uninstall the package
            subprocess.run(['pip', 'uninstall', '-y', package_name])

            # Reinstall the package from PyPI
            subprocess.run(['pip', 'install', package_name])

            # Get the version and add it to fixed requirements
            version = subprocess.check_output(['pip', 'show', package_name]).decode('utf-8')
            version_line = next((v for v in version.splitlines() if v.startswith('Version:')), None)
            if version_line:
                version_number = version_line.split(': ')[1]
                fixed_lines.append(f'{package_name}=={version_number}')
        else:
            fixed_lines.append(line)

    return fixed_lines

def write_fixed_requirements(fixed_lines, fixed_requirements_file):
    with open(fixed_requirements_file, 'w') as file:
        file.write('\n'.join(fixed_lines))

def main():
    if not os.path.exists(requirements_file):
        print(f"Error: {requirements_file} not found.")
        return

    print("Reading requirements...")
    lines = parse_requirements(requirements_file)

    print("Fixing requirements...")
    fixed_lines = fix_requirements(lines)

    print(f"Writing fixed requirements to {fixed_requirements_file}...")
    write_fixed_requirements(fixed_lines, fixed_requirements_file)

    print("Done! Please check the fixed_requirements.txt file.")

if __name__ == '__main__':
    main()