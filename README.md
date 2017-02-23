- Instructions: 
    - Ensure input.json is present in local directory
    - Decrypt the binary, run it as per usage below
    
- Useage: ./json.parser.py

- TODO 
   - batch up metrics rather then acrew over head from re-establishing sessions
   - still trying to locate how to pass timestamp as event epoch in API docs
   - remove sort dict function, opt for streaming yield / split into two funtions. This sort is i/o bottleneck
   - loading into mem bad for oom, again stream / yield
   - remove overlooked standard out debug as will slow egress considerably due to tty response times log.info eg.
   - manage missing keys/values more gracefully / more error checking.
   
