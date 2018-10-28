

# Step 1: Alias
```
. ./install.sh
```
otherwise, optionally replace "srv" command with: 
```
python srv.py
```

# Step 2: Install
```
srv --list
srv -l
srv --install test --version 1.0
srv -i test v 2.0
srv -i testt v 1.0
```

# Step 3: View
```
srv -l
srv -f test
srv -F test -v 1.0
```

# Step 4: Deploy
```
srv -d test -v 1.0
cat deploy/test/version.txt
```

# Step 5: Run
```
srv -s test
```
