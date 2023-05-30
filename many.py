import os
import subprocess

input_directory = "../input"
output_directory = "../output"
face_image = "../input/face.jpg"


video_files = [
    os.path.join(input_directory, filename)
    for filename in os.listdir(input_directory)
    if filename.endswith((".mp4", ".avi", ".mov")) and os.path.isfile(os.path.join(input_directory, filename))
]

# Process each video file
for video_file in video_files:
    video_name = os.path.splitext(os.path.basename(video_file))[0]
    output_file = os.path.join(output_directory, video_name + ".mp4")

    # Run the roop script with the appropriate command
    command = f"python run.py -f {face_image} -t {video_file} -o {output_file}"
    subprocess.call(command, shell=True)

    print(f"Processed video: {video_file}")

print("All videos processed.")
