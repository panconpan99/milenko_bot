from urllib.request import urlopen
from urllib.error import HTTPError
from re import search as search_re


def youtube_request(search): 
    """Parse and treats the results of a given search 

    Parameters
    ----------
    search: string
        parameter used to perform the search through YouTube

    Returns
    -------
    str
        return the 'watch?v=' link segment
        
    """
    
    # Youtube search
    search = str(search).replace(" ", "+").lower()
    search = "https://www.youtube.com/results?search_query=%s" % search
    
    # Youtube request
    try:
        session = urlopen(search)
        page_html = session.read()
        session.close()
    except HTTPError:
        return "No page was found"
    
    # Video selection
    video = search_re('watch\?v=\w*', str(page_html))
    if video:
        return 'https://www.youtube.com/' + video.group(0)
    return 'No video was found'
