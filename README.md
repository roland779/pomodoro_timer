# Enhanced Pomodoro Timer

An advanced Pomodoro Timer application with a graphical user interface (GUI) built using Python's Tkinter library. This timer is designed to help you implement the Pomodoro Technique, a time management method proven to enhance focus and productivity.

## What is the Pomodoro Technique?

The Pomodoro Technique is a time management strategy developed by Francesco Cirillo. It involves breaking your work into intervals, traditionally 25 minutes long, separated by short breaks. Each interval is called a "Pomodoro." 

This method helps to:
- Improve focus and concentration.
- Prevent burnout by encouraging regular breaks.
- Increase productivity through structured work sessions.
- Reduce mental fatigue by alternating work and rest.

The typical cycle:
1. Work for 25 minutes (1 Pomodoro).
2. Take a 5-minute short break.
3. After 4 Pomodoros, take a longer break (15-30 minutes).

This app allows you to fully customize work and break durations, adapting the technique to your needs.

---

## Features

- **Customizable Timer Durations**: Adjust work, short break, and long break times.
- **Activity Log**: Tracks the start and end times of each phase and logs them in a scrollable window.
- **Pause/Resume Functionality**: Pause the timer and resume at any time.
- **Desktop Notifications**: Receive notifications at the end of each phase (via `plyer`).
- **Progress Bar**: Visualize your progress during each phase.
- **Cycle Support**: Configure the number of Pomodoro cycles.
- **Mute Option**: Disable sound notifications if preferred.
- **Responsive GUI**: Resizable window for better usability.

---

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Steps

1. Clone the Repository:
   ```bash
   git clone https://github.com/roland779/enhanced-pomodoro-timer.git
   cd enhanced-pomodoro-timer
   ```

2. Install Dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   Contents of `requirements.txt`:
   ```
   plyer
   tkinter
   ```

3. Run the Application:
   ```bash
   python pomodoro_timer.py
   ```

---

## How to Use

1. Launch the application.
2. Enter your desired durations for work, short breaks, and long breaks in minutes.
3. Set the number of Pomodoro cycles you wish to complete.
4. Click **Start** to begin the timer.
5. Use the **Pause/Resume** button to pause or continue your session.
6. Monitor your session using the countdown timer, progress bar, and activity log.
7. Notifications and sounds will alert you when each phase starts or ends.

---

## Screenshots

_Add screenshots of the application here to demonstrate its UI._

---

## Compatibility

- **Operating System**: Windows, macOS, Linux
- **Python Version**: 3.6 or higher

---

## Known Issues

- The `winsound` module used for sound notifications works only on Windows. For cross-platform compatibility, you can replace it with `playsound` or `pygame` in future versions.
- Precision may vary slightly depending on system performance.

---

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes with descriptive messages.
4. Push the branch to your fork.
5. Create a pull request describing your changes.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Python's [Tkinter](https://docs.python.org/3/library/tkinter.html) library for the GUI.
- [Plyer](https://plyer.readthedocs.io/) for desktop notifications.
- Inspired by Francesco Cirillo's [Pomodoro Technique](https://francescocirillo.com/pages/pomodoro-technique).
