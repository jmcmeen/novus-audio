from .globals import supported_audio_file_extensions
from novus_pytils.files import get_files_by_extension

def count_audio_files(audio_folder_path, file_extensions=supported_audio_file_extensions):
    """Count the number of audio files in a folder.

    Args:
        audio_folder_path (str): The path to the folder containing the audio files.
        file_extensions (list, optional): A list of file extensions to consider as audio files. Defaults to supported_audio_file_extensions.

    Returns:
        int: The number of audio files in the folder.
    """
    files = get_files_by_extension(audio_folder_path, file_extensions)
    return len(files)
