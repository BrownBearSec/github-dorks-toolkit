# My github dorking toolkit

This is my WIP toolkit for github dorks and related tools.


## Notes:

View csv files in the terminal as a table with:
`column -s, -t < somefile.csv | less -#2 -N -S`

### allMerger.py 

add new dorks files found to the first file specified. (removes speechmarks and duplicates.)

`python allMerger.py all.txt new.txt`

### all.txt

Just everything I can find.

### rce.txt

dorks relating to rce.

### tokens.txt

Any kind of authorisation token used to dork.

### high.txt

an arbitrary list of dorks that I think could be of high impact. These will appear rarely, and when they do it will more likely be a false positve.

### gitsubdomain.txt

There are other github pages that arent the offical one. If you brute force a domain to find git subdomains, you can find more attack surface.

### seen.txt

This is a file of dorks ive found/made because I have seen these issue on bug bounty reports

### PII.txt

Personally identifiable information dorks