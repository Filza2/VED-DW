# VED-DW
Youtube Video Download Tool / Hammel app search 

In the Youtube download , after you download "youtube_dl" and "pafy" you must edit this in order to run the tool ,

Library name : File Name : Line ( what you need to delete )

youtube_dl : YoutubeDL.py : Line number 329 delete > 'dislike_count',
pafy : backend_internal.py : Line number 132 delete > self._dislikes = int(statistics["dislikeCount"])
pafy : backend_shared.py : Line number 71 delete > self._dislikes = None
pafy : backend_shared.py : delete From Line 319 To Line 325 (dislikes def ) <<<
pafy : backend_youtube_dl.py : Line 54 delete > self._dislikes = self._ydl_info['dislike_count']
pafy : playlist.py : Line 67 delete > dislikes=allinfo.get('dislikes'),
pafy : playlist.py : Line 86 delete > dislikes=v.get('dislikes'),
pafy : playlist.py : Line 334 delete > dislikes=stats.get('dislikeCount', 0),

You need to delete/edit these thing's becuse Owner of those Librarys didn't update it for the new youtube update wish is don't show the dislike's 
And thanks for using our tool , And sorry for Disturbance , you will need to modify that unless the "pafy" and "youtube_dl" owners update thir Librarys
