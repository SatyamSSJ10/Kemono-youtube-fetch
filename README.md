# Kemono-youtube-fetch (Python 3.8+ Strict)
Fetches YouTube links from Kemono posts, if there is no link write the post title and any attachments. Fetches 50 posts per fetch and writes them into a text file with an Incremental (+50) filename.
It uses a new assignment expression from 3.8.+ which aren't available on previous versions.
## API Description

It uses Kemono API to get the data from the server.
The server allows max=50 posts fetch per request.

## Parameters in the Code

SERVICE_URL = `{patreon,fanbox,fantia,gumroad,subscribestar}`
CREATOR_ID = `String or Integer`

More service URL can be used which aren't mentioned here but require a bit of change in the function `def fetch_post()`

## Fetched Link Results

The Link fetched will be saved as a List [title, attachment(Images), Youtube Link]
if there are no YouTube links just [title, attachment(Images)]

This script saves them in a text file with {OFFSET}.txt as filename.



