import pandas as pd

# 创建数据
data = {
    "序号": list(range(1, 51)),
    "名称": [
        "Chemokine binding protein",
        "Crm-B secreted TNF-alpha-receptor-like protein",
        "Ankyrin repeat protein (39)",
        "EGF-like domain protein",
        "Zinc finger-like protein (2)",
        "Interleukin-18-binding protein",
        "Ankyrin repeat protein (2)",
        "retroviral pseudoprotease-like protein",
        "Ankyrin repeat protein (14)",
        "Host range protein",
        "Bcl-2-like protein",
        "Kelch-like protein (1)",
        "C4L/C10L-like family protein",
        "Bcl-2-like protein",
        "Bcl-2-like protein",
        "Bcl-2-like protein",
        "Ankyrin-like protein (1)",
        "NFkB inhibitor",
        "Ankyrin-like protein (3)",
        "Serpin",
        "Phospholipase-D-like protein",
        "Putative monoglyceride lipase",
        "Bcl-2-like protein",
        "dUTPase",
        "Ribonucleotide reductase small subunit",
        "Telomere-binding protein I6 (1)",
        "CPXV054 protein",
        "Cytoplasmic protein",
        "IMV membrane protein L1R",
        "Serine/threonine-protein kinase",
        "Protein F11",
        "EEV maturation protein",
        "Protein F14 (1)",
        "Cytochrome C oxidase",
        "Protein F15",
        "Protein F16 (1)",
        "DNA-binding phosphoprotein (1)",
        "Poly(A) polymerase catalytic subunit (3)",
        "Iev morphogenesis protein",
        "Double-stranded RNA binding protein",
        "IMV membrane protein E6",
        "Myristoylated protein E7",
        "Membrane protein E8",
        "DNA polymerase (2)",
        "Sulfhydryl oxidase",
        "Virion core protein E11",
        "Iev morphogenesis protein",
        "Glutaredoxin-1",
        "MV membrane EFC component",
        "Telomere-binding protein I1"
    ],
    "长度": [
        "246 aa", "348 aa", "437 aa", "142 aa", "242 aa", "126 aa", "660 aa", "64 aa", "630 aa", "150 aa",
        "153 aa", "206 aa", "315 aa", "214 aa", "117 aa", "177 aa", "442 aa", "220 aa", "284 aa", "375 aa",
        "424 aa", "276 aa", "149 aa", "151 aa", "319 aa", "317 aa", "74 aa", "64 aa", "212 aa", "439 aa",
        "354 aa", "635 aa", "73 aa", "49 aa", "158 aa", "231 aa", "101 aa", "479 aa", "737 aa", "153 aa",
        "567 aa", "166 aa", "273 aa", "1006 aa", "95 aa", "129 aa", "665 aa", "108 aa", "35 aa", "312 aa"
    ],
    "编号": [
        "XFH17391.1", "XFH17392.1", "XFH17393.1", "XFH17394.1", "XFH17395.1", "XFH17396.1", "XFH17397.1", "XFH17398.1",
        "XFH17399.1", "XFH17400.1", "XFH17401.1", "XFH17402.1", "XFH17403.1", "XFH17404.1", "XFH17405.1", "XFH17406.1",
        "XFH17407.1", "XFH17408.1", "XFH17409.1", "XFH17410.1", "XFH17411.1", "XFH17412.1", "XFH17413.1", "XFH17414.1",
        "XFH17415.1", "XFH17416.1", "XFH17417.1", "XFH17418.1", "XFH17419.1", "XFH17420.1", "XFH17421.1", "XFH17422.1",
        "XFH17423.1", "XFH17424.1", "XFH17425.1", "XFH17426.1", "XFH17427.1", "XFH17428.1", "XFH17429.1", "XFH17430.1",
        "XFH17431.1", "XFH17432.1", "XFH17433.1", "XFH17434.1", "XFH17435.1", "XFH17436.1", "XFH17437.1", "XFH17438.1",
        "XFH17439.1", "XFH17440.1"
    ],
    "GI": [
        "2797670992", "2797670993", "2797670994", "2797670995", "2797670996", "2797670997", "2797670998", "2797670999",
        "2797671000", "2797671001", "2797671002", "2797671003", "2797671004", "2797671005", "2797671006", "2797671007",
        "2797671008", "2797671009", "2797671010", "2797671011", "2797671012", "2797671013", "2797671014", "2797671015",
        "2797671016", "2797671017", "2797671018", "2797671019", "2797671020", "2797671021", "2797671022", "2797671023",
        "2797671024", "2797671025", "2797671026", "2797671027", "2797671028", "2797671029", "2797671030", "2797671031",
        "2797671032", "2797671033", "2797671034", "2797671035", "2797671036", "2797671037", "2797671038", "2797671039",
        "2797671040", "2797671041"
    ]
}

# 创建DataFrame
df = pd.DataFrame(data)

# 保存为Excel文件
df.to_excel("monkeypox_virus_data_first_50.xlsx", index=False)