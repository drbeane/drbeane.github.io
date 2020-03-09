import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mplc

def plot_regions(model, X, y, 
                 num_ticks=100, cmap='rainbow', fig_size = None, legend=True, 
                 close=True, display=True, path=None, keras=False):

    # Convert X to numpy array
    X = np.array(X)
    y = np.array(y)
    
    # Check to see if there are exactly 2 features
    if X.shape[1] != 2:
        raise Exception('Training set must contain exactly ' + 
                        'two features.')
        
     
    # Find min and max points for grid axes
    minx, maxx = min(X[:,0]), max(X[:,0])
    marginx = (maxx - minx) / 20
    x0, x1 = minx - marginx, maxx + marginx
    
    miny, maxy = min(X[:,1]), max(X[:,1])
    marginy = (maxy - miny) / 20
    y0, y1 = miny - marginy, maxy + marginy
    
    # Create grid tick marks
    xticks = np.linspace(x0, x1, num_ticks)
    yticks = np.linspace(y0, y1, num_ticks)
    
    # Create array of grid points
    # tile stacks copies of xticks end creating a size num_ticks^2 array
    # repeat repeats each elt of yticks to create a size num_ticks^2 array
    # They are combined into an array of shape (2, num_ticks^2)
    # transpose creates array of pts with shape (num_ticks^2, 2).
    grid_pts = np.transpose([np.tile(xticks,len(yticks)),
                             np.repeat(yticks,len(xticks))])
    
    # Feed grid points to model to generate 1D array of classes
    if(keras==True): 
        class_pts = model.predict_classes(grid_pts)
        class_pts = class_pts.reshape((len(class_pts),))
    else:
        class_pts = model.predict(grid_pts)

    # Get list of classes. This could, in theory, contain text labels.
    classes = np.unique(y)
    k = len(classes)    
        
    # create new list with numerical classes
    class_pts_2 = np.zeros(class_pts.shape)
    for i in range(len(classes)):
        sel = class_pts == classes[i]
        class_pts_2[sel] = i

    # reshape classification array into 2D array corresponding to grid
    class_grid = class_pts_2.reshape(len(xticks),len(yticks) )
    
    # Set a color map        
    my_cmap = plt.get_cmap(cmap)
          
    # Close any open figures and set plot size.
    
    if(close): 
        plt.close()
    if(not fig_size is None):
        plt.figure(figsize=fig_size)
    
    # Add color mesh
    plt.pcolormesh(xticks, yticks, class_grid, cmap = my_cmap, zorder = 1, 
                   vmin=0, vmax=k-1 )
    
    # Add transparency layer to lighten the colors
    plt.fill([x0,x0,x1,x1], [y0,y1,y1,y0], 'white', alpha=0.5, zorder = 2)
    
    # Select discrete cuts for color map
    cuts = np.arange(k) / (k - 1)

    # Add scatter plot for each class, with seperate colors and labels
    for i in range(k):
        sel = y == classes[i]       
        
        my_c = mplc.rgb2hex(my_cmap(cuts[i]))
        plt.scatter(X[sel,0],X[sel,1], c=my_c, edgecolor='k', 
                    zorder=3, label=classes[i])

    if(legend):
        plt.legend()
    
    if(not path is None):
        plt.savefig(path, format='png')

    
    if(display): 
        plt.show()


