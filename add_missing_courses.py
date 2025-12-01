import os

base_dir = r"d:\coding\HUST_COURSE\docs\source"

# 新增的分类和课程
new_categories = {
    "general_education": {
        "title": "通识与公共基础",
        "courses": [
            "中国语文", "综合英语_一", "综合英语_二",
            "大学体育_一", "大学体育_二", "大学体育_三",
            "军事理论", "军事训练", "国家安全教育",
            "大学生心理健康", "劳动教育", "工程制图_一"
        ]
    },
    "practice": {
        "title": "集中实践与实训",
        "courses": [
            "工程训练_三", "软件课程设计", "硬件课程设计",
            "生产实习", "毕业设计_论文",
            "科研创新实践", "社会实践活动"
        ]
    }
}

# 需要补全到现有分类的课程
append_courses = {
    "professional_elective": ["计算机网络实验"]
}

template = """{course_name}
======================

基本信息
--------
* **学分**: 待补充
* **教材**: 待补充
* **前置课程**: 待补充

速通指南
--------
* **是否可以速通**: (例如：是，考前突击3天即可 / 否，需平时积累)
* **速通建议**: 
  * (例如：重点复习第三章，放弃第五章推导)
* **推荐资源**: 
  * `XX速成视频 <URL>`_

课程评价
--------
*(在这里写学长学姐的主观评价，比如：)*
* “这门课主要靠背，理解不难。”
* “期中考试很难，期末会调分。”

历年试卷
--------
* :download:`2021-2022学年秋冬学期试卷 <../../downloads/xxx.pdf>`
* :download:`2020-2021学年秋冬学期试卷 <../../downloads/xxx.pdf>`

复习资料
--------
* `外部链接：学长整理的思维导图 (GitHub) <https://github.com/xxxx>`_
* :download:`课堂PPT合集 (ZIP) <../../downloads/xxx.zip>`
"""

index_template = """{title}
{underline}

.. toctree::
   :maxdepth: 2
   :caption: {title}

{toc_entries}
"""

def create_missing_files():
    # 1. 处理新分类
    for cat_key, cat_data in new_categories.items():
        cat_dir = os.path.join(base_dir, cat_key)
        os.makedirs(cat_dir, exist_ok=True)
        
        toc_entries = ""
        for course in cat_data["courses"]:
            filename = course
            file_path = os.path.join(cat_dir, f"{filename}.rst")
            
            # 只有文件不存在时才创建，避免覆盖
            if not os.path.exists(file_path):
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(template.format(course_name=course))
                print(f"Created {filename}.rst in {cat_key}")
            
            toc_entries += f"   {filename}\n"
            
        # 创建或更新 index.rst
        index_path = os.path.join(cat_dir, "index.rst")
        title = cat_data["title"]
        underline = "=" * 30 
        
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(index_template.format(title=title, underline=underline, toc_entries=toc_entries))

    # 2. 处理补全课程
    for cat_key, courses in append_courses.items():
        cat_dir = os.path.join(base_dir, cat_key)
        if not os.path.exists(cat_dir):
            continue
            
        for course in courses:
            filename = course
            file_path = os.path.join(cat_dir, f"{filename}.rst")
            
            if not os.path.exists(file_path):
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(template.format(course_name=course))
                print(f"Created {filename}.rst in {cat_key}")
        
        # 更新该目录的 index.rst (简单追加)
        index_path = os.path.join(cat_dir, "index.rst")
        with open(index_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        if course not in content:
            with open(index_path, "a", encoding="utf-8") as f:
                f.write(f"   {course}\n")
            print(f"Appended {course} to {cat_key}/index.rst")

if __name__ == "__main__":
    create_missing_files()
