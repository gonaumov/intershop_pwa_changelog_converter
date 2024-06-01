import re

prompt = re.sub(r"\s+", " ", f"""
For each occurrence of the pattern ## From [from version number] to [to version number], extract the content - 
including all new lines and special characters until the next ## marker and keep it as [entire content].
Replace all occurrences of past simple or present perfect tense in [entire content], with future simple tense, 
and keep the whole result as [resulted content].
In [resulted content] find mentioning of Angular version. If there is no
Angular version take the one from previous row. If there is no previous row
take version 11 and remember it as [angular version].
In [resulted content] find mentioning of NodeJS version. If there is no
NodeJS version take the one from previous row. If there is no previous row
take version 14.15.0 LTS and remember it as [nodejs version].
In [resulted content] find mentioning of NPM version. If there is no
NPM version take the one from previous row. If there is no previous row
take version 6.14.8 and remember it as [npm version].
Finally output a well formatted markdown table with columns From PWA version - [from version number], 
To PWA version - [to version  number], 
Angular version - [angular version], 
NodeJS version - [nodejs version], 
NPM version - [npm version], 
Things we need to do - [resulted content]  - the whole text don't summarize it, 
Estimate - 1 this is a hardcoded value, 
Regression - two days - this is a hardcoded value.
Please sort the entire output table based on the values in the From PWA version column.
Response only with the result table, please.
Here is the input data:
""".strip())

print(prompt)
