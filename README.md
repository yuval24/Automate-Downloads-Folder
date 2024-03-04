# Download Organizer

The Download Organizer script is a Python tool designed to automatically organize files in your downloads directory based on their file extensions. It monitors a specified directory for newly downloaded files and moves them to appropriate folders according to their file types.

## How to Use

1. **Installation**: Ensure you have Python installed on your system.

2. **Download the Scripts**: Download the `download_monitor.py` and `organize_download_files.py` scripts from this repository.

3. **Dependencies**: Install the necessary dependencies by running:
- pip install watchdog

4. **Configuration**: Open the `organize_download_files.py` and `download_monitor.py` scripts in a text editor and modify the following variables according to your system:
- `DOWNLOADS_PATH`: The path to the directory you want to monitor for new downloads.
- `BASE_NAME`: The base directory where the organized files will be moved.
- `EXT_INSTALLATION`, `EXT_IMAGES`, `EXT_DOCS`, `EXT_AUDIO`, `EXT_COMPRESSION`, `EXT_VIDEO`, `EXT_CODE`: Lists of file extensions corresponding to different file types.

5. **Run the Script**: Execute the script by running:
- python download_monitor.py

6. **Background Execution (Optional)**: To run the script in the background without leaving a terminal open, refer to the section on "Running in the Background" below.

## What it Does

- Monitors the specified directory for new file creations and modifications.
- Automatically moves files to appropriate folders based on their file extensions.
- Prevents duplicate files by checking for existing files with the same names.
- Works efficiently with a minimal delay to accommodate antivirus scans.

## Running in the Background

You can run the script in the background using a task scheduler or service manager on your operating system. Refer to the documentation or tutorials for your specific system:

- **Windows**: Use Task Scheduler to create a task that runs the script at startup or on a schedule.
- **Linux**: Use `systemd` to create a service for the script.
- **macOS**: Use `launchd` to create a daemon for the script.

## License

This project is licensed under the [MIT License](LICENSE).
