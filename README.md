# Python Mail Merge

## 📌 Overview  
This Python script automates the process of generating personalized letters using a list of names. It reads a template letter, replaces placeholders with actual names, and outputs ready-to-send letters in a specified directory.

## 🔧 Features  
- Reads a list of names from a file (`invited_names.txt`)  
- Reads a template letter (`starting_letter.txt`)  
- Replaces placeholders with names  
- Saves the personalized letters in the `Output/ReadyToSend/` directory  

## 🚀 Usage  
1. Place a list of names in `./Input/Names/invited_names.txt`, each on a new line.  
2. Prepare a template letter in `./Input/Letters/starting_letter.txt` with `....` as a placeholder.  
3. Run the script:  
   ```bash
   python mail_merge.py
   ```  
4. Generated letters will be stored in `./Output/ReadyToSend/`.

## 📂 File Structure  
```
📂 Project Root  
 ├── 📂 Input  
 │   ├── 📂 Names  
 │   │   └── invited_names.txt  
 │   ├── 📂 Letters  
 │   │   └── starting_letter.txt  
 ├── 📂 Output  
 │   ├── 📂 ReadyToSend  
 │   │   └── (Generated Letters)  
 ├── mail_merge.py  
 ├── README.md  
```

## 🛠️ Requirements  
- Python 3.x  

## 📜 License  
This project is open-source under the MIT License.

