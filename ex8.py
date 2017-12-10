#Define formatter string with 4 empty slots
formatter = "{} {} {} {}"

#replace the empty slots with various inputs
print(formatter.format(1,2,3,4))
print(formatter.format("one","two","three","four"))
print(formatter.format(True,False,False,True))
print(formatter.format(formatter,formatter,formatter,formatter))
print(formatter.format("Guinea Pig","Guinea Piig","Guinea Piiig","Guinea Piiiig"))
