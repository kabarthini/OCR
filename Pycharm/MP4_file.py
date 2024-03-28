import cv2

def get_video_info(file_path):
    try:
        # Open video file
        cap = cv2.VideoCapture(file_path)

        # Get video information
        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        codec = int(cap.get(cv2.CAP_PROP_FOURCC))

        # Calculate bitrate if possible
        bitrate = None
        if fps > 0:
            bitrate = (frame_count / fps) * 8

        # Convert codec to four-character code
        codec_fourcc = "".join([chr((codec >> 8 * i) & 0xFF) for i in range(4)])

        # Print the information
        print(f"Codec: {codec_fourcc}")
        print(f"FPS: {fps}")
        print(f"Frame Count: {frame_count}")
        print(f"Bitrate: {bitrate} bps (approx)")

        # Release video capture object
        cap.release()

    except Exception as e:
        print(f"Error: {e}")

# Example usage
video_file_path = r"C:\Internship\PycharmProjects\ocr\Video.mp4"
get_video_info(video_file_path)
