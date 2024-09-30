import pandas as pd
import re

# 读取文件内容
with open('sequence.gb', 'r') as file:
    content = file.read()

# 使用正则表达式匹配基因信息，包括 gene、misc_feature 和 CDS 标签
pattern = re.compile(
    r'gene\s+(complement\(\d+\.\.\d+\)|\d+\.\.\d+)\n\s+/gene="(OPG\d+)"\n(?:\s+misc_feature\s+(complement\(\d+\.\.\d+\)|\d+\.\.\d+)\n\s+/gene="(OPG\d+)"\n\s+/note="(.*?)"\n)?(?:\s+CDS\s+(complement\(\d+\.\.\d+\)|\d+\.\.\d+)\n\s+/gene="(OPG\d+)"\n\s+/codon_start=\d+\n\s+/product="(.*?)"\n\s+/protein_id="(.*?)"\n)?',
    re.DOTALL
)
matches = pattern.findall(content)

# 创建 DataFrame
data = []
for match in matches:
    gene_location = match[0]
    gene_name = match[1]
    misc_location = match[2] if match[2] else None
    misc_gene_name = match[3] if match[3] else None
    misc_note = match[4] if match[4] else None
    cds_location = match[5] if match[5] else None
    cds_gene_name = match[6] if match[6] else None
    product = match[7] if match[7] else None
    protein_id = match[8] if match[8] else None
    data.append([gene_location, gene_name, misc_location, misc_gene_name, misc_note, cds_location, cds_gene_name, product, protein_id])

df = pd.DataFrame(data, columns=['Gene Location', 'Gene Name', 'Misc Location', 'Misc Gene Name', 'Misc Note', 'CDS Location', 'CDS Gene Name', 'Product', 'Protein ID'])

# 保存为 XLS 文件
df.to_excel('mpox.xlsx', index=False)