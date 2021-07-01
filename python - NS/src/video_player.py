"""A video player class."""

from .video_library import VideoLibrary
import random

is_playing = False
old_video = None

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        videos_list = self._video_library.get_all_videos()
        print("Here's a list of all available videos:")
        temp_list = []
        
        for i in videos_list:
#            b =[]
            if len(i.tags) != 0:
                temp_list += [f"{i.title} ({i.video_id}) [{i.tags[0]} {i.tags[1]}]"]
# I tried to genralise for the number of tags but couldn't make it work - any feedback on this would be appreciated.                
#                a = [f"{i.title} ({i.video_id}) ["]
#                for k in list(range(len(i.tags))):
#                    b += f"{i.tags[k]}"
#                    print(b)
#                temp_list += a+b
                    
            else:
                temp_list += [f"{i.title} ({i.video_id}) []"]
                
        temp_list = sorted(temp_list)
        for u in temp_list:
            print(u)


    def play_video(self, video_id):
    
        global is_playing
        global old_video
        video = self._video_library.get_video(video_id)
        
        if video is None:
#                is_playing = False [Including this passes more tests but unclear why]
                print('Cannot play video: Video does not exist')                
        elif is_playing is False:
                old_video = video.title
                is_playing = True
                print(f"Playing video: {video.title}")               
        else:
                print(f"Stopping video: {old_video}")
                print(f"Playing video: {video.title}")
                old_video = video.title
                is_playing = True
                          
        
        

    def stop_video(self):
        """Stops the current video."""
        global is_playing
        global old_video
        
        if is_playing is True:
            print(f"Stopping video: {old_video}")
        else:
            print("Cannot stop video: No video is currently playing")
        
        is_playing = False
        old_video = None

    def play_random_video(self):
        """Plays a random video from the video library."""
        global is_playing
        global old_video
        
        all_videos = self._video_library.get_all_videos()
        random.shuffle(all_videos)
            
        if is_playing is False:
            print(f"Playing video: {all_videos[0].title}")
        else:
            print(f"Stopping video: {old_video}")
            print(f"Playing video: {all_videos[0].title}")
        
        is_playing = True
        old_video = all_videos[0].title

    def pause_video(self):
        """Pauses the current video."""

        print("pause_video needs implementation")

    def continue_video(self):
        """Resumes playing the current video."""

        print("continue_video needs implementation")

    def show_playing(self):
        """Displays video currently playing."""

        print("show_playing needs implementation")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
