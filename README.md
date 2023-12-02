# Kemono-youtube-fetch
Fetches Youtube Links from Kemono posts, if no link write the post title and any attachments. Fetches 50 posts per fetch and writes them into a text file with Incremental (+50) filename.

## API Description

Uses Kemono API to get the data from the server.
The server allows max=50 posts fetch per request.

## Parameters in the Code

SERVICE_URL = `{patreon,fanbox,fantia,gumroad,subscribestar}`
CREATOR_ID = `String or Integer`

More service url can be used which aren't mentioned here but require a bit of changes in the function `def fetch_post()`



