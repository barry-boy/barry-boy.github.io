## **六: Linux系统管理-磁盘管理**


### **6.1. 磁盘结构**

1. 硬盘的物理结构
  
  - 盘片: 硬盘有多个盘片，每个盘片2面
  - 磁头: 每面一个磁头

2. 硬盘的数据结构
   扇区: 盘片被分为多个扇形区域，每个扇形区存放512字节的数据
   磁道:统一盘片不同半径的同心圆
   柱面:不同盘片相同半径构成的圆柱面


### **6.2. 磁盘接口**


1. IDE（并口）
2. SATA（串口）
   - 速度快
   - 纠错能力强
3. SCSI 

### **6.3. MBR**

1. 定义: MBR 主引导记录
2. 位置: MBR 位于硬盘第一个物理扇区处



### **6.4. 磁盘分区表示**


![20231027170750](https://barry-boy-1311671045.cos.ap-beijing.myqcloud.com/blog/20231027170750.png)