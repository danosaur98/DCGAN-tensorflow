from google_images_download import google_images_download
response = google_images_download.googleimagesdownload()
arguments = {
    "keywords": "Jackson Pollock Art",
    "limit": 1000,
    "print_urls": True,
    "chromedriver": "C:\\Users\\danie\\Downloads\\chromedriver_win32\\chromedriver.exe"
}  # creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images