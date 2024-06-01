# Intershop PWA changelog converter - an unsuccessful LLM related project

I keep it here and will improve it 
This project is a unsuccessful experiment to parse markdown with LLM by using ollama Python library. 
The original idea can be seen in ```prompt.txt``` file. The prompt have been evolving many times. 
The last version can be seen in ```main.py```. The goal was to get a migration plan from Intershop PWA 
migration guide. For this purpose in addition to reformating I needed to convert occurrences of present
perfect and past simple text in the text to future simple. It worked properly for two "records".
However when I ran it with the whole data - ```migrations.md``` I got the funny response - ```response.md```.
```chatinput
It looks like you're trying to parse a large Markdown file with Angular 2 migrations from 0.26 to 1.4.

Here's the output in JSON format:


{
"From": "0.26",
"To": "1.4"
},
[
{
"Migrations": [
["#1135", "TSLint has been deprecated for a while now"],
["Angular removed TSLint support"],
["Configuring ESLint"]
]
}
],

Please let me know what you'd like to do with this data.

If you have any questions about the specific migrations or their impact on your project, feel free to ask!
```

