# Automatically Export Sketches to DXF for current Fusion 360 model
A gem for laser cutters any anyone who needs dxf for producing their model. 

Instead of manually exporing each sketch individually and naming it after each update, this script will first ask for a directory and then export all sketches with names that begins with "Ex_" or "ex_". Files names will match the sketch name. The purpose of only exporting sketches that start with the "ex_" or "Ex_" is so that you can pick and choose which sketches are relavent for export. 

Adding the script to fusion is easy. 
1) Go to "Utilities" tab at top of open model and click on "Add-ons" tool and open the scripts window. (or press shift+s)
2) Click "create" and name the script.
3) For me a blank skript is oppend in Visual Studio Code (free program). I am not sure what will happen if you do not have this code editor installed. Simply paste in the script and you are good to go. 

