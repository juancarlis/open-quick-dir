import csv
import os

from src.dirs.models import Directory


class DirService:
    def __init__(self, table_name):
        self.table_name = table_name

    def add_dir(self, dir):
        with open(self.table_name, mode="a") as f:
            writer = csv.DictWriter(f, fieldnames=Directory.schema())
            writer.writerow(dir.to_dict())

    def list_dirs(self):
        with open(self.table_name, mode="r") as f:
            reader = csv.DictReader(f, fieldnames=Directory.schema())

            return list(reader)

    def update_dir(self, updated_dir, old_name):
        dirs = self.list_dirs()

        updated_dirs = []
        for dir in dirs:
            if dir["name"] == old_name:
                updated_dirs.append(updated_dir.to_dict())
            else:
                updated_dirs.append(dir)

        self._save_to_disk(updated_dirs)

    def delete(self, deleted_dir):
        dirs = self.list_dirs()

        dirs.remove(deleted_dir.to_dict())

        self._save_to_disk(dirs)

    def _save_to_disk(self, directories):
        tmp_table_name = self.table_name + ".tmp"
        with open(tmp_table_name, mode="w") as f:
            writer = csv.DictWriter(f, fieldnames=Directory.schema())
            writer.writerows(directories)

        os.remove(self.table_name)
        os.rename(tmp_table_name, self.table_name)
