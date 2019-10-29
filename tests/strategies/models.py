from rsrc_local.base import (deserialize_path,
                             deserialize_url)
from rsrc_local.models import (Directory,
                               File)
from .paths import (existent_directories_paths_strings,
                    existent_directories_paths_url_strings,
                    existent_files_paths_strings,
                    existent_files_paths_url_strings,
                    non_empty_directories_paths_strings,
                    non_existent_paths_strings)

existent_directories = (
    (existent_directories_paths_strings.map(deserialize_path)
     | existent_directories_paths_url_strings.map(deserialize_url)))
non_empty_directories = (non_empty_directories_paths_strings
                         .map(Directory.from_string))
non_existent_directories = (non_existent_paths_strings
                            .map(Directory.from_string))
directories = existent_directories | non_existent_directories
existent_files = (existent_files_paths_strings.map(deserialize_path)
                  | existent_files_paths_url_strings.map(deserialize_url))
non_existent_files = non_existent_paths_strings.map(File.from_string)
files = existent_files | non_existent_files
existent_resources = existent_directories | existent_files
non_existent_resources = non_existent_directories | non_existent_files
resources = existent_resources | non_existent_resources
