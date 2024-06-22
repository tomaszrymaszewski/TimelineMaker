# Timeline from JSON input
#### This python projects allows you to create a timeline using the Qt python library (to display the timeline) and a JSON file you can make yourself or use sth like ChatGPT to convert from a piece of text. 

## Installation
To run this project, in the terminal run ```pip install -r requirements.txt``` to install all libraries.

Additionally, go to the ollama website and download their app. Then in your main terminal run the command ```ollama run llama3``` (or the model you like the most from [their library](https://ollama.com/library)). You should be done with the installation then.

## Usage
### First prepare the input:
take a text you would like to turn into a timeline and paste it into an AI like ChatGPT (or any other good one). Afterward paste this:
```
from this text, create a json file in the format 
[{
    "date": 'year of the event',
    "description": 'what happened during the event'
}]
only use full years (not full dates), double quotes (even for the year), if you encounter a date like 1880s - make it 1885, put the entire list into one line
```
#### Example:
Input:
```
Napoleon Bonaparte: A Forceful Figure (1769-1821)
Napoleon Bonaparte (1769-1821) was a French military leader and emperor who dominated European affairs in the early 19th century. Born into a minor noble family in Corsica in 1769, he rose through the ranks of the French army during the French Revolution (1789-1799). His exceptional military skills and strategic brilliance were on display in his victories against Austria and Italy (1796-1797).
By 1799, through a coup d'état known as the 18th Brumaire, Napoleon became the First Consul of France, effectively the country's leader. He instituted a series of reforms that stabilized the nation after the tumultuous years of the revolution.These reforms, known as the Napoleonic Code, established a legal system that continues to influence legal codes around the world today.
Napoleon's ambition for power and expansion led him to declare himself Emperor of France in 1804. He embarked on a series of wars across Europe, conquering vast territories and establishing French dominance over much of the continent.His military victories at Austerlitz (1805) and Jena-Auerstedt (1806) cemented his reputation as a tactical genius.
However, Napoleon's ambitions ultimately led to his downfall. His invasion of Russia in 1812 proved disastrous, with the harsh Russian winter and fierce resistance inflicting heavy losses on his army. This marked a turning point in his fortunes.Defeated at the Battle of Leipzig in 1813 by a coalition of European powers, Napoleon was forced to abdicate the throne in 1814 and exiled to the island of Elba.
A dramatic escape from Elba in 1815 led to what is known as the "Hundred Days," a period where Napoleon briefly regained power in France. However, his final defeat came at the Battle of Waterloo in 1815, definitively ending his reign.He was exiled again, this time to the remote island of Saint Helena, where he died in 1821.
Napoleon's legacy remains complex and controversial. He is admired for his military genius, his legal reforms, and his modernization of France. However, he is also criticized for his authoritarian rule, his wars that devastated Europe, and his attempts to establish a vast French empire. Despite the controversy, Napoleon Bonaparte remains one of the most significant figures in European history.

from this text, create a json file in the format 
[{
    "date": 'year of the event',
    "description": 'what happened during the event'
}]
only use full years (not full dates), double quotes (even for the year), if you encounter a date like 1880s - make it 1885, put the entire list into one line
```
Result:
```
[{"date":"1769","description":"Born into a minor noble family in Corsica"},{"date":"1789","description":"French Revolution began"},{"date":"1799","description":"Became First Consul of France through a coup d'état"},{"date":"1804","description":"Declared himself Emperor of France"},{"date":"1805","description":"Victory at Austerlitz"},{"date":"1806","description":"Victory at Jena-Auerstedt"},{"date":"1812","description":"Invasion of Russia"},{"date":"1813","description":"Defeated at the Battle of Leipzig"},{"date":"1814","description":"Abdicated the throne and exiled to Elba"},{"date":"1815","description":"Escaped from Elba and regained power for the Hundred Days"},{"date":"1815","description":"Defeated at the Battle of Waterloo and exiled to Saint Helena"},{"date":"1821","description":"Died in Saint Helena"}]
```

### Use the result:
Copy the JSON you got from the AI and paste it into the terminal of the `main.py` file (after it has been run).

You should get something like this in the terminal and a timeline of course.
```
THE JSON IS: [{'date': '1769', 'description': 'Born into a minor noble family in Corsica'}, {'date': '1789', 'description': 'French Revolution began'}, {'date': '1799', 'description': "Became First Consul of France through a coup d'état"}, {'date': '1804', 'description': 'Declared himself Emperor of France'}, {'date': '1805', 'description': 'Victory at Austerlitz'}, {'date': '1806', 'description': 'Victory at Jena-Auerstedt'}, {'date': '1812', 'description': 'Invasion of Russia'}, {'date': '1813', 'description': 'Defeated at the Battle of Leipzig'}, {'date': '1814', 'description': 'Abdicated the throne and exiled to Elba'}, {'date': '1815', 'description': 'Escaped from Elba and regained power for the Hundred Days'}, {'date': '1815', 'description': 'Defeated at the Battle of Waterloo and exiled to Saint Helena'}, {'date': '1821', 'description': 'Died in Saint Helena'}]
1. Born into a minor noble family in Corsica (in 1769)
2. French Revolution began (in 1789)
3. Became First Consul of France through a coup d'état (in 1799)
4. Declared himself Emperor of France (in 1804)
5. Victory at Austerlitz (in 1805)
6. Victory at Jena-Auerstedt (in 1806)
7. Invasion of Russia (in 1812)
8. Defeated at the Battle of Leipzig (in 1813)
9. Abdicated the throne and exiled to Elba (in 1814)
10. Escaped from Elba and regained power for the Hundred Days (in 1815)
11. Defeated at the Battle of Waterloo and exiled to Saint Helena (in 1815)
12. Died in Saint Helena (in 1821)
```

## License
The project is under Apache License meaning that you need to credit me when using this. 
