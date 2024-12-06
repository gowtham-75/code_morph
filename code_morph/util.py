import os
import magika
from pathlib import Path

m = magika.Magika()
import zipfile
code_dir_name = "./code"
sql_dir_name = "./sql_files"

def extract_code(repo_dir):
    code_index=[]
    file_list = []
    code_text=""
    for root, _, files in os.walk(repo_dir):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, repo_dir)
            code_index.append(relative_path)
            file_type = m.identify_path(Path(file_path))

            if file_type.output.group in ["text", "code"]:
                try:
                    with open(file_path, "r") as f:
                        code_text += f"__________{relative_path}__________\n"
                        code_text += f.read()
                        code_text += "\n\n"
                        file_list.append(code_text)
                except Exception:
                    pass
    return code_index, code_text, file_list

def get_code_prompt(question, code_index, code_text):

    """ generate a prompt for code related questions """

    prompt = f"""
    Question : {question}
    
    Context:
    
    - Entire codebase is provided below.
    - Here is an index of the files in the codebase: {code_index}
    - Each file is concatenated togather and provided below. {code_text}
    
    Answer:

    """

    return prompt


def safe_write(path, code):
    path = "./software/" + path
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w+',encoding = "utf-8") as f:
        f.write(code)



def extract_sql_files(zip_path,code_dir_name = "./code",sql_dir_name = "./sql_files"):
    # Create the SQL files directory if it doesn't exist
    os.makedirs(sql_dir_name, exist_ok=True)  
    sql_files_content = {}    
    code_text=""
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for file_name in zip_ref.namelist():
            # st.write(zip_ref.namelist())
            if file_name.endswith('.sql'):
                # Extract each SQL file to the specified directory
                zip_ref.extract(file_name, sql_dir_name)                
                # Read the content of the file to store it (optional)
                with zip_ref.open(file_name) as file:
                    sql_files_content[file_name] = file.read().decode('utf-8')
                
                with zip_ref.open(file_name) as file:
                    # st.write(file_name)
                    code_text += f"__________{file.name}__________\n"
                    code_text += file.read().decode('utf-8')
                    code_text += "\n\n"    
    return sql_files_content,code_text
# test
# repo_dir = "./code"
# code_index, code_text, file_content = extract_code(repo_dir)
# for file in file_content:
#     print(file)