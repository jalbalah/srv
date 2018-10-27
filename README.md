

####Step 1: Alias
```
. ./install.sh
```
otherwise, optionally replace "srv" command with: 
```
python srv.py
```

###Step 2: Create 
```
srv --list
srv --install my_service --version 1.0
srv -i my_svc -v 2
srv --l
```

###Step 3: Start
```
srv --start my_service
```