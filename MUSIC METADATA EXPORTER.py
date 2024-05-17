#!/usr/bin/env python
# coding: utf-8

# <!-- PYTHON PROJECT HEADER -->
# <img src = "IMPORT FILES/PythonProjectHeader.png" alt = "Python Project Header" style = "display: block; margin: 0 auto; max-width: 100%; width: 100%; margin-bottom: 5px">
# 
# <!-- PYTHON PROJECT ICONS -->
# <div style = "display: flex; justify-content: center; align-items: center; width: 100%;">
#     <div style = "display: flex; justify-content: center; align-items: center; width: 100%; vertical-align: middle;">
#         <!-- E-MAIL -->
#         <a href = "mailto:norieneil_acosta@outlook.com" title = "E-MAIL: norieneil_acosta@outlook.com">
#             <img src = "IMPORT FILES/EmailIcon.png" alt = "Email Address" style = "width: 100%;"></a>
#         <!-- PHONE -->
#         &nbsp;
#         <a href = "tel:09673381501" title = "PHONE: 09673381501">
#             <img src = "IMPORT FILES/PhoneIcon.png" alt = "Contact Number" style = "width: 100%;"></a>
#         <!-- LINKEDIN -->
#         &nbsp;
#         <a href = "https://www.linkedin.com/in/norzzielein" title = "LINKEDIN: https://www.linkedin.com/in/norzzielein">
#             <img src = "IMPORT FILES/LinkedInIcon.png" alt = "LinkedIn Account" style = "width: 100%;"></a>
#         <!-- GITHUB -->
#         &nbsp;
#         <a href = "https://github.com/norzzielein" title = "GITHUB: https://github.com/norzzielein">
#             <img src = "IMPORT FILES/GitHubIcon.png" alt = "GitHub Account" style = "width: 100%;"></a>
#         &nbsp;
#         <!-- FACEBOOK -->
#         <a href = "https://www.facebook.com/norzzielein" title = "FACEBOOK: https://www.facebook.com/norzzielein">
#             <img src = "IMPORT FILES/FacebookIcon.png" alt = "Facebook Account" style = "width: 100%;"></a>
#         &nbsp;
#         <!-- INSTAGRAM -->
#         <a href = "https://www.instagram.com/norzzielein" title = "INSTAGRAM: https://www.instagram.com/norzzielein">
#             <img src = "IMPORT FILES/InstagramIcon.png" alt = "Instagram Account" style = "width: 100%;"></a>
#         &nbsp;
#         <!-- TWITTER -->
#         <a href = "https://twitter.com/norzzielein" title = "TWITTER: https://twitter.com/norzzielein">
#             <img src = "IMPORT FILES/TwitterIcon.png" alt = "Twitter Account" style = "width: 100%;"></a>
#     </div>
# </div>
# 
# <!-- PYTHON PROJECT TRAILER -->
# <img src = "IMPORT FILES/PythonProjectTrailer.png" alt = "Python Project Trailer" style = "display: block; margin: 0 auto; max-width: 100%; width: 100%; margin-top: 5px">

# <details>
#     <summary> 
#         <strong style = "cursor: pointer; background-color: rgba(0, 0, 0, 0.4); color: #000000; font-family: Franklin Gothic Heavy; padding: 8px; border-radius: 5px; display: inline-block;"> 
#             🖥️ IMPORTING PYTHON LIBRARIES 
#         </strong> 
#         <br>
#     </summary>
#     <div style = "padding: 8px; padding-left: 0px; text-align: justify;"> 
# In the initial segment of the code, critical Python libraries are imported to lay the foundation for the subsequent tasks. The <strong>os</strong> library facilitates robust file system navigation and directory management to enable seamless interaction with the underlying operating system. Moreover, the inclusion of <strong>pandas</strong> as <strong>pd</strong> expresses our deliberate choice for efficient data manipulation, particularly advantageous in handling tabular data structures inherent in music metadata. Additionally, the integration of <strong>TinyTag</strong> and <strong>MP3</strong> from <strong>mutagen.mp3</strong> is instrumental in catering the specialized needs of music metadata extraction and manipulation, particularly tailored for MP3 files. This empowers the commands with the capability to effectively access and manipulate metadata attributes inherent in MP3 files, underpinning the objective of a comprehensive metadata processing.
#     </div>
# </details>

