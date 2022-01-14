from anvil import *

class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    #Setting up card backgrounds
    self.card_1.background = '#000000'
    self.card_2.background = '#353434'
    self.card_3.background = '#000000'
    self.card_4.background = '#000000'
    self.card_5.background = '#000000'
    self.card_6.background = '#000000'
    
    # Setting up 1st dropdown 
    self.drop_down_1.enabled = True
    self.drop_down_1.items = [['1',1],['2',2],['3',3],['4',4],['5',5],['6',6],
                             ['7',7],['8',8],['9',9],['10',10]]
    self.drop_down_1.include_placeholder = False
    self.drop_down_1.placeholder = "Choose number of Columns"
    
    # Setting up 2nd dropdown
    self.drop_down_2.enabled = True
    self.drop_down_2.items =  [['1',1],['2',2],['3',3],['4',4],['5',5],['6',6],
                             ['7',7],['8',8],['9',9],['10',10]]
    self.drop_down_2.placeholder = "Choose number of Rows"
    
    self.primary_color_1.background = "353434"
    self.primary_color_1.background = "353434"
    
    
    
    # Any code you write here will run when the form opens.
    
    def categorise_button_click(self, **event_args):
    '''This method is called when the Gernerate button is pressed.'''
    # Call the google colab function and pass it the needed argumennts
    canvas = anvil.server.call('generate_image_grid', 
                                getColumns(),
                              getRows())
    
    def getColumns():
      # to be written
    def getColumns():
      # to be written
    # If a category is returned set our species
    if iris_category:
      self.species_label.visible = True
      self.species_label.text = "The species is " + iris_category.capitalize()
