import pandas as pd
import os


def remove_symbols(import_list):
    symbol = ["!","@","#","$","%","^","&","*","(",")","=","+","{","}",":",";","'","/"]
    
    clean_list=[]

    for c in import_list:
        clean_text = ''.join(sc for sc in c if sc not in symbol)
        clean_list.append(clean_text)
    return clean_list

def get_list(folder_path, file_type=None, f=False, prt=False):
    import os
    choice = f
    file_list = {}
    need_to_print = prt
    i = 0
    
    for root, directories, files in os.walk(folder_path):
        for file in files:
            if choice:
                if file.endswith(file_type):
                    file_list[i] = os.path.join(root, file)
                    i+=1
            else:      
                file_list[i] = os.path.join(root, file) # Include all files if file_type is not specified
                i +=1
    if prt:  
        print("Keys and Links in Dic")
        for i, l in file_list.items():
            print(i, l)

    return file_list


def clean_df (df, clm):
  df = df.dropna(subset=clm, how='all', inplace=True)
  



def rearrange_df(df):
    
    
    # print columns with its index before selections
    def printd():
        pd_list=[]
        for key, values in dic.items():
            pd_list.append([key, values])
        
        df_select_columns = pd.DataFrame(pd_list, columns=['Index', 'Name'])

        print(df_select_columns )

    clm_list = df.columns.str.strip()
    dic = {}

    for i in range(len(clm_list)):
        dic[i] = clm_list[i]

    printd()

    selected_columns = list(map(int, input("please select column index to form a new df : ").split()))
    clms = [None] * len(selected_columns)

    for key, values in dic.items():
        if key in selected_columns:
            clms[selected_columns.index(key)] = values
    
    df = df[clms]
    file_name = input("Please name the file : ")
    file = rf'C:\Users\nickf\OneDrive\桌面\Python\python working station\temp excel generated by rearrange_df\{file_name}.csv'
    df.to_csv(file, index=False)

    print(f"Temporary CSV file : {file}")
    
    return df[clms]

def get_html_table(df):
    
  html_file = r'C:\Users\nickf\OneDrive\桌面\Python\HTML\table.html'
  html = df.to_html()
  html =html.replace('&lt;','<').replace('&gt;', '>')

  # Specify the path for the HTML file


  # Write the complete HTML content to the file
  # Write the complete HTML content to the file
  with open(html_file, "w", encoding="utf-8") as text_file:
      # Add HTML structure and CSS styling
      complete_html = f"""
      <!DOCTYPE html>
      <html>
      <head>
          <style> 
              /* Define the keyframes for the flame animation */
              @keyframes flameAnimation {{
                  0%  {{ background-color: #2F4F4F; }}
                  25% {{ background-color: black; }}
                  50% {{ background-color: #2F4F4F; }}
                  75% {{ background-color: black; }}
                  100% {{ background-color: #2F4F4F; }}
              }}

              /* Set the content of table using css properties */ 
              table {{ 
                  width: 100%; 
                  margin: auto; 
                  text-align: center; 
              }} 

              
              
              /* Styles for scrollable table container */
              .table-container {{ 
                  width: 100%;
                  overflow-x: auto;
              
              }} 
              /* Applying css properties to table components */ 
              table, td, th, tr {{ 
                  padding: 12px; 
                  color: white; 
                  background: black; 
                  border: 1px solid white; 
                  border-collapse: collapse; 
                  font-size: 20px; 
                  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif; 
              }} 

              /* Apply css properties to th with flame animation */
              th {{ 
                  text-align: center;
                  color: white; 
                  border: 1px solid white; 
                  border-collapse: collapse; 
                  background: #4CAF50; 
                  /* Add the flame animation */
                  animation: flameAnimation 6s linear infinite;
              }} 

              /* Apply hover effect to td */ 
              td:hover {{ 
                  background: orange; 
              }} 

              /* Apply the flame animation to the first column */
              td:first-child {{ 
                  animation: flameAnimation 2s linear infinite;
              }}

              /* Adjust the width and height of the index column */
              .index_col {{
                  width: auto;
                  height: auto;
              }}
          </style> 
      </head>
      <body>
          {html}
      </body>
      </html>

      """
      text_file.write(complete_html)

if __name__ == "__main__":
    
    folder = r'C:\Users\nickf\OneDrive\桌面\Python\python working station'
    flist = get_list(folder, '.xlsx')


    df = pd.read_excel(flist[0])


    table = get_html_table(df)

    
