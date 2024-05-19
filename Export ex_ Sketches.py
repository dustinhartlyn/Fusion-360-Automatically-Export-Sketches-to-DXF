import adsk.core, adsk.fusion, adsk.cam, traceback
import os

def export_sketches():
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)
        
        # Check if a design is active
        if not design:
            ui.messageBox('No active Fusion 360 design', 'No Design')
            return

        rootComp = design.rootComponent
        sketches = rootComp.sketches
        
        # Check if there are sketches in the design
        if sketches.count == 0:
            ui.messageBox('There are no sketches in the design.', 'No Sketches')
            return

        # Prompt user to select a directory for saving the sketches
        folderDialog = ui.createFolderDialog()
        folderDialog.title = "Select Directory to Save Sketches"
        dialogResult = folderDialog.showDialog()
        
        if dialogResult == adsk.core.DialogResults.DialogOK:
            selectedPath = folderDialog.folder
            
            # Loop through each sketch and export it as a DXF if its name starts with 'ex_' or 'Ex_'
            count = 0
            for i in range(sketches.count):
                sketch = sketches.item(i)
                if sketch.name.startswith(('ex_', 'Ex_')):
                    # Define the output filename
                    filename = os.path.join(selectedPath, sketch.name + '.dxf')
                    sketch.saveAsDXF(filename)
                    count += 1

            ui.messageBox('{} sketches exported to folder.'.format(count))
        else:
            ui.messageBox('No directory selected.', 'Operation Cancelled')

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

# Run the function
export_sketches()
