# stop_processes.py
import psutil

def find_processes_using_files(directory_paths):
    processes_to_stop = []
    for proc in psutil.process_iter(['pid', 'name', 'open_files']):
        try:
            for f in proc.info['open_files']:
                if any(directory.lower() in f.path.lower() for directory in directory_paths):
                    processes_to_stop.append(proc)
                    break
        except (psutil.NoSuchProcess, psutil.AccessDenied, TypeError):
            pass
    return processes_to_stop

def stop_processes(process_list):
    for proc in process_list:
        proc.terminate()
    for proc in process_list:
        proc.wait()

if __name__ == "__main__":
    directory_paths = ["C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers", 
                       "C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers_Portrait"]
    
    processes = find_processes_using_files(directory_paths)
    stop_processes(processes)