# In[1]:


import os
import pandas as pd
from tinytag import TinyTag
from mutagen.mp3 import MP3


# <details>
#     <summary> 
#         <strong style = "cursor: pointer; background-color: rgba(0, 0, 0, 0.4); color: #000000; font-family: Franklin Gothic Heavy; padding: 8px; border-radius: 5px; display: inline-block;"> 
#             🖥️ EXTRACTING MUSIC ALBUM ARTS 
#         </strong> 
#         <br>
#     </summary>
#     <div style = "padding: 8px; padding-left: 0px; text-align: justify;"> 
# The <strong>ExtractingMusicAlbumArts</strong> function takes two parameters: <strong>FilePath</strong>, which represents the path of the music file, and <strong>Artist</strong>, which represents the artist name. The code is wrapped within a try-except block, indicating that any potential errors during execution will be caught and handled gracefully. Inside the try block, the code checks if the <strong>FilePath</strong> ends with ".mp3", ensuring that only MP3 files are processed. If it's not an MP3 file, an error message is printed, and the function returns <strong>None</strong>. If the file is indeed an MP3, the code initializes an <strong>Audio</strong> object using the <strong>MP3</strong> class from the <strong>mutagen.mp3</strong> library, passing <strong>FilePath</strong> as the file to be processed. The code then checks if the MP3 file contains album art metadata. If the "<strong>APIC:</strong>" tag is present in the <strong>Audio.tags</strong>, it signifies the presence of album art. If album art is found, the code constructs the destination folders for storing the album art image. It first constructs the path for the "<strong>EXPORT FILES</strong>" folder using <strong>os.path.dirname(os.path.abspath(file))</strong>, which represents the directory of the current Python script. Then, it constructs the path for the "<strong>MUSIC ALBUM ARTS</strong>" folder inside the "<strong>EXPORT FILES</strong>" folder. If the "<strong>EXPORT FILES</strong>" folder does not exist, it is created using <strong>os.makedirs()</strong>. If the "<strong>MUSIC ALBUM ARTS</strong>" folder does not exist, it is likewise created using <strong>os.makedirs()</strong>. The code constructs the file path (<strong>ArtFilePath</strong>) for the album art image by concatenating the destination folder path with the artist's name and ".jpg" extension. It then opens a new file at <strong>ArtFilePath</strong> in binary write mode ("<strong>wb</strong>") and writes the album art data (<strong>Audio.tags["APIC:"].data</strong>) into this file. If the album art is not found in the MP3 file, an error message is printed, and the function returns <strong>None</strong>. If any exception occurs during execution, a warning message is printed along with the exception details, and the function returns <strong>None</strong>.
#     </div>
# </details>

# In[2]:


def ExtractingMusicAlbumArts(FilePath, Artist):
    try:
        if FilePath.endswith(".mp3"):
            Audio = MP3(FilePath)
        else:
            print("ERROR: Unsupported file format. Only MP3 files are supported.")
            return None
        if "APIC:" in Audio.tags:
            ExportFiles = os.path.join(os.getcwd(), "EXPORT FILES")
            MusicAlbumArts = os.path.join(ExportFiles, "MUSIC ALBUM ARTS")
            if not os.path.exists(ExportFiles):
                os.makedirs(ExportFiles)
            if not os.path.exists(MusicAlbumArts):
                os.makedirs(MusicAlbumArts)
            ArtFilePath = os.path.join(MusicAlbumArts, f"{Artist}.jpg")
            with open(ArtFilePath, "wb") as f:
                f.write(Audio.tags["APIC:"].data)            
            return ArtFilePath
        else:
            print(f"ERROR: Album art {os.path.basename(FilePath)} not found.")
            return None
    except Exception as e:
        print(f"WARNING: Error extracting album art {e}.")
        return None


