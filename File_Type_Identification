import os
import magic
import datetime
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Dictionary of common file signatures (magic numbers)
FILE_SIGNATURES = {
    b'\xFF\xD8\xFF': "JPEG Image (.jpg, .jpeg)",
    b'\x89PNG': "PNG Image (.png)",
    b'GIF8': "GIF Image (.gif)",
    b'%PDF': "PDF Document (.pdf)",
    b'PK\x03\x04': "ZIP or Microsoft Office Document (.zip, .docx, .xlsx)",
    b'Rar!': "RAR Archive (.rar)",
    b'7z\xBC\xAF\x27\x1C': "7-Zip Archive (.7z)",
    b'ID3': "MP3 Audio (.mp3)",
    b'fLaC': "FLAC Audio (.flac)",
    b'OggS': "OGG Audio/Video (.ogg)",
    b'\x00\x00\x01\xBA': "MPEG Video (.mpg, .mpeg)",
    b'\x00\x00\x00\x18ftypmp42': "MP4 Video (.mp4)",
    b'MZ': "Windows Executable (.exe, .dll)",
}

def identify_file_type(file_path):
    """Identify file type based on signature, extension, and MIME type."""
    if not os.path.isfile(file_path):
        print(Fore.RED + "❌ File not found.")
        return

    # Get basic metadata
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)
    file_ext = os.path.splitext(file_path)[1].lower()
    last_modified = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))

    # Read first few bytes
    with open(file_path, "rb") as f:
        file_start = f.read(20)

    # Check signature
    file_type = None
    for signature, description in FILE_SIGNATURES.items():
        if file_start.startswith(signature):
            file_type = description
            break

    # MIME type detection using python-magic
    mime_type = magic.from_file(file_path, mime=True)

    # If no known signature
    if not file_type:
        file_type = f"Unknown (based on signature). Possible extension: {file_ext}"

    # Display results
    print(f"\n📁 {Fore.CYAN}{file_name}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}📏 Size:{Style.RESET_ALL} {file_size} bytes")
    print(f"{Fore.YELLOW}🕓 Last Modified:{Style.RESET_ALL} {last_modified}")
    print(f"{Fore.YELLOW}🔍 Signature Match:{Style.RESET_ALL} {file_type}")
    print(f"{Fore.YELLOW}🧩 MIME Type:{Style.RESET_ALL} {mime_type}")

    # Confidence level
    if "Unknown" in file_type:
        print(Fore.RED + "⚠️ Confidence Level: Low")
    else:
        print(Fore.GREEN + "✅ Confidence Level: High")

def main():
    print(Fore.CYAN + "=== ADVANCED FILE TYPE IDENTIFICATION SYSTEM ===\n")
    while True:
        file_path = input("Enter file path (or type 'exit' to quit): ").strip()
        if file_path.lower() == 'exit':
            print(Fore.YELLOW + "\nExiting program. Goodbye! 👋")
            break
        identify_file_type(file_path)

if __name__ == "__main__":
    main()
