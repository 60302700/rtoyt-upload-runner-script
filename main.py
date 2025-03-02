import rtoyt    # HYPOTHETICAL module
import datetime
import yt_uploader   # HYPOTHETICAL module
import logging

WEEKLY_UPLOAD_SUBREDDITS = [
    "sub1",
    "sub2",
    "sub3",
    "sub4",
    "sub5",
    "sub6",
    "sub7"
]

if __name__=="__main__":
    rtoyt.make_preliminary_folders()

    weekday_index = (datetime.datetime.today().weekday()+1)%7   # starting from sunday
    today_subreddit = WEEKLY_UPLOAD_SUBREDDITS[weekday_index]

    rtoyt.download_from_subreddit(today_subreddit)

    # any preconditional setup for yt_uploader module

    # goes into shorts/ directory, and uploads all the clips there
    # 1-2 videos per Youtube Short
    yt_uploader.upload_short("shorts/")    

    # goes into long/ directory, and directly uploads the video there (already made)
    yt_uploader.upload_long_form("long/")

    # optional logging
    logger = logging.getLogger(__name__) 
    logging.basicConfig(
        filename="runner.log",
            encoding="utf-8",
            level=logging.DEBUG,
            format='%(asctime)s %(levelname)s: %(message)s',
            datefmt='%m/%d/%Y %I:%M:%S %p'
    )
    logger.info("Uploading all videos")

    # cleans download and temp directory
    rtoyt.cleanup_files()

    # procedure to clear shorts/* and long/* (TO IMPLEMENT)
    cleanup_videos()
