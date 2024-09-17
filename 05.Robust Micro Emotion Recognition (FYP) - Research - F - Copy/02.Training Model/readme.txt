*First Run preprocessing.py using fer.csv
--it will create the files   flabels.npy and fdataX.npy

*Then Run the train.py using above generated files
--this will generate files  modXtest.npy, modytest,npy, fer.json and fer.h5

*Then Run the Test data using test.py

Can take accuracy of trained classifier using modXtest.npy 
and modytest.npy by running fertest.py file. 

This would give you the accuracy in % of the recently trained classifier. 


****Author- Janith Prabhanuka- 2020/12/07 7.16 pm