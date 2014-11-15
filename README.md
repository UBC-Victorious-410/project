#UBC Victorious Secret

Project for CS410.

### 
To run analyzer navigate to project directory and run 
`python main.py <options>'
option: getRepo <git repo address> - perform 'git pull' with given repoURL at ./target
	gitLog                     - generate gitLog.xml in PMDResult
    	PMD                        - analyze target/ with PMD. place xml results in PMDResults
	Parse                      - execute parsers to parse result within PMDResults
	GenerateJSON               - generate JSON from the fuser 
	GenerateGraph              - start web server and generate graph

Ensure that you have the following python plugin/modules installed.
	-gitpython 0.3.1 
	-flask 
