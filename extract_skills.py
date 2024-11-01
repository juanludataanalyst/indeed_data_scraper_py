
import json
import re
import os

# Obtener el directorio de trabajo actual
current_directory = os.getcwd()  # Esto obtiene el directorio actual

# Especificar el nombre del archivo JSON
file_name = 'US_data_analyst_0.json'

# Combinar el directorio actual con el nombre del archivo
file_path = os.path.join(current_directory, file_name)

# Cargar el archivo JSON
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        print(data)  # Imprimir el contenido del archivo JSON

except FileNotFoundError:
    print(f"Error: El archivo {file_path} no se encontró.")
except json.JSONDecodeError as e:
    print(f"Error al leer el archivo JSON: {e}")



# Diccionario con tecnologías y sus variaciones
skills = {
    'sql': [
        'SQL', 'Sql', 'sQl', 'sqL', 'Structured Query Language', 'Structured query language', 
        'structured query language'
    ],
    'python': [
        'Python', 'PYTHON', 'Py', 'py', 'Python3', 'python 3', 'Python 3.x'
    ],
    'r': [
        'R', 'r', 'R Programming', 'r programming'
    ],
    'c': [
        'C', 'c', 'C Language', 'c language'
    ],
    'c#': [
        'C#', 'c#', 'C Sharp', 'c sharp'
    ],
    'javascript': [
        'JavaScript', 'javascript', 'Java script', 'javaScript', 'JS', 'js', 
        'ECMAScript', 'ecmascript'
    ],
    'js': [
        'JS', 'js', 'JavaScript'
    ],
    'java': [
        'Java', 'java', 'Java SE', 'java se'
    ],
    'scala': [
        'Scala', 'scala'
    ],
    'sas': [
        'SAS', 'sas', 'Statistical Analysis System', 'statistical analysis system'
    ],
    'matlab': [
        'MATLAB', 'matlab', 'MATLAB Language', 'matlab language'
    ],
    'c++': [
        'C++', 'c++', 'C Plus Plus', 'c plus plus'
    ],
    'c/c++': [
        'C/C++', 'C / C++', 'C and C++', 'c/c++', 'c and c++'
    ],
    'perl': [
        'Perl', 'perl'
    ],
    'typescript': [
        'TypeScript', 'typescript', 'TS', 'ts'
    ],
    'bash': [
        'Bash', 'bash', 'Bourne Again Shell', 'bourne again shell'
    ],
    'html': [
        'HTML', 'html', 'Hypertext Markup Language', 'hypertext markup language'
    ],
    'css': [
        'CSS', 'css', 'Cascading Style Sheets', 'cascading style sheets'
    ],
    'php': [
        'PHP', 'php', 'Hypertext Preprocessor', 'hypertext preprocessor'
    ],
    'powershell': [
        'PowerShell', 'powershell', 'Windows PowerShell', 'windows powershell'
    ],
    'rust': [
        'Rust', 'rust'
    ],
    'kotlin': [
        'Kotlin', 'kotlin'
    ],
    'ruby': [
        'Ruby', 'ruby'
    ],
    'dart': [
        'Dart', 'dart'
    ],
    'assembly': [
        'Assembly', 'assembly', 'Assembly Language', 'assembly language'
    ],
    'swift': [
        'Swift', 'swift'
    ],
    'vba': [
        'VBA', 'vba', 'Visual Basic for Applications', 'visual basic for applications'
    ],
    'lua': [
        'Lua', 'lua'
    ],
    'groovy': [
        'Groovy', 'groovy'
    ],
    'delphi': [
        'Delphi', 'delphi'
    ],
    'objective-c': [
        'Objective-C', 'objective-c', 'Objective C', 'objective c'
    ],
    'haskell': [
        'Haskell', 'haskell'
    ],
    'elixir': [
        'Elixir', 'elixir'
    ],
    'julia': [
        'Julia', 'julia'
    ],
    'clojure': [
        'Clojure', 'clojure'
    ],
    'solidity': [
        'Solidity', 'solidity'
    ],
    'lisp': [
        'Lisp', 'lisp'
    ],
    'f#': [
        'F#', 'f#', 'F Sharp', 'f sharp'
    ],
    'fortran': [
        'Fortran', 'fortran'
    ],
    'erlang': [
        'Erlang', 'erlang'
    ],
    'apl': [
        'APL', 'apl'
    ],
    'cobol': [
        'COBOL', 'cobol'
    ],
    'ocaml': [
        'OCaml', 'ocaml'
    ],
    'crystal': [
        'Crystal', 'crystal'
    ],
    'javascript/typescript': [
        'JavaScript / TypeScript', 'javascript / typescript', 'JS / TS', 
        'js / ts', 'JavaScript and TypeScript', 'javascript and typescript'
    ],
    'golang': [
        'Golang', 'golang', 'Go', 'go'
    ],
    'nosql': [
        'NoSQL', 'nosql', 'No-SQL', 'no-sql'
    ],
    'mongodb': [
        'MongoDB', 'mongodb'
    ],
    't-sql': [
        'Transact-SQL', 'T-SQL', 't-sql'
    ],
    'visual_basic': [
        'Visual Basic', 'visual basic', 'VB', 'vb'
    ],
    'pascal': [
        'Pascal', 'pascal'
    ],
    'mongo': [
        'Mongo', 'mongo', 'MongoDB'
    ],
    'pl/sql': [
        'PL/SQL', 'pl/sql'
    ],
    'sass': [
        'Sass', 'sass'
    ],
    'vb.net': [
        'VB.NET', 'vb.net', 'Visual Basic .NET', 'visual basic .net'
    ],
    'mssql': [
        'MSSQL', 'mssql', 'Microsoft SQL Server', 'microsoft sql server'
    ],
    'airflow': [
        'Airflow', 'airflow'
    ],
    'alteryx': [
        'Alteryx', 'alteryx'
    ],
    'asp.net': [
        'ASP.NET', 'asp.net'
    ],
    'atlassian': [
        'Atlassian', 'atlassian'
    ],
    'excel': [
        'Excel', 'excel', 'Microsoft Excel', 'microsoft excel'
    ],
    'power_bi': [
        'Power BI', 'power bi'
    ],
    'tableau': [
        'Tableau', 'tableau'
    ],
    'srss': [
        'SRSS', 'srss', 'SQL Server Reporting Services', 'sql server reporting services'
    ],
    'word': [
        'Word', 'word', 'Microsoft Word', 'microsoft word'
    ],
    'unix': [
        'Unix', 'unix'
    ],
    'vue': [
        'Vue', 'vue', 'Vue.js', 'vue.js'
    ],
    'jquery': [
        'jQuery', 'jquery'
    ],
    'linux/unix': [
        'Linux / Unix', 'linux / unix', 'Linux and Unix', 'linux and unix'
    ],
    'seaborn': [
        'Seaborn', 'seaborn'
    ],
    'microstrategy': [
        'MicroStrategy', 'microstrategy'
    ],
    'spss': [
        'SPSS', 'spss'
    ],
    'visio': [
        'Visio', 'visio'
    ],
    'gdpr': [
        'GDPR', 'gdpr', 'General Data Protection Regulation', 'general data protection regulation'
    ],
    'ssrs': [
        'SSRS', 'ssrs', 'SQL Server Reporting Services', 'sql server reporting services'
    ],
    'spreadsheet': [
        'Spreadsheet', 'spreadsheet'
    ],
    'aws': [
        'AWS', 'aws', 'Amazon Web Services', 'amazon web services'
    ],
    'hadoop': [
        'Hadoop', 'hadoop'
    ],
    'ssis': [
        'SSIS', 'ssis', 'SQL Server Integration Services', 'sql server integration services'
    ],
    'linux': [
        'Linux', 'linux'
    ],
    'sap': [
        'SAP', 'sap', 'Systems Applications and Products', 'systems applications and products'
    ],
    'powerpoint': [
        'PowerPoint', 'powerpoint'
    ],
    'sharepoint': [
        'SharePoint', 'sharepoint'
    ],
    'redshift': [
        'Redshift', 'redshift', 'Amazon Redshift', 'amazon redshift'
    ],
    'snowflake': [
        'Snowflake', 'snowflake'
    ],
    'qlik': [
        'Qlik', 'qlik'
    ],
    'cognos': [
        'Cognos', 'cognos'
    ],
    'pandas': [
        'Pandas', 'pandas'
    ],
    'spark': [
        'Spark', 'spark'
    ],
    'outlook': [
        'Outlook', 'outlook', 'Microsoft Outlook', 'microsoft outlook'
    ],
}
# Compilar expresiones regulares para cada tecnología
patterns = {key: re.compile(r'\b(' + '|'.join(map(re.escape, variations)) + r')\b', re.IGNORECASE) 
            for key, variations in skills.items()}

# Extraer tecnologías
def extract_technologies(description):
    found_technologies = set()  # Usar un conjunto para evitar duplicados
    for key, pattern in patterns.items():
        if pattern.search(description):
            found_technologies.add(key)  # Agregar solo la clave (tecnología)
    return list(found_technologies)  # Convertir el conjunto de vuelta a una lista

# Procesar cada puesto en el JSON
for job in data:
    description = job.get("description", "")
    technologies = extract_technologies(description)
    print(f"Tecnologías para '{job['title']}': {technologies}")