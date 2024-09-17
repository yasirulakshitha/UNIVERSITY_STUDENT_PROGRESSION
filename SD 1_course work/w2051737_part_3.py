from w2051737_part_4 import * #import the graphics.py module (must be in the same folder this file)

def graph_connect(data):

    win = GraphWin("My First Graphics Window", 800, 600) #open a window object called "win" with size and title
    win.setBackground("Mint Cream") # Set the background colour of the window

    bar_width = 100
    start_point = 150
    gap = 30

    list1 =["progress", "trailer","retriever","excluded"] # for display progression outcome in the bottom of ractangle
    colour = ["red", "orange","black","green"] # colours for rectangles
    data_total = sum(data) #for the bottom part to display the outcomes in total 
    max_data = max(data) # for the function that gives us the height for the each rectangle comparing the data list    

    for i in range(len(data)):

        """In the provided code, the data variable is a list that  passed as an argument to the graph_connect function.
        The for loop iterates over the indexes of this list using the range(len(data)) construct.
        So, the data[i] expression is used to retrieve the value at the current index of the data list within the loop """


        height = data[i] / max_data * 400      
                                               
            
        aRectangle = Rectangle(Point(start_point,500),Point(start_point + bar_width, 500 - height))#creating rectangles
        aRectangle.setFill(colour[i])
        aRectangle.draw(win)
        
        
        message_bottom = Text(Point(start_point + bar_width // 2 , 520),list1[i])#adding each progression name into specific rectangle
        message_bottom.draw(win)


        message_top = Text(Point(start_point + bar_width // 2 , 500-(height + 20)),data[i])#adding the numberof each count of progression outcomes to the top of rectangles
        message_top.draw(win)
        
        start_point = start_point + bar_width + gap #
        

        """after the above 1st loop iteration the starting point has to be execute.
           otherwise we can not have seperate ractangle bars beacuse of that we have to add GAP fot the next bar then we can have seperate bars for each one """



    tittle = Text(Point(120,60), "Histogram Results")#adding the tittle to the graph
    tittle.setStyle("bold")
    tittle.draw(win)

    message_bottom = Text(Point(130,550), f" {data_total} outcome in total")#adding total of outcomes in the graph
    message_bottom.draw(win)

    aline = Line(Point(100,500),Point(700,500)) #this is the line that in the bottom of the rectangles
    aline.draw(win)

    

