import os

def main():
  f = open("scrollbar.html","w+")
  fabuwood_arr = sort(os.listdir('./Cabinets/Fabuwood/'))
  cnc_arr = sort(os.listdir('./Cabinets/CNC/'))
  print_begin(f)
  print_head(f)
  f.write("  <style>\n")
  print_style(f, "Fabuwood", fabuwood_arr)
  print_style(f, "CNC", cnc_arr)
  f.write("  </style>\n")
  print_scripts(f)
  f.write("  <body>\n")
  print_body(f, "Fabuwood", fabuwood_arr)
  print_body(f, "CNC", cnc_arr)
  f.write("  </body>\n")
  print_end(f)

def print_begin(f):
  f.write("<!DOCTYPE html>\n<html lang=\"en\">\n")

def print_head(f):
  f.write("  <head>\n    <title>Scrollbar Widget</title>\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n  </head>\n")

def print_style(f, company, arr):
  
  f.write("    :root {\n      --black: #000000;\n      --beige: #d4c9bd;\n      --white: #ffffff;\n      --brown: #5a4d46;\n      --green: #9ba167;\n      --none: #ffffff00;\n    }\n")
  f.write("    div.scrollmenu {\n      background-color: var(--beige);\n      overflow: auto;\n      white-space: nowrap;\n      display: flex;\n    }\n")
  f.write("    div.card {\n      min-width: 250px;\n      display: block;\n      padding: 20px;\n      padding-left: 10px;\n      padding-right: 10px;\n      margin: 20px;\n      margin-bottom: 10px;\n      background: var(--white);\n      border-radius: 10px;\n      border-style: solid;\n      border-width: 4px;\n      border-color: var(--green);\n    }\n")
  f.write("    div.card h1{\n      text-align: center;\n      color: var(--brown);\n    }\n")
  f.write("    div.card img{\n      height: 300px;\n      display: block;\n      margin-left: auto;\n      margin-right: auto;\n      margin-bottom: 20px;\n    }\n")
  f.write("    div.button-group {\n      border-radius: 1px;\n      border-color: var(--black);\n      margin: auto;\n      display: flex;\n      flex-direction: row;\n      justify-content: center;\n    }\n")
  f.write("    div.button-group button{\n      color: var(--none);\n      width: 30px;\n      height: 52px;\n      cursor: pointer;\n    }\n")
  create_custom_buttons(f, company, arr)

def create_custom_buttons(f, company, arr):
  for element in arr:
    for e in element:
      f.write("    button.btn-")
      f.write(unformat(e))
      f.write(" {\n      background-image:url('Cabinets/" + company + "/")
      f.write(e)
      f.write("');\n      background-size: 26px;\n      margin: 2px;\n    }\n")

def unformat(str):
  return str.replace(" ", "-")[0:-4]

def print_scripts(f):
  f.write("  <script>\n    function changeImage(id, new_image, new_text) {\n      var img = document.getElementById(id + \" img\");\n      img.src=new_image;\n      document.getElementById(id + \" title\").innerHTML = new_text;\n      return false;\n    }\n  </script>\n")

def print_body(f, company, arr):
  f.write("    <div class=\"scrollmenu\">\n")
  for element in arr:
    make_card(f, company, element)
  f.write("    </div>\n")

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

def make_card(f, company, set):
  f.write("      <div class=\"card\">\n        <h1 id=\"" + company + " " + type_of(set[0]) + " title" + "\">")
  f.write(format(set[0]))
  f.write("</h1>\n        <img id=\"")
  f.write(company + " " + type_of(set[0]) + " img")
  f.write("\" src=\"Cabinets/" + company + '/' + set[0])
  f.write("\" alt=\"Image Unavailable\">\n")
  f.write("        <div class=\"button-group\">\n")
  for element in set:
    make_button(f, company, element)
  f.write("        </div>\n")
  f.write("      </div>\n")

def make_button(f, company, element):
  f.write("          <button class=\"btn-")
  f.write(unformat(element))
  f.write("\" onclick=\"changeImage('")
  f.write(company + " " + type_of(element))
  f.write("', 'Cabinets/" + company + "/" + element + "', '" + format(element))
  f.write("');\"/>\n")

def format(str):
  return str.replace("_", " ")[0:-4]

def type_of(str):
  return str[0:str.index(" ")]

def print_end(f):
  f.write("</html>\n")

main()