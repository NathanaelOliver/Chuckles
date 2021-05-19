import os

def main():
  f = open("scrollbar.html","w+")
  print_begin(f)
  print_head(f)
  print_style(f)
  print_scripts(f)
  print_body(f)
  print_end(f)

def print_begin(f):
  f.write("<!DOCTYPE html>\n<html lang=\"en\">\n")

def print_head(f):
  f.write("\t<head>\n\t\t<title>Scrollbar Widget</title>\n\t\t<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n\t</head>\n")



def print_scripts(f):
  f.write("\t<script>\n\t\tfunction changeImage(id, newImage) {\n\t\t\tvar img = document.getElementById(id);\n\t\t\timg.src=newImage;\n\t\t\treturn false;\n\t\t}\n\t</script>\n")

def print_body(f):
  f.write("\t<body>\n\t\t<div class=\"scrollmenu\">\n")
  arr = os.listdir('./Cabinets')
  sorted_arr = sort(arr)
  for element in sorted_arr:
    make_card(f, element)
  f.write("\t\t</div>\n\t</body>\n")

def sort(arr):
  list1 = []
  list2 = []
  cabinet_type = type_of(arr[0])
  for element in arr:
    if type_of(element) != cabinet_type:
      list1.append(list2)
      list2 = []
      cabinet_type = type_of(element)
    list2.append(element)
  return list1

def make_card(f, set):
  f.write("\t\t\t<div class=\"card\">\n\t\t\t\t<h1>")
  f.write(format(set[0]))
  f.write("</h1>\n\t\t\t\t<img id=\"")
  f.write(type_of(set[0]))
  f.write("\" src=\"Cabinets/")
  f.write(set[0])
  f.write("\" alt=\"Image Unavailable\">\n")
  f.write("\t\t\t\t<div class=\"button-group\">\n")
  for element in set:
    make_button(f, element)
  f.write("\t\t\t\t</div>\n")
  f.write("\t\t\t</div>\n")

def make_button(f, element):
  f.write("\t\t\t\t\t<button onclick=\"changeImage('")
  f.write(type_of(element))
  f.write("', 'Cabinets/")
  f.write(element)
  f.write("');\"/>\n")

def format(str):
  return str.replace("_", " ")[0:-4]

def type_of(str):
  return str[0:str.index(" ")]

def print_end(f):
  f.write("</html>\n")


def print_style(f):
  f.write('''<style>
:root {
--beige: #d4c9bd;
--white: #ffffff;
--brown: #5a4d46;
--green: #9ba167;
--none: #ffffff00;
}
div.scrollmenu {
background-color: var(--beige);
overflow: auto;
white-space: nowrap;
display: flex;
}
div.card {
padding: 20px;
padding-left: 30px;
padding-right: 30px;
margin: 40px;
margin-bottom: 10px;
background: var(--white);
border-radius: 10px;
border-style: solid;
border-width: 4px;
border-color: var(--green);
}
div.card h1{
text-align: center;
color: var(--brown);
}
div.card img{
height: 400px;
display: block;
margin-left: auto;
margin-right: auto;
margin-bottom: 20px;
}
div.button-group {
margin: auto;
display: flex;
flex-direction: row;
justify-content: center;
}
div.button-group button{
background-color: var(--green); /* Green background */
border: 1px solid var(--brown); /* Green border */
color: var(--none); /* White text */
width: 30px;
height: 30px;
cursor: pointer; /* Pointer/hand icon */
}
</style>''')























main()