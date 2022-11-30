import os
import shutil
from sys import argv





translation = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'j', 'з': 'z', 'и': 'i',
               'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
               'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ъ': '', 'ы': 'y', 'ь': '',
               'э': 'e', 'ю': 'yu', 'я': 'ya', 'є': 'je', 'і': 'i', 'ї': 'ji', 'ґ': 'g', 'А': 'A', 'Б': 'B', 'В': 'V',
               'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E', 'Ж': 'J', 'З': 'Z', 'И': 'I', 'Й': 'J', 'К': 'K', 'Л': 'L',
               'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H',
               'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Sch', 'Ъ': '', 'Ы': 'Y', 'Ь': '', 'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya',
               'Є': 'Je', 'І': 'I', 'Ї': 'Ji', 'Ґ': 'G'}

punct_symbols = "!#$%&'\"()*+,№-/ :;<=>?@\][^`{|}~—"

""" """
def normalize(text):
    for c in punct_symbols:
        if c in text:
            text = text.replace(c, '_')

    for c in translation.keys():
        text = text.replace(c, translation[c])
    return text



docs = (".doc", ".docx", ".txt", ".pdf", ".xlsx", ".xls", ".pptx", ".ppt", ".csv")
images = (".jpeg", ".png", ".jpg", ".svg")
video = (".avi", ".mp4", ".mov", ".mkv")
audio = (".mp3", ".ogg", ".wav", ".amr")
archives = (".zip", ".rar", ".gz", ".tar")


docs_list = []
images_list = []
video_list = []
audio_list = []
archive_list = []
others_list = []

path_trash = []

known_extens_list = []
unknown_extens_list = []




def file_sorter(root_direct):

    filter_dir = [os.path.join(f"{root_direct}"), os.path.join(f"{root_direct}", "video"),
                  os.path.join(f"{root_direct}", "audio"), os.path.join(f"{root_direct}", "archives"),
                  os.path.join(f"{root_direct}", "images"), os.path.join(f"{root_direct}", "documents"),
                  os.path.join(f"{root_direct}", "others")]


    try:
        os.mkdir(os.path.join(f"{root_direct}", "video"))
    except FileExistsError:
        pass
    try:
        os.mkdir(os.path.join(f"{root_direct}", "audio"))
    except FileExistsError:
        pass
    try:
        os.mkdir(os.path.join(f"{root_direct}", "archives"))
    except FileExistsError:
        pass
    try:
        os.mkdir(os.path.join(f"{root_direct}", "images"))
    except FileExistsError:
        pass
    try:
        os.mkdir(os.path.join(f"{root_direct}", "documents"))
    except FileExistsError:
        pass
    try:
        os.mkdir(os.path.join(f"{root_direct}", "others"))
    except FileExistsError:
        pass

    for path, direct, files in os.walk(root_direct):
        path_trash.append(path)

        for file in files:

            if file.endswith(docs):
                extens_files = file.split('.')[-1]
                known_extens_list.append(extens_files)
                docs_list.append(normalize(file))
                try:
                    shutil.move(os.path.join(path, file), os.path.join(f"{root_direct}", "documents",
                                                                       f"{normalize(file)}"))
                except shutil.Error:
                    pass

            elif file.endswith(images):
                extens_files = file.split('.')[-1]
                known_extens_list.append(extens_files)
                images_list.append(normalize(file))
                try:
                    shutil.move(os.path.join(path, file), os.path.join(f"{root_direct}", "images",
                                                                       f"{normalize(file)}"))
                except shutil.Error:
                    pass

            elif file.endswith(video):
                extens_files = file.split('.')[-1]
                known_extens_list.append(extens_files)
                video_list.append(normalize(file))
                try:
                    shutil.move(os.path.join(path, file), os.path.join(f"{root_direct}", "video", f"{normalize(file)}"))
                except shutil.Error:
                    pass

            elif file.endswith(audio):
                extens_files = file.split('.')[-1]
                known_extens_list.append(extens_files)
                audio_list.append(normalize(file))
                try:
                    shutil.move(os.path.join(path, file), os.path.join(f"{root_direct}", "audio", f"{normalize(file)}"))
                except shutil.Error:
                    pass

            elif file.endswith(archives):
                arch_extens_files = file.split('.')[-1]
                known_extens_list.append(arch_extens_files)
                archive_list.append(normalize(file))

            else:
                if len(file.split('.')) != 1:
                    extens_files = file.split('.')[-1]
                    unknown_extens_list.append(extens_files)
                    others_list.append(normalize(file))
                try:
                    shutil.move(os.path.join(path, file), os.path.join(f"{root_direct}", "others"))
                except shutil.Error:
                    pass

    for path, direct, files in os.walk(root_direct):
        for file in files:

            if file.endswith(archives):

                old_file = os.path.join(path, file)
                new_file = os.path.join(path, normalize(file))
                os.rename(old_file, new_file)
                archive_dir = os.path.basename(new_file).split('.')[0]
                archive = os.path.basename(new_file)
                archive_path = os.path.join(f"{root_direct}", "archives", archive_dir)
                archive_path_file = os.path.join(f"{root_direct}", "archives", archive_dir, archive)

                try:
                    os.mkdir(archive_path)
                except FileExistsError:
                    pass

                filter_dir.append(archive_path)
                shutil.move(new_file, archive_path_file)

                try:
                    shutil.unpack_archive(archive_path_file, os.path.join(archive_path))
                except shutil.ReadError:
                    pass

    for path, direct, files in os.walk(root_direct):
        dir_del = list(set(path_trash) - set(filter_dir))

        for dir_path in sorted(dir_del, reverse=True):

            if not dir_path in ("video", "audio", "archives", "images", "documents", "others"):
                shutil.rmtree(dir_path, ignore_errors=True)

    print(f"List of known file formats: {set(known_extens_list)}")
    print(f"List of unknown file formats: {set(unknown_extens_list)}")

    print(f"""As a result of sorting, the files were found:
    Audio: {set(audio_list)}
    Video: {set(video_list)}
    Documents: {set(docs_list)}
    Pictures: {set(images_list)}
    Archives: {set(archive_list)}
    Others files: {set(others_list)}""")




if __name__ == '__main__':
    try:
        file_sorter(argv[1])
    except FileNotFoundError:
        print(f"The path '{argv[1]}' does not exist, please make sure it is typed correctly.")



