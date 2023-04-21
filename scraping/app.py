from atwiki.dataLibrary import scrape_chips
import json

chips = scrape_chips(5)
json_chips = json.dumps(chips, ensure_ascii=False)
file = open('/tmp/data/exe5-chips.json', 'w')
file.write(json_chips)
