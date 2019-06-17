from rsrc.base import deserialize

from rsrc_local.models import (Directory,
                               File)
from .paths import (existent_directories_paths_strings,
                    existent_directories_paths_url_strings,
                    existent_files_paths_strings,
                    existent_files_paths_url_strings,
                    non_empty_directories_paths_strings,
                    non_existent_paths_strings)

existent_directories = ((existent_directories_paths_strings
                         | existent_directories_paths_url_strings)
                        .map(deserialize))
non_empty_directories = (non_empty_directories_paths_strings
                         .map(Directory.from_string))
non_existent_directories = (non_existent_paths_strings
                            .map(Directory.from_string))
directories = existent_directories | non_existent_directories
existent_files = ((existent_files_paths_strings
                   | existent_files_paths_url_strings)
                  .map(deserialize))
non_existent_files = non_existent_paths_strings.map(File.from_string)
files = existent_files | non_existent_files
existent_resources = existent_directories | existent_files
non_existent_resources = non_existent_directories | non_existent_files
resources = existent_resources | non_existent_resources
