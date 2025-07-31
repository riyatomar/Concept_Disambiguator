import os

input_usr_folder = "usr_mod/"
con = []
usr_files = os.listdir(input_usr_folder)

def read_concept_row(file_path):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            if len(lines) >= 2:
                second_line = lines[1].strip()
                return second_line, lines
            else:
                return None, None
    except Exception as e:
        return None, None

for file_name in usr_files:
    file_path = os.path.join(input_usr_folder, file_name)

    if os.path.isfile(file_path):
        second_line, file_lines = read_concept_row(file_path)
        if second_line is not None:
            hyphen_count = second_line.count("-")

            if hyphen_count > 1:
                concepts = [concept.strip() for concept in second_line.split(",")]
                corrected_concepts = []

                for concept in concepts:
                    if '-' in concept:
                        hyphen_parts = concept.split('-')
                        if len(hyphen_parts) > 2:
                            # Correct by joining only the first two parts
                            corrected_concept = hyphen_parts[0] + "-" + hyphen_parts[1]
                            corrected_concepts.append(corrected_concept)
                        else:
                            corrected_concepts.append(concept)
                    else:
                        corrected_concepts.append(concept)

                # Rebuild the second line with corrected concepts
                corrected_second_line = ",".join(corrected_concepts) + "\n"
                file_lines[1] = corrected_second_line  # Replace the second line

                # Write the corrected lines back to the file
                with open(file_path, "w") as file:
                    file.writelines(file_lines)

                # print(f"Corrected Second Line in {file_name}:")
                # print(corrected_second_line)
            else:
                # print(f"No correction needed for Second Line in {file_name} \n")
                continue