# <details>
#     <summary> 
#         <strong style = "cursor: pointer; background-color: rgba(0, 0, 0, 0.4); color: #000000; font-family: Franklin Gothic Heavy; padding: 8px; border-radius: 5px; display: inline-block;"> 
#             🖥️ FORMATTING MUSIC LENGTH 
#         </strong> 
#         <br>
#     </summary>
#     <div style = "padding: 8px; padding-left: 0px; text-align: justify;"> 
# In the <strong>FormattingMusicLength</strong> function, the input parameter <strong>Length</strong> represents the duration of a music track in seconds. The function begins by calculating the number of minutes and seconds in the track duration. This calculation is performed using integer division (<strong>//</strong>) to determine the number of whole minutes (<strong>Minutes</strong>) and the modulus operator (<strong>%</strong>) to obtain the remaining seconds (<strong>Seconds</strong>). For instance, if the input <strong>Length</strong> is 245 seconds, the calculation would result in <strong>Minutes = 4</strong> (as 245 // 60 equals 4) and <strong>Seconds = 5</strong> (as 245 % 60 equals 5). Finally, the function formats the minutes and seconds into a string representation with leading zeros for both values using the <strong>format()</strong> method. The format string <strong>"{:02d}:{:02d}"</strong> specifies that each value should be displayed as a two-digit integer with leading zeros if necessary. The calculated <strong>Minutes</strong> value is inserted as the first placeholder and <strong>Seconds</strong> as the second placeholder within the format string. The formatted string representing the track length in the format <strong>MM:SS</strong> is then returned as the output of the function.
#     </div>
# </details>

# In[3]:


