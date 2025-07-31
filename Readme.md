# Concept Disambiguator Tool
-----------------------------

## Required Files and Folders

Ensure the following files and folders are present in the specified structure before running the tool:

### 1. Parallel Corpus

- **Filepath**: `data/ParallelCorpus.xlsx`  
- Description: Excel file containing aligned Hindi-English sentence pairs.

### 2. Concept Dictionary

- **Filepath**: `data/H_concept-to-mrs-rels.dat`  
- Description: Mapping of Hindi concepts to their English meanings and MRS relations.

### 3. USR Input Folder

- **Folderpath**: `usr/`  
- Description: Folder containing individual USR files in CSV format.

--------------------------------------------------------------------

#### Example USR File:
'''
#अथ अतः दिनचर्याअध्यायम् व्याख्यास्यामः .								
xinacaryA_1,aXyAya_1,vi_Af_KyA_1-syawi_1,[6-tat_1]
1,2,3,4
,,,
,,pl,
,3:k2,nan:nan,
,,,
,,,
,,,
,,,
%affirmative
'''

## Installation Steps:

1. git clone https://github.com/LC-Platform/concept_disambiguator.git

2. cd concept_disambiguator

3. Install Python Dependencies by running this:
    - pip3 install pandas numpy wxc wxconv

4. Install Apertium and System Packages
    - sudo apt-get -f install apertium-all-dev
    - apt-cache policy | grep apertium
    - sudo apt-get install python3-openpyx
    - lt-comp lr apertium-eng.eng.dix eng.bin

5. After installing dependencies and preparing input files, run the tool using:
    - python3 main.py

## Output

- The output USR files will be generated in a new folder named [inputfolder]_mod.
- Example: If your input folder is usr/, the output will be stored in usr_mod/.

## Notes

- Ensure all paths are correctly set relative to the project root.
- The tool expects files to be formatted exactly as described above.