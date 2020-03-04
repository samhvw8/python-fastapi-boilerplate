import os.path

def get_run_time_file_path(base_file: str, rel_file_path: str):
    return os.path.join(os.path.dirname(base_file), rel_file_path)
