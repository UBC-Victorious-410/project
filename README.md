#UBC Victorious Secret

Project for CS410.

### 
To run analyzer navigate to project directory and run 
`python main.py <options>'
option: getRepo <git repo address> - perform 'git pull' with given repoURL at ./target
	GenerateJSON               - parse gitlog, execute PMD and generate JSON 
	GenerateGraph              - start web server and generate graph

Ensure that you have the following python plugin/modules installed.
	-gitpython 0.3.1 
	-flask 
