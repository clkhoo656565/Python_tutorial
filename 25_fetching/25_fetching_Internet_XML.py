import xml.dom.minidom
import os

def main():
    path = r'C:\Users\ckhoo5\OneDrive - DXC Production\Documents\Python\Tutorial'
    doc = xml.dom.minidom.parse(os.path.join(path, "samplexml.xml"))

    print(doc.nodeName)
    print(doc.firstChild.tagName)

    skills = doc.getElementsByTagName("skill")
    print("%d skills: " % skills.length)
    for skill in skills:
        print(skill.getAttribute("name"))
    

    # create a new XML tag and add it into the document
    newSkill = doc.createElement("skill")
    newSkill.setAttribute("name", "jQuery")
    doc.firstChild.appendChild(newSkill)

    skills = doc.getElementsByTagName("skill")
    print("%d skills: " % skills.length)
    for skill in skills:
        print(skill.getAttribute("name"))


if __name__ == "__main__":
    main()