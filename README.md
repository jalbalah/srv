

# Step 0: Clone & Alias
```
git clone https://github.com/jsa41394/srv.git
cd srv
. ./install.sh
```
otherwise, optionally replace "srv" command with: 
```
python srv.py
```

# Step 1: Develop
- Write some code that is called from main.py
- Include all files in the local directory or subdirectories
- Srv will copy all files into the deploy folder and will run from there

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
