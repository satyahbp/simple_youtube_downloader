from pytube import YouTube
from tqdm import tqdm

class YoutubeDownload:
    def __init__(self) -> None:
        self.progress_bar = None
        self.completed = 0


    @staticmethod
    def read_from_file(file_name):
        with open(file_name, "r") as f:
            links = f.read()
        links = links.split("\n")
        return links
    

    def tracking_progress(self, progress_data, current_byte, remaining_bytes):
        if not self.progress_bar:
            self.progress_bar = tqdm(range(progress_data.filesize), unit="B", unit_scale=True, colour="#344feb")
        current_chunk = progress_data.filesize - remaining_bytes - self.completed
        self.completed = self.completed + current_chunk
        self.progress_bar.update(current_chunk)

    
    def completing_track(self, a,  b):
        self.progress_bar = None
        self.completed = 0

    
    def download(self):
        links = self.read_from_file("files.txt")
        i = 1
        for each_link in links:
            try:
                if not each_link or each_link == "":
                    continue
                
                yt = YouTube(each_link, on_progress_callback=self.tracking_progress, on_complete_callback=self.completing_track)
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


YoutubeDownload().download()