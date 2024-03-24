# MotionSense: Video-Driven Motion Analyzer

MotionSense is a project aimed at analyzing object motion in videos using computer vision techniques.

## Description

MotionSense is an application for detecting, tracking, and analyzing the motion of objects within video footage. By leveraging computer vision algorithms, MotionSense offers insights into the velocity, acceleration, trajectory, and other motion characteristics of objects captured in videos.

## Features

- Object detection: Identify objects of interest within video frames.
- Motion tracking: Track the movement of objects across multiple frames.
- Velocity and acceleration analysis: Calculate the velocity and acceleration of objects over time.
- Trajectory visualization: Visualize the trajectory of objects within the video.
- Provide the graphical analysis of the video and acceleration of the Objects

## Technologies Used
- Python
- OpenCV in Python
- DIP ( Digital Image Processing )
- Tkinter ( UI for the User )
- Matplotlib ( Visualizing speed and acceleration graphs )

## Installation

To use MotionSense, follow these steps:

1. Clone the MotionSense repository to your local machine:
   
       git clone https://github.com/anubhav-234/MotionSense-Video-Driven-Object-Motion-Analysis.git

3. Install the required dependencies:

       Python:  Install python from [Python](https://www.python.org/downloads/)
       OpenCv: pip install opencv-python
       Matplotlib: pip install matplotlib

## Usage

To analyze motion in a video using MotionSense, execute the file start.py which will automaticall execute the whole project.

## Working

The MotionSense project operates through the following key steps:

1. **Object Detection:** Utilizing advanced background subtraction techniques, MotionSense identifies and isolates objects within a given video frame.

   ![photo1711276714](https://github.com/anubhav-234/MotionSense-Video-Driven-Object-Motion-Analysis/assets/86945010/9ecd76d6-130d-4316-b7c3-9306f8df2d48)

2. **Centroid Declaration:** A centroid, representing the center of the detected object's boundary, is identified and marked for further analysis.

   ![photo1711274736 (3)](https://github.com/anubhav-234/MotionSense-Video-Driven-Object-Motion-Analysis/assets/86945010/a8d78ba9-aa8a-46ee-bf45-9f99d2a3827b)

3. **Motion Tracking:** The movement of the centroid is tracked across subsequent frames, enabling the extraction of valuable velocity and acceleration data.

   ![photo1711274736](https://github.com/anubhav-234/MotionSense-Video-Driven-Object-Motion-Analysis/assets/86945010/8abb1f3a-7208-40bd-a642-4116252a11d5)

## Contributing

Contributions are welcome! If you'd like to contribute to MotionSense, please follow these guidelines:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/my-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/my-feature`).
5. Create a new pull request.

## License

MotionSense is licensed under the MIT License. See `LICENSE` for more information.