def vis_training(h, start=0, show_val=True):
    
    rng = range(start+1, len(h.history['loss'])+1)
    
    plt.figure(figsize = (8,4))
    
    plt.subplot(1,2,1)
    plt.plot(rng, h.history['loss'][start:], label='Training')
    if(show_val): plt.plot(rng, h.history['val_loss'][start:], label='Validation')
    plt.title('Loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend()
        
    plt.subplot(1,2,2)
    plt.plot(rng, h.history['acc'][start:], label='Training')
    if(show_val): plt.plot(rng, h.history['val_acc'][start:], label='Validation')
    plt.title('Accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.legend()

    plt.show()
    
def view_activations(model, input_img, layers_to_display, 
                     plot_size=(3,3), filters_per_row=4,
                     cmap='viridis'):
    
    import keras
    import math
    #-------------------------------------------
    # Create an run activation model
    #-------------------------------------------
    layer_outputs = [layer.output for layer in model.layers]
    activation_model = keras.models.Model(inputs=model.input, outputs=layer_outputs)
    activations = activation_model.predict(input_img)
    
    #-------------------------------------------
    # Display Activations
    #-------------------------------------------
    
    # Loop over desired layers. 
    for i in range(len(layers_to_display)):
        idx = layers_to_display[i]
        print(model.layers[idx].name)
        act = activations[idx]
        num_filters = act.shape[3]
        num_rows = math.ceil(num_filters / filters_per_row)
        fig_size = [plot_size[0] * filters_per_row, plot_size[1] * num_rows]
        plt.figure(figsize = fig_size)
        
        # Loop over all filters in the current layer.    
        for j in range(num_filters):
            plt.subplot(num_rows, filters_per_row, j+1)
            plt.imshow(act[0, :, :, j], cmap=cmap)
            plt.axis('off')
        plt.show()


def deprocess_image(x):
    x -= x.mean()
    x /= (x.std() + 1e-5)
    x *= 0.1

    x += 0.5
    x = np.clip(x,0,1)

    x *= 255
    x = np.clip(x, 0, 255).astype('uint8')
    return x[0]
   

#def visualise_filter(model, layer, sel_filter, plot_size=(3,3),
#                     step=1, iter=100):    
#    
#    from keras import backend as K
#    import math
#    
#    # Complete this later
#    
    
    
def max_filter_activation(model, layers_to_display, selected_filters = None,
                          output_size=(64,64), plot_size=(3,3), 
                          filters_per_row=4, row_by_row=False,
                          step=1, iter=100, obj_val=False, obj_hist=False):
    
    from keras import backend as K
    import math
    
        
    # Loop over desired layers. 
    for i in range(len(layers_to_display)):
        
        # Get layer number and name
        idx = layers_to_display[i]
        print(model.layers[idx].name, '--', model.layers[idx].output.shape)
        
        # Get layer output
        layer_output = model.layers[idx].output

        # Get input size, number of filters, and number of rows
        #print(model.layers[0].input.shape[1] == None)
        
        #height = int(model.layers[0].input.shape[1])
        height = output_size[0]
        #width = int(model.layers[0].input.shape[2])
        width = output_size[1]
        num_filters = int(layer_output.shape[3])
        
        num_rows = math.ceil(num_filters / filters_per_row)
        if(row_by_row == True): num_rows = 1
        
        # Prepare plot
        fig_size = [plot_size[0] * filters_per_row, plot_size[1] * num_rows]
        plt.figure(figsize = fig_size)
        
        # Determine selected filters
        if(selected_filters is None):
            f_range = range(num_filters)
        else:
            f_range = selected_filters
        
        # Loop over all filters in current layer
        for j in f_range:
            
            
            # Define objective function to be maximizes
            objective = K.mean(layer_output[:, :, :, j])
            grad = K.gradients(objective, model.input)[0]
            grad /= (K.sqrt(K.mean(K.square(grad))) + 1e-5)
            iterate = K.function([model.input], [objective, grad])

            # Randomly generate input impage
            input_img_data = np.random.random((1, height, width, 3)) * 20 + 128.

            # run gradient ascent
            for n in range(iter):
                obj_value, grad_value = iterate([input_img_data])
                input_img_data += grad_value * step
                if(obj_hist): 
                    print('Objective:', obj_value)

            subplot_num = j   
            if(row_by_row == True): 
                subplot_num = subplot_num % filters_per_row
            
            #print(num_rows, filters_per_row, subplot_num + 1)
            plt.subplot(num_rows, filters_per_row, subplot_num + 1)
            plt.imshow(deprocess_image(input_img_data))
            if(obj_val): plt.text(0,-5,str(obj_value))
            plt.axis('off')
        
            if(row_by_row and subplot_num + 1 == filters_per_row):
                plt.show()
                if(j != f_range[-1] - 1): plt.figure(figsize = fig_size)
            
        if(row_by_row == False): plt.show()
    
    
    