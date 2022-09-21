import pandas as pd
def add_tag_to_page(page_id):
    file = "/home/saribeg/Downloads/pages_1400_091.xlsx"
    sheet = pd.read_excel(file)
    xl = pd.DataFrame(sheet)
    pg = page_id
    v = xl.loc[xl['page_id'] == pg].iloc[0][3:].dropna()
    return set(v)


a = add_tag_to_page('parcinema')
print(a)




