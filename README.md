## Texttools

Python 2.7 package for various text normalization functions. Currently contains transliteration functionality for special symbols from most common European languages to Latin symbils. 
You can extend the symbol dictionary with more symbols as needed.

## Usage 

Use pip to install this package:

```
pip install git+https://github.com/IevaZarina/texttools.git
``` 

Import the ```textools``` package into your project: 

```
from texttools.normalize import transliterate


unicode_string = u'Šaursliežu dzelzceļš, Chemin de fer à voie étroite, Узкоколейная железная дорога'

transliterate(unicode_string)
# Saursliezu dzelzcels, Chemin de fer a voie etroite, Uzkokolejnaja zheleznaja doroga
```