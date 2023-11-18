import subprocess

def run_scripts(scripts):
    for script in scripts:
        try:
            result = subprocess.run(["python", script], check=True, text=True, stdout=subprocess.PIPE)
            print(f"Script {script} executed successfully with output:\n{result.stdout}")
        except subprocess.CalledProcessError as e:
            print(f"Script {script} execution failed with error:\n{e}")

if __name__ == "__main__":
    script_dir = "/Wallpaper-MGMT/Archive/Wallpapers"
    
    # List of scripts to be executed in sequence
    scripts_to_run = [
        f"{script_dir}\\0.5-duplicates.py",
        f"{script_dir}\\2-portorait.py",
        f"{script_dir}\\3.5-uw-sort.py",
        f"{script_dir}\\3.75-uw-width.py",
        f"{script_dir}\\3.80-uw-name.py",
        f"{script_dir}\\3-width.py",
        f"{script_dir}\\4-name by date.py",
        f"{script_dir}\\5-port-height.py",
        f"{script_dir}\\6-port-name by date.py",
        # Add paths to other scripts here
    ]

    run_scripts(scripts_to_run)