def FormattingMusicLength(Length):
    Minutes = int(Length // 60)
    Seconds = int(Length % 60)
    return "{:02d}:{:02d}".format(Minutes, Seconds)


# <details>
#     <summary> 
#         <strong style = "cursor: pointer; background-color: rgba(0, 0, 0, 0.4); color: #000000; font-family: Franklin Gothic Heavy; padding: 8px; border-radius: 5px; display: inline-block;"> 
#             🖥️ CONVERTING MUSIC SIZE
#         </strong> 
#         <br>
#     </summary>
#     <div style = "padding: 8px; padding-left: 0px; text-align: justify;"> 
# In the <strong>ConvertingMusicSize</strong> function, the input parameter <strong>Size</strong> represents the size of a music file in bytes. The function begins by converting the file size from bytes to megabytes. This conversion is done by dividing the input <strong>Size</strong> by the product of 1024 (the number of bytes in a kilobyte) and 1024 (the number of kilobytes in a megabyte). For example, if the input <strong>Size</strong> is 3145728 bytes, the calculation would result in <strong>Megabytes = 3145728 / (1024 * 1024) = 3</strong>. Once the size is converted to megabytes, the function proceeds to format the result as a string with two decimal places using the <strong>format()</strong> method. The format specifier <strong>".2f"</strong> indicates that the floating-point number should be displayed with two digits after the decimal point. The calculated <strong>Megabytes</strong> value is inserted into the format string, followed by the unit "MB" to denote megabytes. The formatted string representing the music file size in megabytes is then returned as the output of the function.
#     </div>
# </details>

# In[4]:


def ConvertingMusicSize(Size):
    Megabytes = Size / (1024 * 1024)
    return "{:.2f} MB".format(Megabytes)


# <details>
#     <summary> 
#         <strong style = "cursor: pointer; background-color: rgba(0, 0, 0, 0.4); color: #000000; font-family: Franklin Gothic Heavy; padding: 8px; border-radius: 5px; display: inline-block;"> 
#             🖥️ PROCESSING MUSIC METADATA
#         </strong> 
#         <br>
#     </summary>
#     <div style = "padding: 8px; padding-left: 0px; text-align: justify;"> 
# In the <strong>ProcessingMusicMetadata</strong> function, the input parameter <strong>MusicFolderPath</strong> represents the path to the directory containing music files. The function initializes an empty dictionary called <strong>MusicMetadata</strong> to store metadata information for each music file. The keys of this dictionary represent different metadata attributes such as "MUSIC TITLE", "MUSIC ALBUM", "MUSIC ARTIST", "MUSIC LENGTH", and "MUSIC SIZE", each associated with an empty list as its value. The function then iterates through all files and subdirectories within the specified <strong>MusicFolderPath</strong> using the <strong>os.walk()</strong> method. For each file encountered, it checks if the file ends with the ".mp3" extension to ensure it is an MP3 file. If the file is indeed an MP3 file, the function retrieves its full file path using <strong>os.path.join(root, file)</strong>. It then extracts metadata information from the MP3 file using the <strong>TinyTag.get()</strong> method, creating a <strong>MusicFileTag</strong> object. Next, the function retrieves specific metadata attributes such as title, album, and artist from the <strong>MusicFileTag</strong> object. The title of the music file is obtained by removing the file extension from the file name using <strong>os.path.splitext(os.path.basename(FilePath))[0]</strong>. The duration of the music file is retrieved in seconds from the <strong>MusicFileTag</strong> object, and then formatted into a human-readable format (MM:SS) using the <strong>FormattingMusicLength</strong> function. Similarly, the size of the music file in bytes is obtained using <strong>os.path.getsize(FilePath)</strong> and then converted to megabytes using the <strong>ConvertingMusicSize</strong> function. Additionally, the function calls the <strong>ExtractingMusicAlbumArts</strong> function to extract and save album artwork associated with the music file. Finally, the extracted metadata attributes are appended to the corresponding lists within the <strong>MusicMetadata</strong> dictionary. Once all files have been processed, the populated <strong>MusicMetadata</strong> dictionary containing metadata information for all MP3 files within the specified folder is returned as the output of the function.
#     </div>
# </details>

# In[5]:


def ProcessingMusicMetadata(MusicFolderPath):
    MusicMetadata = {"MUSIC TITLE": [], "MUSIC ALBUM": [], "MUSIC ARTIST": [], "MUSIC LENGTH": [], "MUSIC SIZE": []}
    for root, dirs, files in os.walk(MusicFolderPath):
        for file in files:
            if file.endswith(".mp3"):
                FilePath = os.path.join(root, file)
                MusicFileTag = TinyTag.get(FilePath)
                MusicTitle = os.path.splitext(os.path.basename(FilePath))[0]
                MusicAlbum = MusicFileTag.album
                MusicArtist = MusicFileTag.artist
                MusicLength = FormattingMusicLength(MusicFileTag.duration)
                MusicSize = ConvertingMusicSize(os.path.getsize(FilePath))
                AlbumArtFile = ExtractingMusicAlbumArts(FilePath, MusicArtist)
                MusicMetadata["MUSIC TITLE"].append(MusicTitle)
                MusicMetadata["MUSIC ALBUM"].append(MusicAlbum)
                MusicMetadata["MUSIC ARTIST"].append(MusicArtist)
                MusicMetadata["MUSIC LENGTH"].append(MusicLength)
                MusicMetadata["MUSIC SIZE"].append(MusicSize)
    return MusicMetadata


# <details>
#     <summary> 
#         <strong style = "cursor: pointer; background-color: rgba(0, 0, 0, 0.4); color: #000000; font-family: Franklin Gothic Heavy; padding: 8px; border-radius: 5px; display: inline-block;"> 
#             🖥️ EXPORTING EXCEL FILE
#         </strong> 
#         <br>
#     </summary>
#     <div style = "padding: 8px; padding-left: 0px; text-align: justify;"> 
# In the <strong>ExportingExcelFile</strong> function, the input parameters <strong>ExcelFilePath</strong> and <strong>MusicMetadata</strong> represent the file path where the Excel file will be saved and the metadata dictionary containing music information, respectively. The function is encapsulated within a try-except block, indicating that it attempts to execute the code within the try block, and if any exceptions occur during execution, they will be caught and handled within the except block. Within the try block, the function first converts the <strong>MusicMetadata</strong> dictionary into a pandas DataFrame using <strong>pd.DataFrame(MusicMetadata)</strong>. This DataFrame organizes the metadata information into a tabular format, where each row represents metadata for a specific music track, and each column represents a different attribute such as "MUSIC TITLE", "MUSIC ALBUM", etc. Once the DataFrame is constructed, the <strong>to_excel()</strong> method is invoked to export the DataFrame to an Excel file specified by the <strong>ExcelFilePath</strong>. The parameter <strong>index = False</strong> is passed to exclude the DataFrame index from being included as a column in the Excel file. If the export process completes successfully, a message "EXECUTION: Excel file exported successfully." is printed to indicate successful execution. However, if an exception occurs during the execution of the code within the try block, it will be caught by the except block. The function then prints a warning message indicating the error that occurred during the export process, including details of the exception (if any) obtained using the <strong>Exception as e</strong> syntax.
#     </div>
# </details>

# In[6]:


def ExportingExcelFile(ExcelFilePath, MusicMetadata):
    try:
        MusicDataFrame = pd.DataFrame(MusicMetadata)
        MusicDataFrame.to_excel(ExcelFilePath, index = False)
        print("EXECUTION: Excel file exported successfully.")
    except Exception as e:
        print(f"WARNING: Error exporting to Excel {e}.")


# <details>
#     <summary> 
#         <strong style = "cursor: pointer; background-color: rgba(0, 0, 0, 0.4); color: #000000; font-family: Franklin Gothic Heavy; padding: 8px; border-radius: 5px; display: inline-block;"> 
#             🖥️ EXECUTING DEFINED FUNCTIONS
#         </strong> 
#         <br>
#     </summary>
#     <div style = "padding: 8px; padding-left: 0px; text-align: justify;"> 
# For the final segment of the code, the variable <strong>MusicFolderPath</strong> is assigned the path to the directory containing the music files. This path, <strong>"C:\Users\Norie Neil Acosta\Documents\Norie Neil Acosta\Music Soundscape"</strong>, specifies the location of the music files to be processed. The variable <strong>ExportFolderPath</strong> is created using the <strong>os.path.join()</strong> function to concatenate the directory path of the Python script with the folder name "EXPORT FILES". This ensures that the path points to the directory where the Excel file will be exported. The variable <strong>ExcelFilePath</strong> is constructed by joining the <strong>ExportFolderPath</strong> with the filename "Music Metadata.xlsx". This specifies the complete path to the Excel file where the music metadata will be exported. The function <strong>ProcessingMusicMetadata(MusicFolderPath)</strong> is called with <strong>MusicFolderPath</strong> as its argument. This function processes the metadata of music files located in the specified directory (<strong>MusicFolderPath</strong>) and returns a dictionary containing the metadata information for each music file. The returned dictionary, <strong>MusicMetadata</strong>, stores attributes such as "MUSIC TITLE", "MUSIC ALBUM", "MUSIC ARTIST", "MUSIC LENGTH", and "MUSIC SIZE" for each music file. The function <strong>ExportingExcelFile(ExcelFilePath, MusicMetadata)</strong> is called with <strong>ExcelFilePath</strong> and <strong>MusicMetadata</strong> as arguments. This function exports the music metadata stored in the <strong>MusicMetadata</strong> dictionary to an Excel file specified by <strong>ExcelFilePath</strong>. The metadata is organized into a tabular format within the Excel file, enabling easy access and analysis of the music information.
#     </div>
# </details>

# In[7]:


MusicFolderPath = r"C:\Users\Norie Neil Acosta\Documents\Norie Neil Acosta\Music Soundscape"
ExportFolderPath = os.path.join(os.getcwd(), "EXPORT FILES")
ExcelFilePath = os.path.join(ExportFolderPath, "MusicMetadata.xlsx")
MusicMetadata = ProcessingMusicMetadata(MusicFolderPath)
ExportingExcelFile(ExcelFilePath, MusicMetadata)


# <!-- PYTHON PROJECT HEADER -->
# <img src = "IMPORT FILES/PythonProjectFooter.png" alt = "Python Project Footer" style = "display: block; margin: 0 auto; max-width: 100%; width: 100%">
