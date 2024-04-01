# Prayer Time Tracker

This Python script retrieves and displays prayer times for Lahore, Pakistan, for the year 2024 from the Aladhan API. It also provides a GUI interface built with Tkinter to display the prayer times and remaining time until the next prayer.

## Requirements

- Python 3.x
- requests
- beautifulsoup4
- tkinter

## Installation

1. Clone the repository:

```bash
git clone https://github.com/abdbbdii/prayer-time-tracker.git
```

2. Install the required dependencies:

```bash
pip install requests beautifulsoup4
```

## Usage

1. Run the script:

```bash
python prayer_time_tracker.py
```

2. A window will appear showing the available prayer times. Select the desired time from the dropdown menu and click "OK".

3. Another window will pop up showing the selected prayer time and the remaining time until that prayer.

## Features

- Retrieves prayer times from the Aladhan API.
- Provides a graphical user interface for easy interaction.
- Displays the remaining time until the next prayer dynamically.
- Alerts when the prayer time is due.

## Credits

- [Aladhan](https://aladhan.com/) - For providing the prayer times API.

## License

This project is licensed under the [BSD License](https://github.com/abdbbdii/prayer_timer/blob/main/LICENSE).