# Chapter 9

## Background
This markdown refers to 
- [**Chapter 9-1: Background-1**](https://www.youtube.com/watch?v=r6LkcFY093M&list=PLwD0kbgjHKhHaUh1mnJIuwm6otLQW3_UP&index=57)
- [**Chapter 9-1:  Background-2**](https://www.youtube.com/watch?v=e4mKfEFLHGc&list=PLwD0kbgjHKhHaUh1mnJIuwm6otLQW3_UP&index=58)

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
<div align="center" style='display: flex'>
    <img src="images/image-2.png" alt="Memory Protection Diagram" style="max-width: 45%;border-radius: 10px">
    <img src="images/image-3.png" alt="Memory Protection Diagram" style="max-width: 50%;border-radius: 10px"/>
</div>

