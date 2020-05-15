# -*- coding: utf-8 -*-
"""
Created on Mon May 11 16:36:44 2020

@author: NAVEENA
"""


import xml.etree.ElementTree as ET


def elementtree_to_dict(element):
    node = dict()                            

    text = element.text
    
    if text is not None:
        node['text'] = text                       #storing text
   
    node.update(element.attrib)                   #storing attribute
   
    child_nodes = {}  
    
    for child in element:    
       child_nodes.setdefault(child.tag, []).append(elementtree_to_dict(child))
     
    for key, value in child_nodes.items():
       if len(value) == 1:
             child_nodes[key] = value[0]
             
    node.update(child_nodes)
  
    return node

def get_tag_name(element):
    
  elemList = []
  root=element.tag
  for elem in element.iter():
    elemList.append(elem.tag)

  elemList = list(set(elemList))
  elemList.remove(root)
  print("Welcome to our book store")
  
  for i,j in enumerate(elemList,start=1):
    print ("{}.{}".format(i,j))
 
  
def get_recursively(search_dict, field):
   
    fields_found = []

    for key, value in search_dict.items():

        if key == field:
            fields_found.append(value)

        elif isinstance(value, dict):
            results = get_recursively(value, field)
            for result in results:
                fields_found.append(result)

        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    more_results = get_recursively(item, field)
                    for another_result in more_results:
                        fields_found.append(another_result)

    return fields_found


    
   
def print_value(result,field):
    

  for data in result:
     if isinstance(data, dict) and len(data.values())!=1:
      for key, value in data.items():
          
            
             
             if isinstance(value,dict) and  len(value.values())==1:
                 one_value(key,value)
                               
             elif isinstance(value,dict):
                  multiple_values(key,value)
                        
                         
             elif isinstance(value,list):
                  multiple_values(key,value)
                       
             else:
                 
                 if (key=='text' and '\n' in value):
                      pass
                 else:
                       print(key,':',value)
                   
                             
        
     elif isinstance(data, list):
             print_value(data,field)
       
     elif isinstance(data,dict) and len(data.values())==1:
         one_value(field,data)
         
     
             
def one_value(key,value):
     for k,v in value.items():
        if (k=='text' and '\n' in v ):
           pass
        else:
           print(key,':',v)
          
def multiple_values(key,value):
    
    if isinstance(value,dict):
      c=[]
      for k,v in value.items():
        if (k=='text' and '\n' in v ):
            pass
        else:
           c.append({k:v})
      print(key,':',c)
      
      
    elif isinstance(value,list):
          d=[]
          for x in value:
              for k,v in x.items():
                if (k=='text' and '\n' in v ):
                   pass
                else:
                    d.append({k:v})
          print(key,':',d)  
          
  
        
                 
def main():      

        
 mytree = ET.parse('madurai.xml')
 myroot = mytree.getroot()  
 get_tag_name(myroot)
 print("Please enter a value")
 node=elementtree_to_dict(myroot)
 val = input("Enter your value: ") 
 result=get_recursively(node,val)
 
 if (result):
   print_value(result,val)
 else:
     print('your query didnt match.Pls try again')




    
if __name__ == '__main__':
    main()








          
            





        
        
        
               