# Chapter 10
- [**Chapter 10-1: Background**](https://www.youtube.com/watch?v=mB2OdZYruFk&list=PLwD0kbgjHKhHaUh1mnJIuwm6otLQW3_UP&index=70)
- [**Chapter 10-2: Demand Paging-1**](https://www.youtube.com/watch?v=bn34DqK_2QU&list=PLwD0kbgjHKhHaUh1mnJIuwm6otLQW3_UP&index=71)
- [**Chapter 10-2: Demand Paging-2**](https://www.youtube.com/watch?v=h27STlhrljo&list=PLwD0kbgjHKhHaUh1mnJIuwm6otLQW3_UP&index=72)
- [**Chapter 10-2: Demand Paging-3**](https://www.youtube.com/watch?v=4zgxz7H-Ns0&list=PLwD0kbgjHKhHaUh1mnJIuwm6otLQW3_UP&index=73)
## Virtual Memory Background

- 不該把整個程式碼傳入記憶體
    - **處理 errors 的程式** (不會被執行到那白做了)
    - Array, list, tables 這些一開始宣告很大但不會被存去到的 → 浪費記憶體空間
    - 特定很少使用 options 跟 features E.g. Word & PowerPoint
- Sol.
    - 載入一部分的程式就好
    - 優點
        - 程式不受限 physical memory 的大小
        - 更少記憶體空間被需要，允許更多 processes 執行
        - I/O 變少了，之前要把所有 pages 都載入記憶體，現在做 swap 跟載入的變少了，因此也比較快

    <div align="center" style='display: flex; justify-content: center; align-items: center;'>
        <img src="images/image-11.png" alt="Memory Protection Diagram" style="max-width: 45%;border-radius: 10px"/>
    </div>

## Demand Paging

- 當「**需要的時候才**」把 page 從硬碟搬到記憶體
- 發生 Page Fault 後 **Page In**
- **Page Fault**:  假設存取 Page 的時候發現他不在記憶體裡面
- **Swapper and Pager**: Swapper: 搬動一整個 process; Pager: 有需要的時候搬 page
- **Page out 時候放哪裡?**
    - 放在 secondary memory (disk partition: swap space or backing store)

- **使用 free frame list**:
    - 當 page fault 時，拿出來用
    - 當 stack 跟 heap 擴增 : hole 在 stack 跟 heap 之間的被填滿時將會使用 free frame list 配置空間

- **zero-fill on demand**
    - 配置之前 zero-out ( 用 0 填滿 )
    - 怕留下**之前 process 的資料在裡面**，因此需要消除

- **了解如何 page 在記憶體裡面**
    - **Hardware Support (MMU)** : **valid-invalid bit** (當時使用 memory protection)，**現在用記憶體管理**
        - invalid: page fault
        - 搬移動作 OS 搬移的，Page Table OS 維護
- **Page Fault Handling**
    1. 若 valid-invalid bit 是 0 → invalid → 觸發 Trap → 
    2. 跳到 OS
    3. Invalid Reference → terminate 
       不在記憶體裡面 → Page In
    4. Free Frame List 找一個 Free Frame，Page 從硬碟搬到記憶體裡 
    5. OS 修改 Page Table $P_i$, frame number 填寫與 valid bit = 1
    6. Restart the instruction
- **Demand Paging 可行的前提**
    - 不要太多 page faults → 否則要一直去硬碟抓資料
    - 程式執行基本上不會產生太多 page faults: 因 ***Locality of Reference*** Demand Paging 的效能不會太差
- **Locality of Reference**
    - **Temporal Locality**: **近期使用到**的指令容易被重複執行
    - **Spatial Locality**: **附近的資料**容易被存取

- **Page Fault Rate**\
    p = 0, no page faults\
    p = 1, every reference is a page fault
