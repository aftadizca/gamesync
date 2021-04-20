from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from filetype import fileType

gauth = GoogleAuth()
gauth.LocalWebserverAuth()  # Creates local webserver and auto handles authentication.

drive = GoogleDrive(gauth)

# file1 = drive.CreateFile(
#     {"title": "Hello.txt", "parents": [{"id": "1xfNntheiJVo0KwRtn4McDxsCPW7P6JYt"}]}
# )  # Create GoogleDriveFile instance with title 'Hello.txt'.
# file1.SetContentString("Hello World!")  # Set content of the file from given string.
# file1.Upload()
isFolderAvailable = False
folderId = ""
file_list = drive.ListFile(
    {"q": f"mimeType = '{fileType.folder}' and trashed=false"}
).GetList()
for file1 in file_list:
    print("title: %s, id: %s" % (file1["title"], file1["id"]))
    if file1["title"] == "GameSavedBackup":
        isFolderAvailable = True
        folderId = file1["id"]
        break


if not isFolderAvailable:
    folder = drive.CreateFile(
        {"title": "GameSavedBackup", "mimeType": fileType.folder}
    )  # Create GoogleDriveFile instance with title 'Hello.txt'.
    # file1.SetContentString("Hello World!")  # Set content of the file from given string.
    folder.Upload()
    folderId = folder["id"]
    print("Folder Created")

file2 = drive.CreateFile(
    {
        "title": "test.png",
        "parents": [{"id": folderId}],
    }
)  # Create GoogleDriveFile instance with title 'Hello.txt'.
file2.SetContentFile("test.png")  # Set content of the file from given string.
file2.Upload()
print("title: %s, hash: %s" % (file2["title"], file2["md5Checksum"]))