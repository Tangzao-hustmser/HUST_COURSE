import os

source_dir = r"d:\coding\HUST_COURSE\docs\source"
output_md = r"d:\coding\HUST_COURSE\COURSE_CATALOG.md"

# Define the order and display names
order = [
    ("guidebook", "生存指南"),
    ("ideological_politics", "思政课程"),
    ("general_education", "通识与公共基础"),
    ("science", "理学课程"),
    ("mathmatics", "数学类课程 (旧版/英文)"),
    ("information", "信息类课程"),
    ("electrical", "电学课程"),
    ("professional_elective", "专业选修课程"),
    ("practice", "集中实践与实训"),
    ("public_elective", "公选课程"),
    ("open_course", "通识/其他课程"),
]

md_content = "# 华中科技大学课程攻略共享计划 - 课程目录\n\n"
md_content += "欢迎大家在飞书文档中对课程进行评价！请在对应课程下方直接填写内容。\n\n"

for folder, name in order:
    folder_path = os.path.join(source_dir, folder)
    if os.path.exists(folder_path):
        md_content += f"## {name}\n\n"
        
        files = os.listdir(folder_path)
        # Filter for .rst files, exclude index.rst
        courses = [f for f in files if f.endswith(".rst") and f != "index.rst"]
        
        for course in courses:
            course_name = os.path.splitext(course)[0]
            display_name = course_name.replace("_", " ")
            # 使用三级标题，下面预留较大空白
            md_content += f"### {display_name}\n\n"
            md_content += "*(在此处填写评价、避雷指南或粘贴资料链接)*\n\n"
            # 插入多个空行
            md_content += "\n" * 6 
        
        md_content += "---\n\n"

with open(output_md, "w", encoding="utf-8") as f:
    f.write(md_content)

print(f"Generated {output_md}")
