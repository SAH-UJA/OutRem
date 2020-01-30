### Installation
The module, Dupamb requires pandas module to function
This module is used to remove the tuples having duplicate and ambiguous tuples in a dataset. The first column of the csv file should be that of the target class or feature while the others be independent features affecting target feature.
```sh
$ pip install Dupamb
$ python
>> import Dupamb
>> da_obj = Dupamb.Dupamb('data.csv') # input file is data.csv 
>> da_obj.removeDupAmb(outfilename='out.csv') # default outfile name is 'out.csv'
```
### License
MIT
### Author
Sahil Ahuja
