This script will send an `HTTP request` to the device at the specified `IP address` and parse the response headers to determine the operating system and software versions. It will also scan a range of common ports to identify which ones are open.
To use this script, the user must enter an IP address in the terminal. The script will then display the gathered information about the device. You can modify the script to accept additional input from the user, such as the specific ports they want to scan or the types of information they want to gather.

#use this comnand to run the script:

 ```
 python3 deviceR3con.py
```

 #if you get  a `reportMissingModuleSource` warning , please install pip3 on your system with following command:

 ```
 curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```

 #after you use this command:

 ```
python3 or python get-pip.py
 ```


 #check the version with one of the following commands:

``` 
pip --version
```
```
pip3 --version
```


feel free to contribute or correct me if i made a mistake.
  Thank you
