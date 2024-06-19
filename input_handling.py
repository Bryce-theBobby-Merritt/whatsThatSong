def get_playlist_id_from_link(user_input_playlist_link: str) -> str:
    """
    TODO implement input handling that checks:
        - that is is a spotify link
        - that it has a .com and a https://open.spotify.com/playlist/
        - MORE


        https://open.spotify.com/playlist/312Cr7cPq6bXu4b40ZB2DU?si=f8cd0d4bb5744d0c
    """
    #first make sure it contains the right elements
    if not user_input_playlist_link.strip().startswith("https://open.spotify.com/playlist/") or not ("?" in user_input_playlist_link):
        return "INVALID"
    
    user_input_playlist_link = user_input_playlist_link.strip()
    
    prefix_idx = user_input_playlist_link.find("/playlist/")
    question_mark_idx = user_input_playlist_link.find("?")

    #now if it has the right elements, parse
    return (user_input_playlist_link[prefix_idx+10:question_mark_idx])

