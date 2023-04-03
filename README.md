# Daily-Quote
This project utilizes my collection of Quotes and personal notes from my Obsidian.MD Vault to automate an email to my inbox (and any other contacts) at 7am each morning.

The project is written in Python and hosted on my Raspberry Pi using Cronjob for scheduling. Originally I was using local files on the Raspberry Pi to get the note for each day but now it uses the Github API and my credentials to access a private Github Repo where my Obsidian vault is frequently updated.
