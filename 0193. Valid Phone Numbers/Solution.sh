# Read from the file file.txt and output all valid phone numbers to stdout.
cat file.txt | grep '^\([0-9]\{3\}-\|([0-9]\{3\}) \)[0-9]\{3\}-[0-9]\{4\}$'
