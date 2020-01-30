### Installation
The module, OR requires pandas module to function
This module is used to remove the tuples having outliers in the datset and generate outlier-free dataset.
```sh
$ pip install OutRem
$ python
>> import OutRem
>> or_obj = OutRem.OutRem('data.csv') # input file is data.csv with all numberical data
>> or_obj.generateOutputFile(outfilename='out.csv') # default outfile name is 'out.csv'
```
### License
MIT
### Author
Sahil Ahuja
