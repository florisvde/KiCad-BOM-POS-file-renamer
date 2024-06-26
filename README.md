# KiCad-BOM-POS-file-renamer
Python REPL to rename and reorder BOM and position files columns generated by KiCad.

The program is set to produce JLCPCB compatible files, see [JLC's post](https://jlcpcb.com/help/article/81-How-to-generate-the-BOM-and-Centroid-file-from-KiCAD) explaining the format. 
It can however be easily adapted to suit other EMS's requirements.

Copy the BOM and position files to the same directory as the program. 
The input files should have the following format: `<KiCad Project Name><Input Suffix>.csv`. The REPL will ask the user for the KiCad Project Name, what files to rename and assume the input suffix. The table below shows the expected input suffix and the produced output file suffix upon successfull conversion:

| File type  | Input Suffix | Output Suffix | 
| ------------- | ------------- | ------------- | 
| BOM  | `-BOM.csv`  | `-JLC-BOM.csv` |
| Top Position File  | `-top-pos.csv`  | `-top-CPL.csv` | 
| Bottom Position File | `-bottom-pos.csv` | `-bottom-CPL.csv` |
