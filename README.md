# Es wird keine Haftung vom Autor übernommen.
# Author is not to be held liable.
## This script was written and tested on windows, with the chrome debugging version and only for lectures on the typewriter.at website.
0. Install AutoTyper by MurGee. Create an entry, which writes from the clipboard, when you press a shortcut. The shortcut needs to be F6, otherwise you'll have to edit the script to change it. Keep AutoTyper by MurGee open.
1. Install Chrome.
2. Win + r -> "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\chrome-debug"
3. Open Typewriter and go to a lecture. Click on start, so the pop-up goes away.
4. Win + r -> Locate script and run it using "python path/to/typewriter.py
5. Go to the lecture in chrome -> F12 -> Use the cursor selection tool to find the two IDs of the text -> Paste them in the order of 1 and then 2 into the script when prompted to.
6. Run script and instantly click on the lecture in chrome, so that chrome is focused.

Author is  Pileshkasupa. Written with help of AI.