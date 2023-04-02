from pytube import YouTube

with open("files.txt", "r") as f:
    links = f.read()

links = links.split("\n")
i = 1
for each_link in links:
    try:
        if not each_link or each_link == "":
            continue
        
        yt = YouTube(each_link)
        print("Downloading file no: " + str(i) + " - " + yt.title)
        obj = yt.streams.filter(progressive=True, res="720p")

        if not obj:
            print("Did not get 720p for file: " + str(i) + " - " + yt.title + ". Going for 360p")
            obj = yt.streams.filter(progressive=True, res="360p")
            if not obj:
                print("Even 360p is not available for the video.")
                print("Skipping video: " + str(i) + " - " + yt.title)
            
        try:
            obj_to_download = obj[0]
            itag_of_obj = obj_to_download.itag
            stream_to_downaload = yt.streams.get_by_itag(itag_of_obj)
            stream_to_downaload.download("downloaded_files/")
            print("Completed downloading file no: " + str(i) + " - " + yt.title)
        except Exception as e:
            print("No youtube object found.")
            print(str(e))

    except:
        print("Could not download file no: " + str(i))

    i += 1
