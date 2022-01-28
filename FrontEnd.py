from anvil import *
import anvil.server

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
    
  
    

  def primary_color_1_click(self, **event_args):
    if (self.check_box_1.checked == True):
        canvas = anvil.server.call( 'generate_image_grid', anvil.server.call('interpolate', tensors, getRow))
    else:
        canvas = anvil.server.call('generate_image_grid', getColumns(),getRows())
        
    self.image_2.source = anvil.server.call('get_img_url')
                                   
     
  def primary_color_2_click(self, **event_args):
    if (self.check_box_1.checked == True):
        canvas = anvil.server.call( 'generate_image_grid', anvil.server.call('interpolate', tensors, getRow))
    else:
          canvas = anvil.server.call('generate_image_grid', anvil.server.call(make_frame) getColumns(),getRows())
        
    self.image_2.source = anvil.server.call('get_img_url')
    pass
  
  def make_frame(self, t):
    frame_idx = int(np.clip(np.round(t * fps), 0, num_frames - 1))
    latents = all_latents[frame_idx]
    fmt = dict(func=tflib.convert_images_to_uint8, nchw_to_nhwc=True)
    images = Gs.run(latents, None, truncation_psi=truncation_psi,
                          randomize_noise=False, output_transform=fmt, 
                          minibatch_size=16)

    grid = create_image_grid(images, grid_size)
    if image_zoom > 1:
        grid = scipy.ndimage.zoom(grid, [image_zoom, image_zoom, 1], order=0)
    if grid.shape[2] == 1:
        grid = grid.repeat(3, 2) # grayscale => RGB
    return grid
    
    
  def getColumns(self):
    column = self.drop_down_1.selected_value  
  def getRow(self):
    row = self.drop_down_1.selected_value

    
    training_data = []

def main():
    for category in CATEGORIES:

        path = os.path.join(DATADIR,category)  
        class_num = CATEGORIES.index(category)  

        for file in os.listdir(path):  
            #print("test" + file)
            if not file.startswith("._"):
                image = nib.load(os.path.join(path, file))
                print(0)
                print(image.shape)

                training_data.append([nib.load(os.path.join(path,file)).get_fdata(),class_num])

if __name__ == '__main__':
    main()
    random.shuffle(training_data)

    X = []
    y = []

    for features, label in training_data:
        X.append(features)
        y.append(label)
