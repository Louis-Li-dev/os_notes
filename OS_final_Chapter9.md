# Chapter 9

## Background
This markdown refers to 
- [**Chapter 9-1: Background-1**](https://www.youtube.com/watch?v=r6LkcFY093M&list=PLwD0kbgjHKhHaUh1mnJIuwm6otLQW3_UP&index=57)
- [**Chapter 9-1:  Background-2**](https://www.youtube.com/watch?v=e4mKfEFLHGc&list=PLwD0kbgjHKhHaUh1mnJIuwm6otLQW3_UP&index=58)
- [**Chapter 9-2: Contiguous Memory Allocation-1**](https://www.youtube.com/watch?v=e62l0H4DF6k&list=PLwD0kbgjHKhHaUh1mnJIuwm6otLQW3_UP&index=59)
- [**Chapter 9-2: Contiguous Memory Allocation-2**](https://www.youtube.com/watch?v=SkiBd48_80o&list=PLwD0kbgjHKhHaUh1mnJIuwm6otLQW3_UP&index=60)
---

### Memory Protection

#### 誰保護記憶體？
- **Answer:** 硬體

#### 怎麼檢查？
- **Answer:**
  1. **Base Register**  
  2. **Limit Register**  
     - (這兩個暫存器只有 OS 能填寫)
     - 屬於 **Privileged Instruction** （特權指令）

---

<div align="center">
    <img src="images/image.png" alt="Memory Protection Diagram" style="max-width: 70%; border-radius: 10px">
</div>

### 程式開發步驟
---
1. **source code** 編譯成 **object files**
2. **linker** 把 **object files** 結合成 **執行檔** 
3. **loader** 將 **program**  丟進 **memory** 裡面等待執行 
<div align="center">
    <img src="images/image-1.png" alt="Memory Protection Diagram" style="max-width: 70%;border-radius: 10px">
</div>

* **Address binding**: 從一個Address space轉道另一個Address space -> 變數轉換成記憶體位置就是binding

#### 甚麼時候做binding
- **Answer:**
    - **complier time:(SIC)**
      - 必須知道執行之後的在記憶體的位址是多少(沒有彈性) 👎
      - symbolic addresses **compile** 時轉成 absolute addresses (abc => 1424) 再 **link**
    - **loading time(SIC/XE)**
      - relocatable code 可以把 relocatable 位址 轉成 實際位址
      - symbolic address **compile** 轉成 relocatable address 再 **link** 跟 **load** 轉成 absolute address *load time 算出來實際的起始位址*
    - **execution time(x86)**
      - 需要hardware support
      - 當前裝置都是這樣 😊
      - CPU生成的位址跟memory看到的 ***不一樣***
      - **Logical address**: CPU 送出來的 virtual address (CPU定義)
      - **Physical address**: 經過轉換出來的真位址 (記憶體大小)
      - **MMU**: relocation register: 把CPU送出來的address加上relocation register獲得physical address

---

### Dynamic Loading
- Routine 只有在**呼叫**的時候才會載入
- 更好的 memory-space 利用率
  - 沒有使用的程式不會被載入
  - 當很多程式在處理不常發生的狀況(處理error)時，除非呼叫才載入，好用👍
### Dynamic Linking
- **Static Linking**: 
  - 大家都用同library時有重複檔案
- **Dynamic Linking**: 
  - link **先作假** 實際 call 的時候才會載入記憶體
  - 載入一次就好了，第二次即可共享

- **Static Linking v.s. Dynamic Linking**
<div align="center" style='display: flex; justify-content: center; align-items: center;'>
    <img src="images/image-2.png" alt="Memory Protection Diagram" style="max-width: 45%;border-radius: 10px">
    <img src="images/image-3.png" alt="Memory Protection Diagram" style="max-width: 50%;border-radius: 10px"/>
</div>

## Contiguous Memory Allocation
* 最直覺的分配方式
- Memory Protection for **relocation and limit register**
  - hardware support
  - limit register: range of addresses
  - relocation register: **最小的 address**
  - MMU: **Logical address -> if < limit register then + relocation register -> physical address**
  - <mark><strong>OS 決定 Relocation 跟 Limit Registers 且 context switch 時會存他們，「save跟restore都會存取跟提取」</strong></mark>
<div align="center" style='display: flex; justify-content: center; align-items: center;'>
    <img src="images/image-4.png" alt="Memory Protection Diagram" style="max-width: 45%;border-radius: 10px">
</div>

- **Memory Allocation**
  - Used partition 
  - Free partition
  - Hole: partition 被釋放
  - <mark>OS紀錄哪些使用到哪些沒使用</mark>
  - Merge: OS merge 隔壁的洞
  <div align="center" style='display: flex; justify-content: center; align-items: center;'>
      <img src="images/image-5.png" alt="Memory Protection Diagram" style="max-width: 45%;border-radius: 10px">
  </div>
  
  - External Fragmentation: process 離開的時候釋放掉的空間 -> 用哪個洞執行程式
    - First fit: 第一個夠大的
    - Best fit: 全部找完，最小的洞 
    - Worst fit: 全部找完，最大的洞
    <mark>First fit 跟 Best Fit 最好，<strong>First fit最快</strong></mark>

    - **50-percent rule**: 
      - N 個分配blocks 中 .5 N 會因Fragmentation 而無用 -> 1/3 memory 無法使用
      - **Sol 1. Compaction**: shuffle memory contents: 往上搬動來整理記憶體 -> 很耗時間
      - **Sol 2. Non-contiguous Memory Allocation**
    - **Non-contiguous**
      - **Internal Fragmentation**(memory internal to a partition): 因memory拆成特定大小的 Blocks **分配的 Block 會大於實際要求的空間**