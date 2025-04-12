import os
import struct


class Archive:
    def __init__(self, save_path):
       self.archive_path:str = save_path
       self.archive_list = {}
    def add_archive(self, name, value):
        self.archive_list[name]=value
    def save(self,split=" "):
        if self.archive_path.split(".")[-1] not in ["bin","save","saves"]:
            with open(self.archive_path,"w") as f:
                for i in self.archive_list.keys():
                    f.write(i+split)
                    #TODO 其他的类型的保存
                    f.write(str(self.archive_list[i]))
                    f.write("\n")
                    f.flush()
        else:
            with open(self.archive_path, "wb") as f:
                for i in self.archive_list.keys():
                    if isinstance(self.archive_list[i],int):
                        s = struct.Struct("i")
                        f.write(bytes(len(i)))
                        print(len(i))
                        f.write(bytes(ord(i)))
                        print(bytes(ord(i)))
                        f.write(s.pack(self.archive_list[i]))
                        print(s.pack(self.archive_list[i]))
