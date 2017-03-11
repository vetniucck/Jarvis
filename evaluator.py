def calc(s):
    # You should really use floats...
    
    s = str.lower(s)
    replace_dict = {"power": "**",
                    "plus": "+",
                    "minus": "-",
                    "divided": "/", # Changed this keyword cause dicts are not ordered
                    "by": "*",
                    "^": "**"}
    
    for key in replace_dict.keys():
        s = s.replace(key, replace_dict[key])
    
    try:
        # This is not good, look at ast.literaleval() for a safer way to do this
        x = eval(s)
        print(x)
    except Exception: # This is not good either, shit to debug
        print("Error : Not in correct format")
