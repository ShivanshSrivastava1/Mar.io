# Mar.io
Mar.io is a Discord bot written in Python. Its features include streamlined server moderation, music playback, and simple Wikipedia searches.

## Install
Invite Mar.io to your server using this [link](https://discord.com/oauth2/authorize?client_id=738092825463226368&permissions=8&scope=bot).

## Commands
**Note: Leave out the square brackets when running a command**

**.join** - Joins the voice channel the command user is currently in

**.leave** - Leaves the voice channel the command user is currently in

**.kick [user mention]** **[optional reason]** - Kicks the target user from the server if the command user has Admin privileges. The command user can also provide an optional kick reason, which will be saved to the server audit log

**.ban [user mention]** **[optional reason]** - Bans the target user from the server if the command user has Admin privileges. The command user can also provide an optional ban reason, which will be saved to the server audit log

**.unban [user mention]** - Unbans the target user from the server if the command user has Admin privileges

**.pl [YouTube URL]** - Plays the audio from the YouTube video provided in the current voice channel. Can only be used after the bot has joined a voice channel using .join

**.ping** - Returns the command user’s current ping

**.clear [optional number]** - Clears a certain number of most recent messages in the current text channel. The default number is 5, but it can be changed

**.8ball [question]** - Answers the command user’s question like the Magic 8 Ball would

**.wiki [search term]** - Searches Wikipedia for the given term and returns a summary from the most relevant article

 ## License
[MIT License](https://choosealicense.com/licenses/mit/)
