# coding:utf-8
import os
class getData():
    def data(self,device_name,case_name):
        # 写入数据
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        performance_data = os.path.join(base_dir, 'data')
        # mfile = r"D:\moxiu\youyang\data\shuju1.txt"
        mfile = ('%s\\data.txt' % (performance_data))
        print(mfile)
        fp = open(mfile, 'w+')
        cmd_log = os.popen('adb -s %s shell dumpsys meminfo com.youyouth.video' % device_name)
        fp.write(cmd_log.read())
        fp.close()
        fp2 = open(mfile, 'r')
        list_lines = fp2.readlines()
        fp2.close()
        new = []
        for l in list_lines:
            temp1 = l.strip('\n')
            temp2 = temp1.split(',')
            new.append(temp2)
        native_heap = new[7][0]
        heap_size = float(native_heap[50:60].strip()) / 1024
        heap_alloc = float(native_heap[60:70].strip()) / 1024
        heap_free = float(native_heap[70:77].strip()) / 1024
        values = ('%s,%.2f, %.2f, %.2f' % (case_name,heap_size, heap_alloc, heap_free))
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        performance_data = os.path.join(base_dir, 'data')
        # xfile = r"D:\moxiu\youyang\data\xin.txt"
        xfile = ('%s\\memory_data.txt' % (performance_data))
        fp3 = open(xfile, 'a')
        fp3.write(values + '\n')
        return fp3
if __name__=="__main__":
    a = getData
    a.data("cea8dc6c","冷启动")
